print('praktikum-1')
print('Nama Lengkap: Rizki Muzakki')
print('NIM         : 231031032')
print('Prodi       : Sistem informasi')
print()
x=2023
print('Angkatan',x)

print()
a=10
print('data adalah: ',a)
print('Tipe data a adalah',type(a))
print()

b=10.0
print('data adalah: ',b)
print('Tipe data b adalah',type(b))

print()
kampus='Institut Teknologi BJ Habibie'
print('data adalah:',kampus)
print('tipe data adalah',type(kampus))

print()
c=complex(2, 3)
print('data adalah:',c)
print('tipe data adalah',type(c))

print()
log=True
print('data adalah:',log)
print('tipe data adalah',type(log))

print()
p=20
q=23
hasil= p+q
print('hasil ',p,'+',q,'=',hasil)
print()
print()
print('ini adalah batas untuk tugas praktikum####')
print()
print('Tugas Praktikum')
y=12
z=12
#penjumlahan
hasil=y+z
print('hasil',y,"+",z,'=',hasil)
print()
#pengurangan
hasil=y-z
print('hasil',y,"-",z,'=',hasil)
print()
#perkalian
hasil=y*z
print('hasil',y,"*",z,'=',hasil)
print()
#pembagian
hasil=y/z
print('hasil',y,"/",z,'=',hasil)
print()
#modulus
hasil=y%z
print('hasil',y,"%",z,'=',hasil)
print()
#eksponen
hasil=y**z
print('hasil',y,"**",z,'=',hasil)
print()
#floordivision
hasil=y//z
print('hasil',y,"//",z,'=',hasil)



str1 = 'duFort Frankel Von Neumann'
up=str1.upper().split()
print(up[-1]," ".join(up[0:3]))
#output: NEUMANN DUFORT FRANKEL VON
print()

str2 = 'duFort Frankel Von Neumann'
up2=str2.upper().split()
print(f'{up2[0][0]}{up2[1][0]}{up2[2][0]} {up2[3]}')
#output: DFV NEUMANN
print()

str3 = 'duFort Frankel Von Neumann'
up3=str3.upper().split()
print(f'{up3[0]} {up3[0][2]}{up3[2][0]}{up3[1][3]}')
#output: DUFORT FVN
print()


str4 = 'duFort Frankel Von Neumann'
up4=str4.split()
print(f'{up4[3][0]} {up4[0]} {up4[1][0]}{up4[2][0]}')
#output: N duFort FV
print()

str5 = 'duFort Frankel Von Neumann'
up5=str5.split()
print(f'{up5[3].upper()} {up5[0][0]} {up5[1][0].lower()} {up5[2][0].lower()}')
#output: NEUMANN d f v
print()

str6 = 'duFort Frankel Von Neumann'
up6=str6.upper().split()
print(f'{up6[3]} {up6[0][0]}{up6[1][0]}{up6[2][0]}')
#output: NEUMANN DFV
print()

str7 = '@duFort Frankel Von Neumann$'
up7=str7.split()
print(f'{up7[0].strip("@")} {up7[1]} {up7[2]} {up7[3].upper().strip("$")}')
#output: duFort Frankel Von NEUMANN
print()

str8 = '#duFort4Frankel4Von4Neumann$'
up8=str8.split("4")
print(f'{up8[0].strip("#")} {up8[1]} {up8[2]} {up8[3].strip("$")}')
#output: duFort Frankel Von Neumann