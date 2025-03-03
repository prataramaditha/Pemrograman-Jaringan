import socket

HOST = "localhost"
PORT = 9806

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nama = input("Nama: ")
nim = input("NIM: ")
tahun_lahir = input("Tahun Lahir: ")

data = f"{nama},{nim},{tahun_lahir}"
client.send(data.encode("utf-8"))

response = client.recv(1024).decode("utf-8")
print("Server:", response)

client.close()
