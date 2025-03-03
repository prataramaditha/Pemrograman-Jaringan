import socket

HOST = "localhost"
PORT = 9807

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server chat berjalan...")

conn, addr = server.accept()
print(f"Koneksi diterima dari {addr}")

while True:
    pesan = conn.recv(1024).decode("utf-8")
    if pesan.lower() == "exit":
        print("Client keluar.")
        break
    print("Client:", pesan)
    balasan = input("Server: ")
    conn.send(balasan.encode("utf-8"))

conn.close()
server.close()
