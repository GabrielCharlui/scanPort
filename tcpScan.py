import socket

host = input ("Enter the host or IP address to check: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input("Enter the port to check: ")))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((host, port))
    
    if code == 0:
        print(f"Port {port} is open on {host}.")
    else:
        print(f"Port {port} is closed on {host}.")
    
print("Scan Completed")
