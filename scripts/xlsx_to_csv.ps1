param(
  [Parameter(Mandatory=$true)] [string] $XlsxPath
)

$ErrorActionPreference = 'Stop'

if (!(Test-Path $XlsxPath)) {
  Write-Error "File not found: $XlsxPath"
  exit 1
}

Write-Output "Exporting sheets from: $XlsxPath"

$excel = $null
$wb = $null
try {
  $excel = New-Object -ComObject Excel.Application
  $excel.Visible = $false
  $wb = $excel.Workbooks.Open($XlsxPath)

  foreach ($ws in $wb.Worksheets) {
    $csvPath = Join-Path (Split-Path $XlsxPath -Parent) ("$($ws.Name).csv")
    Write-Output (" -> " + $csvPath)
    $ws.SaveAs($csvPath, 6) # xlCSV = 6
  }
}
finally {
  if ($wb) { $wb.Close($false) }
  if ($excel) { $excel.Quit() }
}

Write-Output "Done."


