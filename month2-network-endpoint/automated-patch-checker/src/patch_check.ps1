<#
Naive patch checker: lists installed programs and compares to a local CSV of latest versions.
Provide latest_versions.csv with columns: Name,LatestVersion
#>
$installed = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* ,
                          HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |
             Select-Object DisplayName, DisplayVersion | Where-Object {$_.DisplayName}
$latest = Import-Csv .\latest_versions.csv
foreach ($app in $installed) {
    $match = $latest | Where-Object { $_.Name -eq $app.DisplayName }
    if ($match) {
        if ($app.DisplayVersion -ne $match.LatestVersion) {
            Write-Host "[OUTDATED] $($app.DisplayName): $($app.DisplayVersion) < $($match.LatestVersion)"
        }
    }
}
