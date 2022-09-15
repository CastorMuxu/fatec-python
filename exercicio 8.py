# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:23:22 2022

@author: anama
"""

temp = int(input("Digite a temperatura: "))

umidade = int(input("Digite a umidade relativa do ar: "))

if temp >= 28 and umidade >= 50:
    print("Irá chover amanhã")
else:
    print("Amanhã o dia será sem chuvas")             