$parentFolder = "C:/Iphone_copy"
Set-Location -Path $parentFolder

$extensions = @(
    "*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp",
    "*.mp4", "*.avi", "*.mkv", "*.mov", "*.wmv", "*.flv", "*.webm"
)

foreach ($ext in $extensions) {
    Get-ChildItem -Path $parentFolder -Filter $ext -Recurse -File | 
    ForEach-Object {
        $newPath = Join-Path -Path $parentFolder -ChildPath $_.Name
        $counter = 1
        while (Test-Path $newPath) {
            $newName = "{0}_{1}{2}" -f $_.BaseName, $counter, $_.Extension
            $newPath = Join-Path -Path $parentFolder -ChildPath $newName
            $counter++
        }
        Move-Item -Path $_.FullName -Destination $newPath
    }
}

Get-ChildItem -Path $parentFolder -Directory | Remove-Item -Recurse -Force