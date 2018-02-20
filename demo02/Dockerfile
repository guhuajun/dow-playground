FROM microsoft/dotnet:2-sdk

COPY demo02/ c:/apps/demo02/

WORKDIR c:/apps/demo02/
RUN dotnet restore
RUN dotnet build
CMD ["dotnet", "run"]