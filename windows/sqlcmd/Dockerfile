FROM microsoft/nanoserver:1803

RUN mkdir apps
ADD MsSqlCmdLnUtils.msi c:/apps/MsSqlCmdLnUtils.msi

RUN msiexec /i c:/apps/MsSqlCmdLnUtils.msi /qn

CMD [ "cmd" ]