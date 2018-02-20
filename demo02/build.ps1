Set-Location -Path demo02
dotnet publish
Set-Location -Path ".."

docker image build --file Dockerfile.slim --tag greggu/demo02 .
