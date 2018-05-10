#escape=`

FROM microsoft/windowsservercore

SHELL [ "powershell", "-command" ]

RUN $ErrorActionPreference = 'Stop'; `
    $ProgressPreference = 'SilentlyContinue'; `
    $null = New-Item -Path c:\apps -Type Directory

RUN Invoke-WebRequest -Uri https://download.sysinternals.com/files/SysinternalsSuite.zip `
                      -UseBasicParsing -OutFile c:\apps\SysinternalsSuite.zip `
                      -Proxy http://192.168.0.124:1080; `
    Expand-Archive -Path C:\apps\SysinternalsSuite.zip -DestinationPath C:\apps\sysinternals\ -Force; `
    Remove-Item -Path c:\apps\SysinternalsSuite.zip

ENTRYPOINT [ "powershell" ]
