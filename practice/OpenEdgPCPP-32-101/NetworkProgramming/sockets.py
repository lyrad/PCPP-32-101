import socket

# Asynchronous I/O (asyncio) -> Correct. Asynchronous I/O (asyncio) is a programming paradigm in Python that enables
# efficient and scalable network communication. It allows handling a large number of concurrent connections with a
# single thread by utilizing non-blocking I/O operations and coroutines. asyncio provides built-in support
# for writing high-performance networking code.

# Sockets domains: Initially, UNIX sockets (computer internal network) and internet domains (INET).
# IP: 32 bits long addresses, not a reliable protocol (datagrams can be lost/corrupted).
# TCP (Transmission Control Protocol), uses handshakes to construct a reliable communication channel (stream data reach the target intact).
# UDP (User Datagram Protocol) is faster than TCP (no handshake, less reliable).
# Socket address: IP + Port
# Socket/service number (Port): 16 bits long integer used to identify the service.

# Exception:
# ConnectionError: generic for connections.
# ConnectionRefusedError: when server refuse the connection.
# SocketTimeoutError: not specific for connections.

## Client socket.
# server_addr = input("What server do you want to connect to? ")
server_addr = 'www.google.fr'
# server_addr = 'asdasd.asdasd.asdasd'
# SOCK_STREAM => TCP (send characters...), SOCK_DGRAM => UDP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Works with UDP? No.
    sock.connect((server_addr, 80))

    # When UDP, and socket not in connected mode yet, we can use sento.
    # sock.sendto(b"GET...", (server_addr, 80));

    # b convert the string into bytes, Connection: close|keep-alive (set server connection management mode).
    sock.send(b"GET / HTTP/1.1\r\nHost: " + bytes(server_addr, "utf8") + b"\r\nConnection: close\r\n\r\n")

    # recv arg max response length (recv internal buffer), keep invoking recv as far the total response is not read.
    reply = sock.recv(10000)

    # SHUT_RD: we declare we won't reading server's messages, SHUT_WR: won't say a word, SHUT_RDWR: both.
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

    # repr: textual representation of an object.
    print(repr(reply))

except socket.gaierror as error:
    #
    # socket.gaierror comes from lower level function getaddrinfo() (malformed or non existent IP/domain...).
    print(f'error: {type(error)}, message: {error}')
except socket.timeout as error:
    # Timeout could be set using settimeout().
    print(f'error: {type(error)}, message: {error}')


## Server socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# address: socket.gethostname() (hostname, visible from outside world), '' (any address of the machine)
serversocket.bind(('127.0.0.1', 8081))
# Arg: max number of connection (5 max).
serversocket.listen(5)

while(True):
    conn, addr = serversocket.accept()
    conn.send('kikkooo')
    conn.close()