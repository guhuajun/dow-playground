
$dt  = (Get-Date).ToString('yyyyMMddHHmm')
$image_name = "demo/sysinternals"

$tag = [string]::Format("{0}:{1}", $image_name, $dt)

docker build --rm --tag $tag .