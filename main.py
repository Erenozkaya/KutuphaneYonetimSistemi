PYTHON
import sqlite3
from datetime import datetime

def connect():
    return sqlite3.connect("kutuphane.db")

# Kitap Ekle
def kitap_ekle():
    conn = connect()
    cur = conn.cursor()

    ad = input("Kitap Adı: ")
    yazar = input("Yazar: ")
    stok = int(input("Stok: "))

    cur.execute(
        "INSERT INTO books(title, author, stock) VALUES (?, ?, ?)",
        (ad, yazar, stok)
    )

    conn.commit()
    conn.close()
    print("Kitap başarıyla eklendi.")

# Kitapları Listele
def kitaplari_listele():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")

    for kitap in cur.fetchall():
        print(kitap)

    conn.close()

# Üye Ekle
def uye_ekle():
    conn = connect()
    cur = conn.cursor()

    isim = input("Üye Adı: ")
    telefon = input("Telefon: ")

    cur.execute(
        "INSERT INTO members(name, phone) VALUES (?, ?)",
        (isim, telefon)
    )

    conn.commit()
    conn.close()
    print("Üye başarıyla eklendi.")

# Kitap Ödünç Ver
def kitap_odunc_ver():
    conn = connect()
    cur = conn.cursor()

    kitap_id = int(input("Kitap ID: "))
    uye_id = int(input("Üye ID: "))

    cur.execute(
        "INSERT INTO loans(book_id, member_id, loan_date) VALUES (?, ?, ?)",
        (kitap_id, uye_id, datetime.now())
    )

    cur.execute(
        "UPDATE books SET stock = stock - 1 WHERE id=?",
        (kitap_id,)
    )

    conn.commit()
    conn.close()

    print("Kitap ödünç verildi.")

while True:
    print("\n=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")
    print("1- Kitap Ekle")
    print("2- Kitapları Listele")
    print("3- Üye Ekle")
    print("4- Kitap Ödünç Ver")
    print("5- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        kitap_ekle()

    elif secim == "2":
        kitaplari_listele()

    elif secim == "3":
        uye_ekle()

    elif secim == "4":
        kitap_odunc_ver()

    elif secim == "5":
        print("Program sonlandırıldı.")
        break

    else:
        print("Geçersiz seçim!")
