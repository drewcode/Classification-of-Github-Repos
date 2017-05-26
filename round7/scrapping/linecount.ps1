param(
[string]$filename
)

$linecount = 0
gc $filename |% {$linecount ++}
write-host "Number of lines: " $linecount