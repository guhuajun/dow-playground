# escape=`
FROM microsoft/windowsservercore:1803
SHELL [ "powershell", "-Command"]
ADD "http://download.backup4all.com/download/setup/b4asetup.msi" c:/msi/
RUN Start-Process msiexec.exe -ArgumentList '-i', 'c:\msi\b4asetup.msi', '/quiet', '/norestart' -NoNewWindow