a= True  #merupakan variabel dengan nilai True
while a:   #memulai perulangan while yang akan terus berjalan selama nilai a=True
    print('menjalankan program')   # Mencetak teks "menjalankan program"


a= True  #merupakan variabel dengan nilai True
perulangan= 0 #merupakan variabel dengan nilai =0
while a:   #memulai perulangan while yang akan terus berjalan selama nilai a=True
    if perulangan >= 5 :    #Baris ini memeriksa apakah nilai perulangan lebih besar dari atau sama dengan 5
        print('Program selesai')   #Baris ini mencetak string "Program selesai"
        a=False  #membuat nilai a menjadi False yang akan membuat perulangan while berhenti
    else:   # Baris ini dieksekusi jika kondisi dalam pernyataan if tidak terpenuhi
        perulangan +=1   #Baris ini menambahkan nilai perulangan sebesar 1
        print('Menjalankan program sebanyak ',perulangan,'kali')   #Baris ini mencetak string "Menjalankan program sebanyak ", diikuti oleh nilai perulangan, diikuti oleh string "kali"



       