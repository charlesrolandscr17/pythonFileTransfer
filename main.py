import socket, tqdm
#tqdm for a progress bar

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ip = socket.gethostbyname(socket.gethostname()) #get host ip address
    port = 8001 #port
    b = 0
    SIZE = 5120

    s.bind((ip, port))

    print(ip)
    print("Connection Bound")

    s.listen()

    conn, add = s.accept()
    print(f"Connection from {add}")

    while True:
        data = conn.recv(SIZE)
        # check if the filename and size have been sent
        if not b:
            b = conn.send(b'received')
            file = open(data.decode().split("     ")[1], 'wb')
            SIZE = int(data.decode().split("     ")[0])
            if len(data.decode().split("     ")[1]) > 5:
                progress = tqdm.tqdm(range(SIZE), f"sending file: {' '.join(data.decode().split('     ')[1].split(' ')[:5])}...", unit="B", unit_scale=True, unit_divisor=1024)
            else:
                progress = tqdm.tqdm(range(SIZE), f"sending file: {file}", unit="B", unit_scale=True, unit_divisor=1024)
        else:
            progress.update(len(data))
            file.write(data)

        if not data:
            break


    conn.close()



# print(socket.gethostbyname(socket.gethostname()))
