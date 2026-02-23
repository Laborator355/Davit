Write-Host "System Information"
Write-Host "------------------"

Write-Host "CPU Info:"
(Get-CimInstance CIM_Processor | Select-Object -First 1).Name

Write-Host "CPU ID:"
(Get-CimInstance CIM_Processor | Select-Object -First 1).ProcessorId

Write-Host "Memory:"
$mem = Get-CimInstance CIM_OperatingSystem
$totalGB = [math]::Round($mem.TotalVisibleMemorySize / 1MB, 2)
$freeGB = [math]::Round($mem.FreePhysicalMemory / 1MB, 2)
Write-Host "Total: $totalGB GB | Free: $freeGB GB"

Write-Host "`nDisk:"
Get-Volume | Where-Object DriveType -eq 'Fixed' | Format-Table DriveLetter, FileSystemLabel, SizeRemaining, Size

Write-Host "MAC address:"
Get-NetAdapter | Where-Object Status -eq 'Up' | Format-Table Name, MacAddress

Write-Host "OS version:"
$os = Get-CimInstance CIM_OperatingSystem
Write-Host "$($os.Caption) $($os.Version)"