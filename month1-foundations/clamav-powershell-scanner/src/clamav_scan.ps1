<#
.SYNOPSIS
Automated ClamAV scan script for local and network paths.
#>

param (
    [string]$ClamPath = "C:\ClamAV",
    [string]$TargetPath = "C:\Users\Public",
    [string]$QuarantinePath = "C:\ClamAV\quarantine",
    [string]$LogFile = "C:\ClamAV\logs\scan_$(Get-Date -Format yyyyMMdd_HHmmss).log"
)

New-Item -ItemType Directory -Force -Path $QuarantinePath, (Split-Path $LogFile) | Out-Null
Write-Host "[INFO] Updating virus definitions..."
& "$ClamPath\freshclam.exe"

Write-Host "[INFO] Starting scan on $TargetPath"
& "$ClamPath\clamscan.exe" -r $TargetPath --infected --move=$QuarantinePath | Tee-Object -FilePath $LogFile
Write-Host "[INFO] Scan complete. Log saved to $LogFile"
