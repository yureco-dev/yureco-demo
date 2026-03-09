import re, glob
root='/mnt/data/navfix/guide'
html_files=glob.glob(root+'/**/*.html', recursive=True)
script='''<script id="auto-active-nav">
(function () {
  // Normalize current path (no trailing slash)
  var path = window.location.pathname.replace(/\/+/, "/").replace(/\/$/, "");
  // Treat "/" as "/index.html" for matching convenience
  var pathAlt = (path === "" || path === "/") ? "/index.html" : path;

  var links = document.querySelectorAll('nav a[href], .sidebar a[href]');
  links.forEach(function(a){
    var href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;

    var url;
    try { url = new URL(href, window.location.origin); } catch (e) { return; }
    var p = url.pathname.replace(/\/+/, "/").replace(/\/$/, "");
    var pAlt = (p === "" || p === "/") ? "/index.html" : p;

    if (pAlt === pathAlt) {
      a.classList.add('active');
    }
  });
})();
</script>'''

changed=0
for fp in html_files:
    with open(fp,'r',encoding='utf-8') as f:
        s=f.read()
    orig=s
    # remove hardcoded active class attrs
    s=re.sub(r'\sclass="active"','',s)
    if 'id="auto-active-nav"' not in s:
        if '</body>' in s:
            s=s.replace('</body>', script+'\n</body>')
        else:
            s += '\n'+script+'\n'
    if s!=orig:
        with open(fp,'w',encoding='utf-8') as f:
            f.write(s)
        changed += 1
print('files_modified', changed)
# sanity: ensure no class="active" remains
import subprocess, shlex, os
res=subprocess.run(['bash','-lc', f"grep -R \"class=\\\"active\\\"\" -n {root} | wc -l"], capture_output=True, text=True)
print('remaining_hardcoded_active', res.stdout.strip())
