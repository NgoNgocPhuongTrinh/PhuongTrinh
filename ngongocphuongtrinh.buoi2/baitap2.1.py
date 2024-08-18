# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:17:27 2024

@author: PTRINH
"""
import math
# Giai phuong trinh bac 2
a = float(input("Nhap so thuc a:"))
b = float(input("Nhap so thuc b:"))
c = float(input("Nhap so thuc c:"))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        print("Phuong trinh vo nghiem")
    print("Phuong trinh co 1 nghiem")
else:
    delta=b**2-4*a*c
if delta == 0 :
    print("vay phuong trinh co nghiem kep la" , -b/(2*a) )
elif delta > 0:
    print("vay phuong trinh co 2 nghiem phan biet la:" , (-b+ math.sqrt(delta))/(2*a) , "va" , (-b- math.sqrt(delta))/(2*a) )    
else:
    print("vay phuong trinh vo nghiem")