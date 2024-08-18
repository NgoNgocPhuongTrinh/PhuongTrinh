# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:46:41 2024

@author: Student
"""

a = float(input("Tien taxi theo so km quang duong di duoc (km):"))
if a <= 1:
    sotien = 20
    print("Tong tien:", sotien)
elif a <= a*13:
    print("Tong tien:" , sotien )
elif a >= 4 and a <= 8:
    sotien= 3*13+(a-3)*12
    print("Tong tien:" , sotien)
else: 
    sotien =3*13+8*12+10*(a-8)
if sotien > 100:
    print("Tong tien:", sotien*0.92)
else:
    print("Tong tien:",3*13+8*12+10*(a-8) )