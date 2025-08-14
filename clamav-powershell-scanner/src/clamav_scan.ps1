<#
.SYNOPSIS
Automated ClamAV scan script for local and network paths.

.DESCRIPTION
- Updates ClamAV signatures using freshclam
- Runs recursive scans on target paths
- Quarantines infected files
- Logs results with timestamps
#>

param (
    [string]$ClamPath = "C:\ClamAV",
    [string]$TargetPath = "C:\Users\Public",
    [string]$QuarantinePath = "C:\ClamAV\quarantine",
    [string]$LogFile = "C:\ClamAV\logs\scan_$(Get-Date -Format yyyyMMdd_HHmmss).log"
)

# Ensure quarantine and log folders exist
New-Item -ItemType Directory -Force -Path $QuarantinePath, (Split-Path $LogFile) | Out-Null

# Update virus definitions
Write-Host "[INFO] Updating virus definitions..."
& "$ClamPath\freshclam.exe"

# Run scan
Write-Host "[INFO] Starting scan on $TargetPath"
& "$ClamPath\clamscan.exe" -r $TargetPath --infected --move=$QuarantinePath `
| Tee-Object -FilePath $LogFile

Write-Host "[INFO] Scan complete. Log saved to $LogFile"
