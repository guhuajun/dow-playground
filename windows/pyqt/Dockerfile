#escape=`

FROM python:windowsservercore-ltsc2016

SHELL [ "powershell", "-command" ]

RUN $ErrorActionPreference = 'Stop'; `
    $ProgressPreference = 'SilentlyContinue'; `
    $null = New-Item -Path c:\apps -Type Directory

# Install PyQT5
RUN pip install pyqt5
RUN $env:PATH = $env:PATH + 'c:\python\Scripts'; `
    [Environment]::SetEnvironmentVariable('PATH', $env:PATH, [EnvironmentVariableTarget]::Machine)

# Install TightVNC
# RUN Invoke-WebRequest -Uri https://www.tightvnc.com/download/2.8.11/tightvnc-2.8.11-gpl-setup-64bit.msi `
#                       -UseBasicParsing -OutFile c:\apps\tightvnc.msi -Proxy http://192.168.0.124:1080
ADD tightvnc-2.8.11-gpl-setup-64bit.msi c:\apps\tightvnc-2.8.11-gpl-setup-64bit.msi
RUN msiexec /regserver; msiexec /i c:\apps\tightvnc-2.8.11-gpl-setup-64bit.msi /lv* c:\apps\tightvnc.log /qn `
    ADDLOCAL=Server `
    SET_USEVNCAUTHENTICATION=1 `
    VALUE_OF_USEVNCAUTHENTICATION=1 `
    SET_PASSWORD= 1 `
    VALUE_OF_PASSWORD=111111 `
    SET_USECONTROLAUTHENTICATION=1 `
    VALUE_OF_USECONTROLAUTHENTICATION=1;
ADD texteditor.py c:\apps

EXPOSE 5900

CMD [ "python", "c:/apps/texteditor.py" ]