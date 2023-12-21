nama=input('Nama Karyawan:')
pendapatan=int(input('Pendapatan:'))

if pendapatan > 1000:
    print('Status:berhak')
elif pendapatan <= 1000:
    print('Status:Tidak Berhak')