# CXQ966_Project
# Bogárhátú Autó Értékbecslő és Archívum (Projektfeladat)

## Hallgatói adatok
- **Név:** Kardos István Gergő
- **Neptun-kód:** CXQ966 

---

## Feladat leírása
A program egy Python Tkinter alapú grafikus alkalmazás, amellyel klasszikus Volkswagen Bogár (VW Beetle) modellek adatait, technikai specifikációit és becsült gyűjtői piaci értékét lehet nyilvántartani és kiszámítani. A szoftver kiszámítja a jármű pontos korát az aktuális év alapján, figyelembe veszi annak állapotát (pajta lelet, megkímélt gyári, OT-restaurált), és az ezekből származó szorzók alapján ad becsült piaci árat.

---

## Felhasználói leírás

### Szükséges környezet és modulok:
- Python 3.8+ értelmező
- Beépített modulok (külön telepítést nem igényelnek): tkinter, datetime

### Használat és indítás:
1. Nyiss egy terminált / parancssort a projekt mappájában.
2. Indítsd el a főprogramot a következő paranccsal:
   python main.py
3. A megnyíló grafikus ablakban:
   - Válaszd ki a kívánt VW Bogár modellt a legördülő menüből.
   - Válaszd ki az autó állapotát.
   - Kattints az Értékbecslés és Specifikáció gombra az egyedi adatok megjelenítéséhez.
   - Kattints a Teljes Gyűjteményi Statisztika gombra az adatbázisban szereplő összes autó együttes értékének és a legrégebbi gépnek a lekérdezéséhez.

---

## Felépítés

### Modulok:
1. main.py: A program belépési pontja, tartalmazza a Tkinter grafikus felületet és az eseménykezelő függvényeket.
2. bogar_modul_XY.py: Saját logikai modul (A fájlnévben az XY helyére a saját monogramodat írd!).

### Osztályok:
- BogarAuto_XY: A járműveket reprezentáló saját osztály.
  - becsult_ertek_szamitas_XY(): Kiszámítja az autó becsült piaci értékét a kor és az állapot alapján.
  - kor_kiszamitas_XY(aktualis_ev): Megadja az autó életkorát években.
  - specifikacio_lekerdezes_XY(): Összeállítja a jármű modell- és motoradatait.

### Modul függvények (bogar_modul_XY.py):
1. adatbazis_betoltes_XY(): Visszaadja a gyári tesztadatok listáját.
2. legregebbi_bogar_kereses_XY(bogar_lista): Kiválasztja a listában szereplő legidősebb autó objektumot.
3. gyujtemeny_osszertek_XY(bogar_lista): Kiszámolja a teljes gyűjtemény becsült összegét.
