print('praktikum-a2\n\n')

print('NAMA   : RIZKI MUZAKKI')
print('NIM    : 231031032')
print('Prodi  : Sistem Informasi A\n')

# INI OPERATOR ASSIGNMENT
a=19
print('nilai a adalah',a)
a +=3
print('nilai a+=3 adalah',a)

a=19
print('nilai a adalah',a)
a -=3
print('nilai a-=3 adalah',a)

a=19
print('nilai a adalah',a)
a *=2
print('nilai a*=2 adalah',a)

a=19
print('nilai a adalah',a)
a /=2
print('nilai a/=2 adalah',a)

a=3
print('nilai a adalah',a)
a **=2
print('nilai a**=2 adalah',a)

a=35
print('nilai a adalah',a)
a %=32
print('nilai a%=32 adalah',a)

a=35
print('nilai a adalah',a)
a //=32
print('nilai a//=32 adalah',a)

# Tugas melanjutkan untuk operator selanjutnya line 25-line 59
# OR
b=True
print('Nilai b =',b)
b |=False
print('nilai b|=false akan menjadi',b)
b=False
print('nilai b=',b)
b|=False
print('nilai b|=false akan menjadi',b)

# AND
b=True
print('nilai b=',b)
b&=False
print('nilai b&=false akan menjadi',b)
b=False
print('nilai b=',b)
b&=False
print('nilai b&=false akan menjadi',b)

#XOR
b=True
print('nilai b=',b)
b^=False
print('nilai b^=false akan menjadi',b)
b=False
print('niali b=',b)
b^=False
print('nilai b^=false akan menjadi',b)

#Shifting
c=0b0100
print('nilai c=',format(c, '04b'))
c>>=1
print('nilai c >>=1 akan menjadi',format(c, '04b'))
c=0b0100
c<<=1
print('nilai c <<=1 akan menjadi',format(c, '04b'))


# operator perbandingan
a=9
b=13
print('\n-------- Besar dari 32')
hasil= a>32
print(a,'> 32 adalah',hasil)
hasil= b>32
print(b,'> 32 adalah',hasil)

print('\n-------- kecil dari 32')
hasil= a<32
print(a,'< 32 adalah',hasil)
hasil= b<32
print(b,'< 32 adalah',hasil)

print('\n-------- Besar atau sama dari 32 ')
hasil= a>=32
print(a,'>= 32 adalah',hasil)
hasil= b>=32
print(b,'>= 32 adalah',hasil)

print('\n-------- Kecil atau sama dari 32 ')
hasil = a<= 32
print(a,'<= 32 adalah',hasil)
hasil = b<=32
print(b,'<= 32 adalah',hasil)

print('\n-------- Sama dari 32 ')
hasil = a== 32
print(a,'== 32 adalah',hasil)
hasil = b==32
print(b,'== 32 adalah',hasil)

print('\n-------- Tidak sama dari 32 ')
hasil = a!= 32
print(a,'!= 32 adalah',hasil)
hasil = b!=32
print(b,'!= 32 adalah',hasil)


#operator logika
a=True
b=False
print('\n=======AND=======')

hasil= a and a
print(a,'and',a,'hasilnya=',hasil)

hasil= a and b
print(a,'and',b,'hasilnya=',hasil)

hasil= b and a
print(b,'and',a,'hasilnya=',hasil)

hasil= b and b
print(b,'and',b,'hasilnya=',hasil)

print('\n=======OR=======')
hasil= a or a
print(a,'or',a,'hasilnya=',hasil)

hasil= a or b
print(a,'or',b,'hasilnya=',hasil)

hasil= b or a
print(b,'or',a,'hasilnya=',hasil)

hasil= b or b
print(b,'or',b,'hasilnya=',hasil)

print('\n=======XOR=======')

hasil= a ^ a
print(a,'xor',a,'hasilnya=',hasil)

hasil= a ^ b
print(a,'xor',b,'hasilnya=',hasil)

hasil= b ^ a
print(b,'xor',a,'hasilnya=',hasil)

hasil= b ^ b
print(b,'xor',b,'hasilnya=',hasil)

print('\n=======NOT=======')

hasil= not a
print('not',a,'hasilnya=',hasil)
hasil= not b
print('not',b,'hasilnya=',hasil)

# Operator membership
print('\n================IN')
nama= 'Rizki Muzakki'
test= 'Ri'
cek= test in nama 
print(test,'terdapat di nama',nama,'adalah',cek)

test= 'Ri'
cek= test in nama 
print(test,'terdapat di nama',nama,'adalah',cek)
print()
test1= 'a'
test2= 'i'
test3= 'u'
test4= 'e'
test5= 'o'

cek= test1 in nama 
print(test1,'terdapat di',nama,'adalah',cek)

cek= test2 in nama 
print(test2,'terdapat di',nama,'adalah',cek)

cek= test3 in nama 
print(test3,'terdapat di',nama,'adalah',cek)

cek= test4 in nama 
print(test4,'terdapat di',nama,'adalah',cek)

cek= test5 in nama 
print(test5,'terdapat di',nama,'adalah',cek)

print('\n================ NOT IN')
nama= 'Rizki Muzakki'
test= 'Ri'
cek= test not in nama 
print(test,'tidak terdapat di nama',nama,'adalah',cek)

test= 'Ri'
cek= test not in nama 
print(test,'tidak terdapat di nama',nama,'adalah',cek)
print()
test1= 'a'
test2= 'i'
test3= 'u'
test4= 'e'
test5= 'o'

cek= test1 not in nama 
print(test1,'tidak terdapat di',nama,'adalah',cek)

cek= test2 not in nama 
print(test2,'tidak terdapat di',nama,'adalah',cek)

cek= test3 not in nama 
print(test3,'tidak terdapat di',nama,'adalah',cek)

cek= test4 not in nama 
print(test4,'tidak terdapat di',nama,'adalah',cek)

cek= test5 not in nama 
print(test5,'tidak terdapat di',nama,'adalah',cek)

