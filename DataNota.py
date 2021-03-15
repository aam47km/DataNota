import csv 
import os 
import datetime

tanggal= datetime.date.today() 

datafile = "Transaksi.csv"

def menu(): 
    print('''
      TOKO MAJU MUNDUR BERSAMA
    jl. Rimpis, Sumbersari, Srono
    =============================
    ''')

    print('''
    PILIHAN MENU :
    1. Tampilkan Data Transaksi
    2. Tambahkan Data Transaksi
    3. Hapus Data Transaksi
    4. Tutup
    ''')
    
    pilihan=int(input('Masukkan menu pilihan anda (1/2/3/4): '))
    
    if pilihan==1:
        tampilkanData()
        
    elif pilihan==2:
        tambahkanData()
        
    elif pilihan==3:
        hapusData() 
        
    elif pilihan==4:
        tutup() 
    else:
        print("Pilihan menu yang anda input !")
        menu()
       
def tutup(): 
    os.system('cls')
    
def kembali():
    menua()
    
def tampilkanData():
    tutup()
    item=[]
   
    with open(datafile,'r') as file:
        tampil= csv.reader(file,delimiter=";")
        for baris in tampil:
            item.append(baris)
        
        urutan= 1
        for data in item:
            print(urutan,"\t","\t".join(data))
            urutan+=1
            
    menu()
            
def tambahkanData():
    tutup()
    item=[]
    
    with open (panggilfile,'a',newline="") as file:
        namabarang=input('Nama Barang : ')
        jumlahbarang=int(input('Jumlah Barang : ')) 
        hargabarang= int(input('Harga Satuan : '))
        total=(jumlahbarang*hargabarang)
        
        unit=[tanggal, namabarang, jumlahbarang, hargabarang, total]
        
        tambah=csv.writer(file,delimiter=";")
        tambah.writerow(unit)
        
    menu()
    
def hapusData(): 
    tutup() 
    item=[] 
                  
    with open (datafile) as file:
        tampil= csv.reader(file,delimiter=";")
        for baris in tampil:
            item.append(baris)
        
        urutan= 1
        for data in item:
            print(urutan,"\t","\t".join(data))
            urutan+=1
            
    nomer=int(input('masukan nomer data yang akan dihapus: '))
    nomer -= 1
    
    del item[nomer]
        
    with open (datafile,'w',newline="")as file:
        tulis=csv.writer(file, delimiter=";")
        tulis.writerows(item)

    menu()             
menu()