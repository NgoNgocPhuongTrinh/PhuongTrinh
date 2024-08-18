# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:43:49 2024

@author: PTRINH
"""

GPA = float(input("Nhap diem trung binh (GPA):"))
if GPA < 3.5 :
    print("Hoc luc kem")
elif GPA >=3.5 and GPA < 5.0 :
    print("Hoc luc yeu")
elif GPA >= 5.0 and GPA < 7.0:
    print("Hoc luc trung binh")
elif GPA >= 7.0 and GPA < 8.0:
    print("Hoc luc kha")
elif GPA >= 8.0 and GPA < 9.0:
    print("Hoc luc gioi")
elif GPA >= 9.0 and GPA <= 10:
    print("Hoc luc xuat sac")
else:
    print("Khong xac dinh")