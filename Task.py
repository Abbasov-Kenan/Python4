import json, os

fayl = 'expenses.json'
xerc = []

if os.path.exists(fayl):
    with open(fayl, 'r') as f:
        xerc = json.load(f)

def saxla():
    with open(fayl, 'w') as f:
        json.dump(xerc, f)

while True:
    print("\n1. Əlavə\n2. Sil\n3. Yenilə\n4. Göstər\n5. Çıx")
    s = input("Seç: ")

    if s == '1':
        t = input("Ad: ")
        k = input("Kat: ")
        m = float(input("Məbləğ: "))
        xerc.append({'ad': t, 'kat': k, 'mebleg': m})
        saxla()
    elif s == '2':
        t = input("Ad: ")
        xerc = [i for i in xerc if i['ad'] != t]
        saxla()
    elif s == '3':
        t = input("Ad: ")
        m = float(input("Yeni məbləğ: "))
        for i in xerc:
            if i['ad'] == t:
                i['mebleg'] = m
        saxla()
    elif s == '4':
        for i in xerc:
            print(i)
    elif s == '5':
        break