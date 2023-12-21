passw= 'Hihi'
per=3
a=True
while a:
    masukkan=input('Masukkan Password:')
    if masukkan== passw:    
        print('selamat anda login')
        a=False
    else:
        print('Password anda salah, coba lagi sisa percobaan anda:',per)
        per -=1
        if per==0:
            print('password anda salah')
            print('Anda kehabisan kesempatan')
            a=False
