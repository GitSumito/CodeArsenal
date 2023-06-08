# Select the base image
FROM arm64v8/ubuntu:latest

# Update the package lists for upgrades for security purposes
RUN apt-get update && apt-get upgrade -y

# Install necessary tools
RUN apt-get install -y curl wget tar sudo

# Install the ICU library
RUN apt-get install -y libicu-dev

# Download the PowerShell binary
RUN wget -O /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.3.4/powershell-7.3.4-linux-arm64.tar.gz

# Create the target folder where PowerShell will be placed
RUN mkdir -p /usr/local/microsoft/powershell/7.3.4

# Expand PowerShell to the target folder
RUN tar zxf /tmp/powershell.tar.gz -C /usr/local/microsoft/powershell/7.3.4

# Set execute permissions
RUN chmod +x /usr/local/microsoft/powershell/7.3.4/pwsh

# Create a symbolic link that points to pwsh
RUN ln -s /usr/local/microsoft/powershell/7.3.4/pwsh /usr/local/bin/pwsh

# Install necessary PowerShell modules
RUN pwsh -Command Install-Module -Name ExchangePowerShell -F
RUN pwsh -Command Install-Module -Name Microsoft.Graph -F

