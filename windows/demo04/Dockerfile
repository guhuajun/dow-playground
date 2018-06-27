#escape=`

FROM microsoft/aspnet

SHELL [ "powershell", "-command" ]

RUN $ErrorActionPreference = 'Stop'; `
    $ProgressPreference = 'SilentlyContinue';
    
RUN Enable-WindowsOptionalFeature -Online -FeatureName "MSMQ" -All -LimitAccess; `
    Enable-WindowsOptionalFeature -Online -FeatureName "MSMQ-Server" -All -LimitAccess
