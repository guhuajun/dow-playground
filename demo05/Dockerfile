# escape=`
# Modified from Docker On Windows ch02-hitcount-website
FROM microsoft/aspnetcore-build:1.1 AS builder

WORKDIR C:\src
COPY src .

RUN dotnet restore; `
    dotnet publish

# app image
FROM microsoft/aspnetcore:1.1

WORKDIR C:\dotnetapp
RUN New-Item -Type Directory -Path .\app-state

CMD ["dotnet", "HitCountWebApp.dll"]
COPY --from=builder C:\src\bin\Debug\netcoreapp1.1\publish .