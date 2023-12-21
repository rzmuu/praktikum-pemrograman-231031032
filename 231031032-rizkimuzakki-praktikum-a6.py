a=True    #variabel dengan nilai True

while a:   #memulai perulangan while yang akan terus berjalan selama nilai a=True
    pilih= input('pilihan:')  # Meminta pengguna untuk memasukkan input dan menyimpannya dalam variabel pilih. Input ini akan digunakan untuk menentukan jalannya program.
    if pilih == 'ya':  #Melakukan pengecekan apakah input yang dimasukkan oleh pengguna adalah string 'ya'.
        print('Selamat datang')  # Program akan mencetak "Selamat datang".
    elif pilih== 'tidak':  #Jika input tidak sama dengan 'ya', maka dilakukan pengecekan apakah input tersebut adalah string 'tidak
        print('sampai jumpa')  #program akan mencetak 'sampai jumpa'
    
    
    


a=True    #variabel dengan nilai True

while a:   #memulai perulangan while yang akan terus berjalan selama nilai a=True
    pilih= input('pilihan:')   # Meminta pengguna untuk memasukkan input dan menyimpannya dalam variabel pilih. Input ini akan digunakan untuk menentukan jalannya program.
    if pilih == 'ya':  #Melakukan pengecekan apakah input yang dimasukkan oleh pengguna adalah string 'ya'.
        print('Selamat datang')  # Program akan mencetak "Selamat datang".
        a=False #membuat nilai a menjadi False yang akan membuat perulangan while berhenti
    elif pilih== 'tidak':  #Jika input tidak sama dengan 'ya', maka dilakukan pengecekan apakah input tersebut adalah string 'tidak
        print('sampai jumpa')  #program akan mencetak 'sampai jumpa'
        a=False  #membuat nilai a menjadi False yang akan membuat perulangan while berhenti
    else: # Baris ini dieksekusi jika kondisi dalam pernyataan if tidak terpenuhi
        continue   #melanjutkan terus program