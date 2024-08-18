# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:34:38 2024

@author: PTRINH
"""

distance=float(input("Nhap do dai doan duong den truong (m):"))
if distance < 300:
    print("Duong den truong qua gan. Thoi! di bo")
elif distance > 1200:
    print("Duong den truong xa qua. Thoi! Di xe may")
elif distance >= 300 and distance <=700:
    print("Duong den truong khong xa. Thoi! Di xe dap")
else:
    print("Khong xac dinh")