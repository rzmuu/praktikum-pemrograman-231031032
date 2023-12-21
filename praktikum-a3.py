nama= 'rizki muzakki'
nim= '231031032'
meet='praktikum 3'
prodi= 'sistem informasi A'
email='rizkimuzakki03@gmail.com'
ttl='Sengkang, 03 Desember 2004'
alamat= 'jl. Bumi Harapan'
asal= 'Kota Sengkang, Kabupaten wajo'
hobi='Lari'
tinggi='166'

print('-'*40)
print(nama.center(40).upper())
print(nim.center(40))
print('\n'*2)
print(meet.capitalize().rjust(40))
print(prodi.title().rjust(40))
print(email.rjust(40))
print('-'*40)

print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima Kasih.\n
Biodata saya,
Nama\t: {nama.title()}
NIM\t: {nim}
Prodi\t: {prodi.title()}
TTl\t: {ttl.title()}
Alamat\t: {alamat.title()}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}cm''') 

stat= 'sir issac newton'
up=stat.upper()
up=up.split()
print(up)

print(up[2],up[0][0],up[0][1])



