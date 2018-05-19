FROM microsoft/windowsservercore:latest

SHELL [ "powershell", "-command" ]

RUN $ErrorActionPreference = 'Stop'
RUN $ProgressPreference = 'SilentlyContinue'
RUN $null = New-Item -Path c:\apps -Type Directory