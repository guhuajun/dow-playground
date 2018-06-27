#escape=`

FROM microsoft/windowsservercore:1803

SHELL [ "powershell", "-command" ]

RUN $ErrorActionPreference = 'Stop'; `
    $ProgressPreference = 'SilentlyContinue'; `
    $null = New-Item -Path c:\apps -Type Directory

RUN Invoke-WebRequest -Uri https://download.microsoft.com/download/2/2/5/225F4CFA-8B54-41DB-98C1-47F5A300BBF6/x64_MicrosoftSpeechPlatformSDK/MicrosoftSpeechPlatformSDK.msi `
    -UseBasicParsing -Outfile c:\apps\MicrosoftSpeechPlatformSDK.msi
RUN msiexec /i c:\apps\MicrosoftSpeechPlatformSDK.msi /qn

CMD [ "cmd" ]