import socket, os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "192.168.61.73" #IP for the host machine
    port = 8001 #port
    path = "E:/Projects/Networks/File transfer/client.py" #path to the file you want to transfer

    s.connect((host, port))
    SIZE = str(os.stat(path).st_size)
    file = open(path, 'rb')
    f_name = os.path.basename(file.name)
    data = f"{SIZE}     {f_name}"
    s.sendall(data.encode())
    if s.recv(2048).decode() == "received":
        s.sendfile(file)
