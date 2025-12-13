import socket
import time
target = "192.168.47.133"  # Localhost for testing
print(f"Starting scan on host: {target}")

start_time = time.time()

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.3)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Open")
    sock.close()

print(f"Scanning completed in {time.time() - start_time:.2f} seconds")    
