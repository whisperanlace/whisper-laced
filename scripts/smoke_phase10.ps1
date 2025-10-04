param([string]$base="http://127.0.0.1:5000")

Write-Host "Health:" (curl.exe -s "$base/health")
Write-Host "Editor ping:" (curl.exe -s "$base/editor/ping")

$doc = @{ title="Smoke Doc"; body="hello world" } | ConvertTo-Json -Compress
$resp = Invoke-RestMethod -Method Post -Uri "$base/editor/documents" -ContentType "application/json" -Body $doc
$docId = $resp.id
Write-Host "Doc created:" ($resp | ConvertTo-Json -Compress)

Write-Host "Doc read:" (curl.exe -s "$base/editor/documents/$docId")
Write-Host "Versions:" (curl.exe -s "$base/editor/documents/$docId/versions")

$enh = @{ instruction="clean up text" } | ConvertTo-Json -Compress
$enhResp = Invoke-RestMethod -Method Post -Uri "$base/editor/documents/$docId/enhance" -ContentType "application/json" -Body $enh
Write-Host "Enhanced:" ($enhResp | ConvertTo-Json -Compress)

Write-Host "Versions after:" (curl.exe -s "$base/editor/documents/$docId/versions")
Write-Host "Enhancements:" (curl.exe -s "$base/enhancements/")
