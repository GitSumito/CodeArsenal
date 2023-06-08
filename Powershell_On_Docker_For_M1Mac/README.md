# PowerShell on ARM64 Ubuntu Docker Container
This repository contains a Dockerfile that builds a Docker container with PowerShell installed on an ARM64 Ubuntu base image.

# Overview
The Dockerfile is configured to:

Use an ARM64 architecture Ubuntu base image.
Update the package lists and upgrade installed packages for security purposes.
Install necessary tools like curl, wget, tar, and sudo.
Install the ICU library, which is required for globalization support in .NET applications.
Download and install PowerShell 7.3.4 for ARM64.
Set execute permissions on the PowerShell binary.
Create a symbolic link so that PowerShell can be run using the pwsh command.
Install the ExchangePowerShell and Microsoft.Graph PowerShell modules.
Prerequisites
Docker is installed on your machine.
Your machine must support ARM64 architecture.
Build the Docker Image
To build the Docker image, navigate to the directory containing the Dockerfile and run:

```
docker build -t arm64-ubuntu-powershell .
This command will create a Docker image named arm64-ubuntu-powershell.
```

Run the Docker Container
To run the Docker container:

```
docker run -it --rm arm64-ubuntu-powershell pwsh
This command will start a PowerShell session within the Docker container.
```

# Contributing
If you want to contribute to this project, feel free to submit pull requests or create issues to report bugs or ask for new features.

# License
Please see the license file in this repository for licensing information.

# Disclaimer
This Dockerfile and container are provided as-is, without warranties. Please use them at your own risk.
