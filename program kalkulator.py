# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:22:26 2021

@author: user
"""

''' Program kalkulator sederhana untuk menjumlah, mengurang, mengali, dan membagi bilangan dengan menggunakan fungsi '''

# fungsi penjumlahan
def tambah(x, y):
   return x + y

# fungsi pengurangan
def kurang(x, y):
   return x - y

# fungsi perkalian
def kali(x, y):
   return x * y

# fungsi pembagian
def bagi(x, y):
   return x / y

# menu operasi
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# Meminta input dari user
pilihan = input("Masukkan pilihan(1/2/3/4): ")

num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

if pilihan == '1':
   print(num1,"+",num2,"=", tambah(num1,num2))

elif pilihan == '2':
   print(num1,"-",num2,"=", kurang(num1,num2))
   
elif pilihan == '3':
   print(num1,"*",num2,"=", kali(num1,num2))

elif pilihan == '4':
   print(num1,"/",num2,"=", bagi(num1,num2))
else:
   print("Input salah")