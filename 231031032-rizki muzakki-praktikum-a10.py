def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Program Utama
input_nilai = int(input('Masukkan sebuah nilai: '))

if input_nilai < 0:
    print('Tidak ada faktorial untuk nilai negatif.')
else:
    print(f'Output untuk nilai {input_nilai}:')
    for i in range(input_nilai + 1):
        print(f'{i:2}! = {faktorial(i)}')
