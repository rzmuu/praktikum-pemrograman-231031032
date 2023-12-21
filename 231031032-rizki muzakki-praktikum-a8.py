def cek_password():
    password1 = "qwe"
    password2 = "rty"
    password3 = "uio"

    input_password1 = input("Masukkan password pertama: ")
    if input_password1 == password1:
        print("Password pertama benar!")
    else:
        print("Password salah. Akses ditolak.")
        return

    input_password2 = input("Masukkan password kedua: ")
    if input_password2 == password2:
        print("Password kedua benar!")
    else:
        print("Password salah. Akses ditolak.")
        return

    input_password3 = input("Masukkan password ketiga: ")
    if input_password3 == password3:
        print("Password ketiga benar!")
    else:
        print("Password salah. Akses ditolak.")
        return

    print("Selamat! Semua password benar. Akses diberikan.")

if __name__ == "__main__":
    cek_password()
