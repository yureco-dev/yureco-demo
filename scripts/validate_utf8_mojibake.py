#!/usr/bin/env python3
import os
import sys

def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to repo root
    repo_root = os.path.dirname(repo_root)
    
    report_file = os.path.join(repo_root, 'validation_utf8_mojibake_report.txt')
    
    mojibake_markers = ['Ð', 'Ñ', 'Ã', 'Â', '�']
    
    results = []
    has_issues = False
    
    for root, dirs, files in os.walk(repo_root):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                utf8_status = 'ok'
                mojibake_status = 'clean'
                charset_status = 'missing'
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check for mojibake
                    if any(marker in content for marker in mojibake_markers):
                        mojibake_status = 'mojibake_found'
                        has_issues = True
                    
                    # Check for charset meta
                    if 'charset="utf-8"' in content or 'charset="UTF-8"' in content:
                        charset_status = 'present'
                    else:
                        has_issues = True
                        
                except UnicodeDecodeError:
                    utf8_status = 'read_error'
                    has_issues = True
                    mojibake_status = 'N/A'  # Can't check if can't read
                    charset_status = 'N/A'
                
                results.append(f"{filepath}\t{utf8_status}\t{mojibake_status}\t{charset_status}")
    
    # Write report
    with open(report_file, 'w', encoding='utf-8') as f:
        for line in results:
            f.write(line + '\n')
    
    sys.exit(0 if not has_issues else 1)

if __name__ == '__main__':
    main()