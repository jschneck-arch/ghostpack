import socket

# Set destination address and port
dst_addr = "192.168.1.1"
dst_port = 80

# Create socket
s = socket.(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# Set the source address to a spoofed address
s.bind(("10.0.0.1", 0))

# Send ghost packet
s.sendto(b"", (dst_addr,dst_port))

# Close the socket
s.close()