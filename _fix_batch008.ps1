$files = @(
  "utylizaciya-ovochiv.html",
  "utylizaciya-paperu-ta-kartonu.html",
  "utylizaciya-parfumeriyi.html",
  "utylizaciya-paverbankiv-dbj.html",
  "utylizaciya-plastyku-ta-polimeriv.html",
  "utylizaciya-produktiv-harchuvannya-napoyiv.html",
  "utylizaciya-promyslovogo-obladnannya-mehanizmiv.html",
  "utylizaciya-promyslovyh-vidhodiv.html",
  "utylizaciya-prostrochenoyi-kosmetyky.html",
  "utylizaciya-pyva.html"
)

foreach ($f in $files) {
  $url = "https://guide.youreco.com.ua/$f"
  $path = Join-Path (Get-Location) $f
  $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

  # Step 1: revert incorrect mainEntityOfPage url addition
  $old1 = '"mainEntityOfPage":{"@type":"WebPage","@id":"' + $url + '","url":"' + $url + '"}'
  $new1 = '"mainEntityOfPage":{"@type":"WebPage","@id":"' + $url + '"}'
  $content = $content.Replace($old1, $new1)

  # Step 2: add separate WebPage JSON-LD block before </head>
  $wpBlock = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"' + $url + '"}</script>'
  if (-not $content.Contains($wpBlock)) {
    $content = $content.Replace('</head>', $wpBlock + '</head>')
  }

  [System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))
  Write-Host "DONE: $f"
}
