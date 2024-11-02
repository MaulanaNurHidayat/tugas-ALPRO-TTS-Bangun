# Nama : Maulana Nur Hidayat
# NPM  : 2413020149

import math
while True:
    print ("""
---> SELAMAT DATANG DI PROGRAM HITUNG BANGUN <---
 A. BANGUN DATAR
    1. Belah Ketupat
    2. Segitiga ( sama kaki, sama sisi, siku-siku, lancip )
    3. Layang-layang         
 B. BANGUN RUANG
    1. Kubus
    2. Tabung
    3. Limas ( Segi empat, Segi lima, Segi enam )""")
    
    list = input ("Silahkan pilih bangun diatas ( pilih A/B) : ")
    if list == "A" :
        print (""" 1. Belah Ketupat
 2. Segitiga ( sama kaki, sama sisi, siku-siku, lancip )
 3. Layang-layang""")
        bangun_datar= input ("\nmasukkan bangun datar ( pilih angka 1-3) : ")
        if bangun_datar == "1":
            d1 = float (input ("Masukkan panjang diagonal 1 : "))
            d2 = float (input ("Masukkan panjang diagonal 2 : "))
            luas = 1/2 * (d1 * d2)
            sisi = float(input("Masukkan nilai sisi : "))
            keliling = 4 * (sisi)
            print ("\nAnda memilih bangun datar")
            print ("   Nama Bangun : Belah Ketupat")
            print (f"   Luas        : {luas}")
            print (f"   Keliling    : {keliling}")
        elif bangun_datar == "2" :
           print (""" a. sama kaki
 b. sama sisi
 c. siku - siku
 d. lancip""")
           segitiga = input ("\nmasukkan pilihan (gunakan huruf 'a-d') : ")
           if segitiga =='a':
               a = float (input("Masukkan panjang alas segitiga : "))
               b = float (input("Masukkan panjang sisi miring segitiga : "))
               hitung_tinggi = math.sqrt(b**2 - (a/2)**2)
               hitung_luas = 0.5 * a * hitung_tinggi
               hitung_keliling = a + 2 * b
               print ("\nAnda memilih bangun datar")
               print ("   Nama Bangun : Segitiga Sama kaki")
               print (f"   Luas        : {hitung_luas}")
               print (f"   Keliling    : {hitung_keliling}")
           elif segitiga == 'b' :
               s = float(input("Masukkan panjang sisi segitiga sama sisi : "))
               hitung_tinggi = (math.sqrt(3) / 2) * s
               hitung_luas = (math.sqrt(3) / 4) * s**2
               hitung_keliling = 3 * s
               print ("\nAnda memilih bangun datar")
               print ("   Nama Bangun : Segitiga Sama sisi")
               print (f"   Luas        : {hitung_luas}")
               print (f"   Keliling    : {hitung_keliling}")
           elif segitiga == 'c' :
               a = float(input("Masukkan panjang alas segitiga : "))
               b = float(input("Masukkan panjang tinggi segitiga : "))
               hitung_sisi_miring = math.sqrt(a**2 + b**2)
               hitung_luas = 0.5 * a * b
               hitung_keliling = a + b + hitung_sisi_miring
               print ("\nAnda memilih bangun datar")
               print ("   Nama Bangun : Segitiga Siku")
               print (f"   Luas        : {hitung_luas}")
               print (f"   Keliling    : {hitung_keliling}")
           elif segitiga == 'd' :
               a = float(input("Masukkan panjang sisi a : "))
               b = float(input("Masukkan panjang sisi b : "))
               c = float(input("Masukkan panjang sisi c : "))
               hitung_semiperimeter = (a + b + c) / 2
               hitung_luas = math.sqrt(hitung_semiperimeter * (hitung_semiperimeter - a) * (hitung_semiperimeter - c))
               hitung_keliling = a + b + c
               hitung_tinggi_a = (2 * hitung_luas) / a
               print ("\nAnda memilih bangun datar")
               print ("   Nama Bangun : Segitiga Lancip")
               print (f"   Luas        : {hitung_luas}")
               print (f"   Keliling    : {hitung_keliling}")
        elif bangun_datar == "3" :
            d1 = float (input ("Masukkan nilai sisi diagonal 1 : "))
            d2 = float (input ("Masukkan nilai sisi diagonal 2 : "))
            luas = (d1 * d2) / 2
            panjang = float (input ("Masukkan nilai panjang : "))
            lebar = float (input ("Masukkan nilai lebar : "))
            keliling = (2 * panjang) + (2 * lebar)
            print ("\nAnda memilih bangun datar")
            print ("   Nama Bangun : Layang-layang")
            print (f"   Luas        : {luas}")
            print (f"   Keliling    : {keliling}")
        else :
            print("Data tidak valid")

    elif list == "B" :
        print (""" 1. kubus
 2. tabung
 3. limas (segi empat, segi lima, segi enam)""")
        bangun_ruang = (input("Masukkan pilihan bangun ruang (1-3) : "))
        if bangun_ruang == '1':
            print ("\n---Hitung Luas Permukaan & Volume Kubus---")
            s = float(input("Masukkan panjang sisi kubus : "))
            luas = 6 * s**2
            volume = s**3
            print ("\nAnda memilih bangun ruang")
            print ("   Nama Bangun    : Kubus")
            print (f"   Luas Permukaan : {luas}")
            print (f"   Volume Bangun  : {volume}")
        elif bangun_ruang =='2':
            print("\n---Hitung Luas Permukaan & Volume Tabung---")
            r = float(input("Masukkan jari-jari tabung : "))
            t = float (input("Masukkan Tinggi Tabung : "))
            luas = 2 * math.pi * r * (r + t)
            volume = math.pi * r**2 * t
            print ("\nAnda memilih bangun ruang")
            print ("   Nama Bangun    : Tabung")
            print (f"   Luas Permukaan : {luas}")
            print (f"   Volume Bangun  : {volume}")
        elif bangun_ruang == '3':
            print ("""\n a. segi empat
 b. segi lima
 c. segi enam""")
            limas = input ("\nmasukkan pilihan Limas (gunakan huruf a-c) : ")
            if limas =='a':
                a = float (input("Masukkan panjang sisi alas : "))
                t = float (input("Masukkan tinggi limas : "))
                luas_alas = a**2
                tinggi = math.sqrt((a / 2)**2 + t**2)
                luas_permukaan = luas_alas + 2 * a * tinggi
                volume = (1 / 3) * a**2 * t
                print ("\nAnda memilih bangun ruang")
                print ("   Nama Bangun    : Limas Segi Empat")
                print (f"   Luas Permukaan : {luas_permukaan}")
                print (f"   Volume Bangun  : {volume}")
            elif limas =='b':
                a = float (input("Masukkan panjang sisi alas : "))
                t = float (input("Masukkan tinggi limas : "))
                luas_alas = (5 / 4) * a**2 / math.tan(math.pi / 5)
                tinggi = math.sqrt((a / 2)**2 + t**2)
                luas_permukaan = luas_alas + 5 * (0.5 * a * tinggi)
                volume = (1 / 3) * luas_alas * t
                print ("\nAnda memilih bangun ruang")
                print ("   Nama Bangun    : Limas Segi Lima")
                print (f"   Luas Permukaan : {luas_permukaan}")
                print (f"   Volume Bangun  : {volume}")
            elif limas =='c':
                a = float (input("Masukkan panjang sisi alas : "))
                t = float (input("Masukkan tinggi limas : "))
                luas_alas = (3 * math.sqrt(3) / 2) * a**2
                tinggi = math.sqrt((a / 2)**2 + t**2)
                luas_permukaan = luas_alas + 6 * (0.5 * a * tinggi)
                volume = (1 / 3) * luas_alas * t
                print ("\nAnda memilih bangun ruang")
                print ("   Nama Bangun    : Limas Segi Enam")
                print (f"   Luas Permukaan : {luas_permukaan}")
                print (f"   Volume Bangun  : {volume}")
            else :
                print ("data tidak valid")
        else :
            print ("data tidak valid")
    else :
        print ("data tidak valid")
    list = input("kembali menghitung(y/n) : ") 
    if list.lower()=='n':
            break