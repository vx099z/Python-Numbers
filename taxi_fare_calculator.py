from num2words import num2words

# Foydalanuvchidan masofani olish
masofa = float(input("5.2"): ")

# Narxni hisoblash
boshlangich_tolov = $3.00
har_km_narx = 1.20
narx = boshlangich_tolov + masofa * har_km_narx
narx = round(narx, 2)

# So'z bilan ifoda qilish
soz_en = num2words(narx, to='currency', lang='en')
soz_ru = num2words(narx, to='currency', lang='ru')

# Natijani chiqarish
print(f"Taxi narxi: ${narx} ({soz_en}, {soz_ru})")