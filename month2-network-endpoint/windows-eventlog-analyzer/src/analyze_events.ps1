<#
Parses Windows Security log for failed logons and suspicious PowerShell usage.
#>
$failed = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 2000
$ps_abuse = Get-WinEvent -FilterHashtable @{LogName='Windows PowerShell'; Id=4104} -MaxEvents 2000
$failed | Select-Object TimeCreated, Message | Out-File .\failed_logons.txt
$ps_abuse | Select-Object TimeCreated, Message | Out-File .\ps_transcript.txt
Write-Host "Saved failed_logons.txt and ps_transcript.txt"
