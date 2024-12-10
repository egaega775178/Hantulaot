#!/usr/bin/python3
# -*- coding: utf-8 -*-
# WGen - Wordlist Generator (4 Jan 2018 (14:32))
# Author: DedSecTL/DTL/Gameye98
# Team: BlackHole Security
# Github: https://github.com/Gameye98
# Blog: http://droidsec9798-com.mwapblog.com
import os
import sys
import time

def jalankan_ulang_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def bersih_layar():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

wgen_banner = """\033[1;37m __      __    ________                 
/  \    /  \  /  _____/    ____     ____   
\   \/\/   / /   \  ___  _/ __ \   /    \  
 \        /  \    \_\  \ \  ___/  |   |  \ 
  \__/\  /    \______  /  \___  > |___|  / 
       \/            \/       \/       \/  
 W O R D L I S T   #   G E N E R A T O R\033[0m
"""

bersih_layar()
print(wgen_banner)
print('\033[1;37mtekan "bantuan" untuk dapatkan menu bantuan\033[0m')
print()

interpreter = '*>'
if os.geteuid() == 0:
    interpreter = '#>'

bantuan = """\033[1;37m
Menu Bantuan WGen:
    Perintah   Deskripsi
    --------   ----------
    bantuan    dapatkan menu bantuan
    bersih     bersihkan layar
    hasilkan   hasilkan wordlist
    ulang      jalankan ulang program
    keluar     keluar dari program\033[0m
"""

opt = True
while opt:
    wgen = input('\033[1;37mWGen' + interpreter + ' ')
    if wgen == 'bantuan':
        print(bantuan)
    elif wgen == 'bersih':
        bersih_layar()
    elif wgen == 'hasilkan':
        try:
            a = input("\nWGen?> Nama Depan: ")
            with open(f"{a}.txt", 'w') as file:
                b = input("WGen?> Nama Tengah: ")
                c = input("WGen?> Nama Belakang: ")
                d = input("WGen?> Nama Panggilan: ")
                e = input("WGen?> Tanggal Lahir (ex: DDMMYY): ")
                f, g, h = e[0:2], e[2:4], e[4:]
                i = input("\nWGen?> Nama Pacar: ")
                j = input("WGen?> Nama Panggilan Pacar: ")
                k = input("WGen?> Tanggal Lahir Pacar (ex: DDMMYY): ")
                l, m, n = k[0:2], k[2:4], k[4:]

                file.write(f"{a}{c}\n")
                file.write(f"{a}{b}{a}{b}{a}{c}\n")
                # Generate combinations and write to file
                for wg in range(1, 101):
                    file.write(f"{a}{wg}\n")
                for en in range(1, 101):
                    file.write(f"{i}{en}\n")
                for word in range(1, 101):
                    file.write(f"{d}{word}\n")
                for gen in range(1, 101):
                    file.write(f"{j}{gen}\n")

                time.sleep(1.5)
                print(f" \n[+] Selesai. Kumpulan kata disimpan sebagai {a}.txt\n")
        except IOError as e:
            print(f" \n[!] ERROR: {e}")
    elif wgen == 'ulang':
        jalankan_ulang_program()
    elif wgen == 'keluar':
        print("\033[0m")
        opt = False
