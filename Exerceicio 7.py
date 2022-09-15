# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:39:15 2022

@author: anama
"""

arroz = 5
feijao = 3
acucar = 2
batata = 3
oleo = 5
bolacha_agua_sal = 1
maizena = 1
banana = 18
couve_flor = 2
leite_em_po = 2

varroz = float(input("Digite o valor do kg do arroz: "))
vfeijao = float(input("Digite o valor do kg de feijao: "))
vacucar = float(input("Digite o valor do kg do açúcar: "))
vbatata = float(input("Digite o valor do kg da batata: "))
voleo = float(input("Digite o valor do litro de óleo: "))
vbolacha = float(input("Digite o valor do pacote de bolacha de água e sal: "))
vmaizena = float(input("Digite o valor do pacote de maizena: "))
vcouve = float(input("Digite o valor do maço de couve flor: "))
vleite = float(input("Digite o valor da lata de leite em pó: "))

print(" ")

print("O valor dos produtos são")

print("O valor do KG  de arroz é de: ", varroz)
print("O valor do KG do feijão é de: ", vfeijao)
print("O valor  do KG do açúcar é de: ", vacucar)
print("O valor do KG da batata é de: ", vbatata)
print("O valor do litro de óleo é de: ", voleo)
print("O valor do pacote de bolacha de água e sal é de: ", vbolacha)
print("O valor do pacote de maizena é de: " , vmaizena)
print("O valor do maço de couve-flor é de: " , vcouve)
print("O valor da late de leite em pó é de: ", vleite)
print("O preço dos produtos são")

parroz = varroz * arroz
pfeijao = vfeijao * feijao
pacucar = vacucar * acucar
pbatata = vbatata * batata
poleo = voleo * oleo
pbolacha = vbolacha * bolacha_agua_sal
pmaizena = vmaizena * maizena
pcouve = vcouve * couve_flor
pleite = vleite * leite_em_po

print("O preço de 5kg de arroz é de: ", parroz)
print("O preço de 3kg de feijão é de: ", pfeijao)
print("O preço de 2kg de açúcar é de: ", pacucar)
print("O preço de 3kg de batata é de: ", pbatata)
print("O preço de 4 litros de óleo é de: ", poleo)
print("O preço do pacote de bolacha água e sal é de: ", pbolacha)
print("O preço do pacote de maizena é de: ", pmaizena)
print("O preço de dois maçoes de couve-flor é de: ", pcouve)
print("O preço de 2 latas de 1kg de leite em pó é de: ", pleite)

vtotal = parroz + pfeijao + pacucar + pbatata + poleo + pbolacha + pmaizena + pcouve + pleite

print("O valor total da compra foi de: R$ ", vtotal)

print("Recomendado gastar R$ 200.00 ")
      