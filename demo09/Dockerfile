# escape=`

FROM microsoft/aspnet:4.7.1

SHELL [ "powershell" ]

RUN Remove-WebSite -Name 'Default Web Site'; `
    mkdir c:\umbracocms `
    New-Website -Name 'umbracocms' `
                -Port 8081 -PhysicalPath 'c:\umbracocms' `
                -ApplicationPool '.NET v4.5'

COPY umbracocms/ c:\umbracocms\
