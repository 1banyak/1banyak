import socket
import time
import subprocess

def run(nama):
    try:
        subprocess.run(nama, shell=True, check=True, timeout=1)
    except:
        pass

def Gae(): 
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 14128))
    sok.send("'/gae':print".encode())  # Pastikan format pesan sesuai
    sok.close()

    servr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servr.bind(("localhost", 3772))
    servr.listen()
    con, add = servr.accept()
    bdata = b''
    while True:
        data = con.recv(1024)
        if len(data)>0:
            bdata+=data
            
        elif len(data)==0:
            break
    servr.close()
    return bdata.decode()
    
def BukaUrl(gandolan):
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 14128))
    sok.send(f"'/gandolan':{gandolan}".encode())  # Pastikan format pesan sesuai
    sok.close()
    

def KodeJS(kode):
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 14128))
    sok.send(f"'/kode':{kode}".encode())  # Pastikan format pesan sesuai
    sok.close()

def GantiUA(ua):
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 14128))
    sok.send(f"'/ua':{ua}".encode())  # Pastikan format pesan sesuai
    sok.close()
    
"""
const elements = document.querySelectorAll('.namaClass');
const elements = document.getElementsByClassName('namaClass');
const elements = document.getElementsByName('nama');
const elements = document.getElementsByTagName('tag');
const element = document.getElementById('namaID');
const element = document.querySelector('.namaClass');
const elements = document.querySelectorAll('.namaClass');

def NyimpenWayah(): 
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 14128))
    sok.send("'/NyimpenWayah':SimpanSesi".encode())  # Pastikan format pesan sesuai
    sok.close()

    servr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servr.bind(("localhost", 3772))
    servr.listen()
    con, add = servr.accept()
    bdata = b''
    while True:
        data = con.recv(1024)
        if len(data)>0:
            bdata+=data
            
        elif len(data)==0:
            break
    servr.close()
    return bdata

def GaeWayah(data): 
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 14128))
    sok.send("'/GaeWayah':".encode())  # Pastikan format pesan sesuai
    sok.close()

    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect(("localhost", 1412))
    sok.send(data)  # Pastikan format pesan sesuai
    sok.close()
    
"""
