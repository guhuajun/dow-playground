# escape=`

FROM microsoft/dotnet-framework-build:3.5-windowsservercore-1709 as builder

WORKDIR c:\src\

COPY src\NerdDinner\packages.config .
RUN nuget restore packages.config -PackagesDirectory ..\packages

COPY src C:\src
RUN msbuild .\NerdDinner\NerdDinner.csproj /p:OutputPath=c:\out\NerdDinner `
            /p:DeployOnBuild=true