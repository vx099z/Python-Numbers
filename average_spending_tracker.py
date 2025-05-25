from num2words import num2words

# Foydalanuvchidan 7 ta xarajatni olish
qiymatlar = input("15.0, 10.0, 13.0, 12.5, 11.0, 14.0,): ")

# Floatga aylantirib o‘rtachasini hisoblash
qiymatlar = [float(q.strip()) for q in qiymatlar]
orta = sum(qiymatlar) / len(qiymatlar)
orta = round(orta, 2)

# So'z bilan ifoda qilish (EN va RU)
soz_en = num2words(orta, to='currency', lang='en')
soz_ru = num2words(orta, to='currency', lang='ru')

# Natijani chiqarish
print(f"O‘rtacha xarajat: ${orta} ({soz_en}, {soz_ru})")