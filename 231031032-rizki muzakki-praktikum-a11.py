#Fungsi Rekursif Fibonacci
def fibonacci(n):
     if n<0:
         print('Tidak ada bilangan yang bernilai negatif')
     if n==0 or n==1:
        return n
     else:
       return fibonacci(n-1) + fibonacci(n-2)

#Program Utama
nilai=int(input('Masukkan sebuah bilangan:'))
hasil=fibonacci(nilai)
print('Fibobacci(%d)=%d' % (nilai,hasil))