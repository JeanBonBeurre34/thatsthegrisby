# That's a grisby is AS/400 Honeypot

## Overview
This project simulates an AS/400 (IBM iSeries) system to function as a honey pot, capturing and logging interactions from clients. It listens on port 23 (Telnet) and supports basic commands to mimic the behavior of an AS/400 system. This tool is intended for educational purposes, security research, and to enhance network security by deceiving attackers.

## Features
- Simulates basic AS/400 system commands.
- Runs as a network service listening on port 23.
- Logs all commands executed by the client.
- Dockerized application for easy deployment and isolation.

## Prerequisites
- Docker

## Installation

### Building the Docker Image
1. Clone the repository or download the source code.
2. Navigate to the project directory where the `Dockerfile` and `as400honey.py` are located.
3. Build the Docker image:
    ```bash
    docker build -t as400-honey-image .
    ```

### Running the Docker Container
Run the container with the following command:
```bash
docker run --name as400-honey-container -p 23:23 as400-honey-image

This command maps port 23 on the host to port 23 in the container where the honey pot service is listening.

## Usage
After starting the Docker container, the honey pot service will be listening on port 23. You can connect to it using a Telnet client:
```bash
telnet <host_ip> 23
```

Replace <host_ip> with the IP address of the Docker host. Interact with the simulated AS/400 system using supported commands.

## Logging
All commands executed by clients are logged. In the Docker environment, logs are written to standard output and can be viewed using:
```bash
docker logs as400-honey-container
```

## Security Notice
This project uses Telnet for simplicity and educational purposes. Telnet is not secure for real-world deployments. This honey pot should be deployed in a controlled environment, preferably behind firewalls or in isolated networks, to prevent unauthorized access to real systems or networks.

## Contributing
Contributions to the project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License
'This project is licensed under the MIT License - see the LICENSE.md file for details.

## Disclaimer
This project is for educational and research purposes only. The author is not responsible for misuse or for any damage that may occur from using this tool.
