$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..')
$OutputFile = Join-Path $RepoRoot 'docs/qa/remediation/cta_mismatch_list_current.txt'
$ValidatorScript = Join-Path $RepoRoot 'tools/validators/validate_cta_mismatch_detection.py'

function Invoke-Validator {
  param(
    [string]$ScriptPath
  )

  $previousErrorActionPreference = $ErrorActionPreference
  try {
    $ErrorActionPreference = 'Continue'
    $output = & py -3 $ScriptPath 2>&1
    $exitCode = $LASTEXITCODE
  } finally {
    $ErrorActionPreference = $previousErrorActionPreference
  }

  if ($exitCode -eq 0) {
    return $output
  }

  if (($output -join "`n") -match 'No installed Python found!') {
    $output = & python $ScriptPath 2>&1
  }

  return $output
}

if (-not (Test-Path $OutputFile)) {
  Write-Output 'FAIL: file missing'
  exit 0
}

$ValidatorOutput = Invoke-Validator -ScriptPath $ValidatorScript
$Expected = @(
  $ValidatorOutput | ForEach-Object {
    if ($_ -match '^CTA_MISMATCH_DETECTED\s+(.+?\.html)\s+reasons=\[.*\]\s*$') {
      $matches[1]
    }
  }
)
$Actual = @(Get-Content $OutputFile)

if (($Expected.Count -eq $Actual.Count) -and (@(Compare-Object -ReferenceObject $Expected -DifferenceObject $Actual).Count -eq 0)) {
  Write-Output 'PASS'
} else {
  Write-Output 'FAIL: list is out of date'
}

exit 0
