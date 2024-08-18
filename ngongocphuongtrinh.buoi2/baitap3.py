# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:41:12 2024

@author: PTRINH
"""

# Bai tap tam giac
a = float(input("Nhap so thuc a:"))
b = float(input("Nhap so thuc b:"))
c = float(input("Nhap so thuc c:"))
if a+b>c and a+c>b and b+c>a:
        # tam giac deu
        if a == b ==c:
            print("a,b,c la 3 canh cua tam giac va la tam giac deu.")
        # tam giac can
        elif a == b or b == c or c == a:
            print("a,b,c la 3 canh cua tam giac va la tam giac can.")
        # tam giac vuong
        elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print("a,b,c la 3 canh cua tam giac va do la tam giac vuong.")
        else:
            print("a,b,c la 3 canh cua tam giac.")
else:
    print("a,b,c khong phai 3 canh cua tam giac.")
    