import os
os.system('clear')


nim=['2','3','1','0','3','1','0','3','2']
nim2='231031032'

print(nim[1:3])
print(nim2[1:3])

print(f'item indeks 0:{nim[0]}')
print(f'item indeks 4:{nim[4]}')


print(f'item indeks terakhir:{nim[len(nim)-1]}')
print(f'item indeks pertama:{nim[-len(nim)]}')
print(f'item indeks 6:{nim[-3]}')
print(f'item indeks 4:{nim[-5]}')
print(f'item indeks 7:{nim[-2]}')
print()

print(f'item indeks 1,2,.....:\n{nim[1:2]}')
print(f'item indeks 3,4,.....:\n{nim[3:]}')
print(f'item indeks 0,1,2:\n{nim[:3]}')
print(f'item indeks 0,1,2:\n{nim[:3]}')
print(f'item indeks 0,1,2,3:\n{nim[:4]}')
print(f'item indeks semua:\n{nim[:]}')
print(f'item indeks [:8]:\n{nim[:-1]}')
print(f'item indeks [:6]:\n{nim[:-3]}')
print()

print(f'item indeks 1,2 : \n {nim[1:3]}')
print(f'item indeks 2,3,4 : \n {nim[2:5]}')
print(f'item indeks kosong : \n {nim[3:3]}')
print(f'item indeks [8:8]kosong : \n {nim[-1:--1]}')
print(f'item indeks [1:8] : \n {nim[1:-1]}')
print(f'item indeks [2,7] : \n {nim[2:-2]}')
print()

data=['Nama Rizki Muzakki',2023, 'aktif']
nilai=[90,89,93,97]

print(f'{data[0]} status kuliah: {data[2]}')
print(f'Data terbesar nilai adalah : {max(nilai)}')
print(f'Data Terkecil adalah: {min(nilai)}')
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}')
print()

data=('Nama Rizki Muzakki',2023, 'aktif')
nilai=[90,89,93,97]
print(f'jumlah  nilai mahasiswa adalah: {len(nilai)}') 
print(f'Data terbesar nilai adalah : {max(nilai)}')
print(f'Data Terkecil adalah: {min(nilai)}')
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}')
print()

data=[['Rizki Muzakki',2023,'aktif'],
[90,89,93,97],
[20,22],
['s1-reguler','ganjil']]

print(f'Program pendidikan Rizki Muzakki: {data[3][0]}')
print(f'Angkatan :{data[0][1]} ')
print(f'Jumlah nilai Rizki Muzakki: {len(data[1])}')
print(f'Data Terbesar Rizki Muzakki: {max(data[1])}')
print(f'Data Terkecil Rizki Muzakki: {min(data[1])}')
print(f'Rata-rata Nilai RIzki Muzakki Adalah: {sum(data[1])/ len(data[1])} ')
print()

data=[['Rizki Muzakki','2023','Aktif'],
[90,89,93,97],
[20,22],
['S1-Reguler','Ganjil']]
matkul=['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan CINTA Iptek dan Imtaq']
sks=[2,2,2,2]

#tambahkan matkul dan sks kedalalam data(di akhir)
data.append(matkul)
data.append(sks)

#matkul 1
print(f'Mata Kuliah {data[4][0]} dengan jumlah {data[-1][0]} sks')
#matkul 2
print(f'Mata Kuliah {data[4][1]} dengan jumlah {data[-1][1]} sks')
#matkul 3
print(f'Mata Kuliah {data[4][2]} dengan jumlah {data[-1][2]} sks')
#matkul 4
print(f'Mata Kuliah {data[4][3]} dengan jumlah {data[-1][3]} sks')

data[4].append('Pengantar Pemrograman')
data[5].append(3)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)
# Matkul 6
print(f'Mata Kuliah {data[4][4]} dengan jumlah {data[-1][4]} sks')
# Matkul 7
print(f'Mata Kuliah {data[4][5]} dengan jumlah {data[-1][4]} sks')
# Matkul 8
print(f'Mata Kuliah {data[4][6]} dengan jumlah {data[-1][6]} sks')

# Tambahkan 8 nilai masing-masing
data[1].append(98)
data[1].append(96)
data[1].append(90)
data[1].append(91)
print(data[0][0])
print(data[3][0])
print(data[2][0:])
# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
print(f'Nama Mahasiswa {data[0][0]} dengan NIM {"".join(nim)}')
# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
print(f'Nama Mahasiswa {data[0][0]}')
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]} {data[-1][1]}')
# >> Jumlah nilai Thomas adalah: 8
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
# >> Data terbesar Thomas adalah: 98
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
# >> Data terkecil Thomas adalah: 90
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
# >> Rata-rata nilai Thomas adalah: 94.625
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/(len(data[1]))}')