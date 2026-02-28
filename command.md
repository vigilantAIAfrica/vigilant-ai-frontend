`Get-ChildItem -Directory | ForEach-Object { 
    Write-Host "Updating Repository: $($_.Name)" -ForegroundColor Cyan
    cd $_.FullName
    if (Test-Path .git) {
        git add .
        git commit -m "Automated update: Syncing all Vigilant AI modules"
        git push
    } else {
        Write-Host "Skipping: No git repo found in $($_.Name)" -ForegroundColor Yellow
    }
    cd ..
}
`