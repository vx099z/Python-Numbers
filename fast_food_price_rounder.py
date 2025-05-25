#foydalanuvchudan narxlar
narxlar = input(4.5, 3.2, 5,5 )


#Sonlarga aylantirib jamlash
narxlar = [float(n.strip()) for n in narxlar]
umumiy = sum(narxlar)

# 0.1 ga yaxlitlash
yaxlit = round(umumiy * 10) / 10


# Natija
print("Umumiy narx:", umumiy)
print("yaxlitlangan narx:, ")