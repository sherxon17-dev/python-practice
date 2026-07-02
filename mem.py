import random
import time

memlar = [
    "👨‍💻 Dasturchi: 'Bugni topdim!' → 5 soatdan keyin: 'yo‘q, hali ham yo‘q 😂'",
    "😴 Code yozdim → Run qildim → Kompyuter: 'Men dam olyapman' 💀",
    "🐍 Python: 'oson til' deyishgan edi... endi yig‘layapman 🤯",
    "📱 Telefon: 2% battery → Dasturchi: 'yana 10 daqiqa ishlayman' 😭",
    "💻 Bug topdim → tuzatdim → yangi bug paydo bo‘ldi 🔁",
    "👀 Dasturchi 1 soat kod qidirdi → muammo: bitta nuqta yo‘q 😂"
]

print("😂 QIZIQARLI MEM GENERATORGA XUSH KELIBSIZ 😂")
print("CTRL + C bilan chiqasiz\n")

while True:
    input("ENTER bosing mem ko‘rish uchun...")
    print("\n", random.choice(memlar))
    time.sleep(1)
