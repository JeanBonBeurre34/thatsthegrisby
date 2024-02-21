import socket
import logging
from threading import Thread

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

class FakeAS400:
    def __init__(self):
        self.files = {}

    def execute_command(self, command):
        # Log the command
        logger.info(f"Executing command: {command}")
        
        parts = command.strip().split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "DSPSYSSTS":
            return "Display System Status: System is operational\n"
        elif cmd == "CRTFILE":
            return self.create_file(args)
        elif cmd == "DSPFILES":
            return self.display_files()
        else:
            return "Unknown command\n"

    def create_file(self, args):
        if len(args) != 1:
            return "Error: CRTFILE requires exactly one argument (filename)\n"
        
        filename = args[0]
        if filename in self.files:
            return f"Error: File '{filename}' already exists\n"
        else:
            self.files[filename] = ""
            return f"File '{filename}' created successfully\n"

    def display_files(self):
        if not self.files:
            return "No files in the system.\n"
        else:
            files_list = ", ".join(self.files.keys())
            return f"Files in system: {files_list}\n"

def client_handler(connection, address, as400_system):
    with connection:
        logger.info(f"Connection established with {address}")
        connection.sendall(b"AS/400 system. Type 'exit' to quit.\n")
        
        while True:
            connection.sendall(b"Enter command: ")
            command = connection.recv(1024).decode().strip()
            if command.lower() == 'exit':
                break
            response = as400_system.execute_command(command)
            connection.sendall(response.encode())

def main():
    HOST = '0.0.0.0'  # Symbolic name meaning all available interfaces
    PORT = 23  # Port to listen on (non-privileged ports are > 1023)

    as400_system = FakeAS400()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logger.info(f"Server listening on port {PORT}...")

        while True:
            conn, addr = server_socket.accept()
            client_thread = Thread(target=client_handler, args=(conn, addr, as400_system))
            client_thread.start()

if __name__ == "__main__":
    main()
