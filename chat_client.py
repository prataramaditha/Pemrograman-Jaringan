import socket

# Konfigurasi client
HOST = "localhost"
PORT = 9807

# Inisialisasi client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Proses komunikasi
while True:
    pesan = input("Client: ")
    client.sendall(pesan.encode("utf-8"))
    if pesan.strip().lower() == "exit":
        break
    balasan = client.recv(1024).decode("utf-8")
    print(f"Server: {balasan}")

# Menutup koneksi
client.close()
