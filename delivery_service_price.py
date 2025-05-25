from num2words import num2words

# Foydalanuvchidan masofani olish
masofa = float(input("3.5): ")

# Narxni hisoblash
boshlangich_tolov = 5.00
har_km_narx = 0.80
narx = boshlangich_tolov + masofa * har_km_narx
narx = round(narx, 2)

# So'z bilan ifoda qilish
soz_en = num2words(narx, to='currency', lang='en')
soz_ru = num2words(narx, to='currency', lang='ru')

# Natijani chiqarish
print(f"Yetkazib berish narxi: ${narx} ({soz_en}, {soz_ru})")