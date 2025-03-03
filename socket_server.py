import socket
from datetime import datetime

def hitung_umur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    return tahun_sekarang - tahun_lahir

HOST = "localhost"
PORT = 9806

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server berjalan di {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Koneksi dari {addr}")

data = conn.recv(1024).decode("utf-8")
nama, nim, tahun_lahir = data.split(",")

umur = hitung_umur(int(tahun_lahir))
response = f"Hello {nama} NIM: {nim}, umur kamu sekarang {umur} tahun."

conn.send(response.encode("utf-8"))
conn.close()
server.close()
