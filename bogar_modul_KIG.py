import datetime

class BogarAuto_KIG:
    def __init__(self, modell_nev, gyartasi_ev, eredeti_ar_huf, motor_type, allapot="Megkímélt gyári"):
        self.modell_nev = modell_nev
        self.gyartasi_ev = gyartasi_ev
        self.eredeti_ar_huf = eredeti_ar_huf
        self.motor_type = motor_type
        self.allapot = allapot

    def becsult_ertek_szamitas_KIG(self):
        szorzo = 1.0
        if self.allapot == "Pajta lelet / Felújítandó":
            szorzo = 0.45
        elif self.allapot == "Megkímélt gyári":
            szorzo = 1.2
        elif self.allapot == "OT-rendszámos / Restaurált":
            szorzo = 2.1

        kor_szorzo = 1.0 + (datetime.datetime.now().year - self.gyartasi_ev) * 0.03
        return round(self.eredeti_ar_huf * szorzo * kor_szorzo)

    def kor_kiszamitas_KIG(self, aktualis_ev):
        return aktualis_ev - self.gyartasi_ev

    def specifikacio_lekerdezes_KIG(self):
        return f"Modell: {self.modell_nev} | Évjárat: {self.gyartasi_ev} | Motor: {self.motor_type}"


def adatbazis_betoltes_KIG():
    return [
        {
            "modell": "VW Bogár 1100 Brezel (Perec)",
            "gyartasi_ev": 1951,
            "alapar": 2500000,
            "motor": "1.1L Boxer (25 LE)",
            "allapot": "OT-rendszámos / Restaurált"
        },
        {
            "modell": "VW Bogár 1200 Ovali",
            "gyartasi_ev": 1956,
            "alapar": 2000000,
            "motor": "1.2L Boxer (30 LE)",
            "allapot": "Megkímélt gyári"
        },
        {
            "modell": "VW Bogár 1300 Standard",
            "gyartasi_ev": 1967,
            "alapar": 1500000,
            "motor": "1.3L Boxer (40 LE)",
            "allapot": "Pajta lelet / Felújítandó"
        },
        {
            "modell": "VW Bogár 1303 Super Beetle",
            "gyartasi_ev": 1974,
            "alapar": 1800000,
            "motor": "1.6L Boxer (50 LE)",
            "allapot": "Megkímélt gyári"
        },
        {
            "modell": "VW Bogár 1303 Cabriolet",
            "gyartasi_ev": 1978,
            "alapar": 2800000,
            "motor": "1.6L Boxer (50 LE)",
            "allapot": "OT-rendszámos / Restaurált"
        }
    ]


def legregebbi_bogar_kereses_KIG(bogar_lista):
    legregebbi = bogar_lista[0]
    for auto in bogar_lista:
        if auto.gyartasi_ev < legregebbi.gyartasi_ev:
            legregebbi = auto
    return legregebbi


def gyujtemeny_osszertek_KIG(bogar_lista):
    osszeg = 0
    for auto in bogar_lista:
        osszeg += auto.becsult_ertek_szamitas_KIG()
    return osszeg