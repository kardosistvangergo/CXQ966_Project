import tkinter as tk
from tkinter import ttk
import datetime
import bogar_modul_KIG as bm

NEV = "Kardos István Gergő"
NEPTUN_KOD = "CXQ966"


class BogarApp:
    def __init__(self, gyoker):
        self.app = gyoker
        self.app.title("Bogárhátú Autó Értékbecslő és Archívum")
        self.app.geometry("520x600")
        self.app.resizable(False, False)

        self.adatok = bm.adatbazis_betoltes_KIG()
        self.auto_objektumok = []
        for elem in self.adatok:
            auto = bm.BogarAuto_KIG(
                elem["modell"],
                elem["gyartasi_ev"],
                elem["alapar"],
                elem["motor"],
                elem["allapot"]
            )
            self.auto_objektumok.append(auto)

        self.felulet_epites()

    def felulet_epites(self):
        cim_cimke = tk.Label(self.app, text="VW Bogár Értékbecslő", font=("Helvetica", 16, "bold"))
        cim_cimke.pack(pady=10)

        fejlec_info = tk.Label(self.app, text=f"Hallgató: {NEV} | Neptun Kód: {NEPTUN_KOD}",
                               font=("Helvetica", 9, "italic"))
        fejlec_info.pack(pady=2)

        keret_valasztas = tk.LabelFrame(self.app, text=" JÁRMŰ KIVÁLASZTÁSA ", padx=10, pady=10)
        keret_valasztas.pack(fill="x", padx=15, pady=10)

        tk.Label(keret_valasztas, text="Modell:").grid(row=0, column=0, sticky="w", pady=5)
        self.modell_var = tk.StringVar()
        modell_nevek = [a.modell_nev for a in self.auto_objektumok]
        self.modell_cb = ttk.Combobox(keret_valasztas, textvariable=self.modell_var, values=modell_nevek,
                                      state="readonly", width=35)
        self.modell_cb.grid(row=0, column=1, pady=5)
        self.modell_cb.current(0)

        tk.Label(keret_valasztas, text="Állapot:").grid(row=1, column=0, sticky="w", pady=5)
        self.allapot_var = tk.StringVar()
        allapotok = ["Pajta lelet / Felújítandó", "Megkímélt gyári", "OT-rendszámos / Restaurált"]
        self.allapot_cb = ttk.Combobox(keret_valasztas, textvariable=self.allapot_var, values=allapotok,
                                       state="readonly", width=35)
        self.allapot_cb.grid(row=1, column=1, pady=5)
        self.allapot_cb.current(1)

        gomb_kalkulal = tk.Button(self.app, text="Értékbecslés és Specifikáció", command=self.kalkulacio_esemeny_KIG,
                                  bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), height=2)
        gomb_kalkulal.pack(fill="x", padx=15, pady=5)

        gomb_statisztika = tk.Button(self.app, text="Teljes Gyűjteményi Statisztika",
                                     command=self.statisztika_esemeny_KIG, bg="#2196F3", fg="white",
                                     font=("Helvetica", 10, "bold"), height=2)
        gomb_statisztika.pack(fill="x", padx=15, pady=5)

        keret_eredmeny = tk.LabelFrame(self.app, text=" EREDMÉNYEK ÉS ADATOK ", padx=10, pady=10)
        keret_eredmeny.pack(fill="both", expand=True, padx=15, pady=10)

        self.eredmeny_text = tk.Text(keret_eredmeny, wrap="word", font=("Courier", 9))
        self.eredmeny_text.pack(fill="both", expand=True)

    def kalkulacio_esemeny_KIG(self):
        kivalasztott_nev = self.modell_var.get()
        kivalasztott_allapot = self.allapot_var.get()

        kivalasztott_auto = None
        for auto in self.auto_objektumok:
            if auto.modell_nev == kivalasztott_nev:
                kivalasztott_auto = auto
                break

        if kivalasztott_auto:
            kivalasztott_auto.allapot = kivalasztott_allapot
            aktualis_ev = datetime.datetime.now().year
            kor = kivalasztott_auto.kor_kiszamitas_KIG(aktualis_ev)
            becsult_ertek = kivalasztott_auto.becsult_ertek_szamitas_KIG()
            spec = kivalasztott_auto.specifikacio_lekerdezes_KIG()

            self.eredmeny_text.delete("1.0", tk.END)
            self.eredmeny_text.insert(tk.END, f"--- JÁRMŰ ADATLAP ---\n")
            self.eredmeny_text.insert(tk.END, f"{spec}\n")
            self.eredmeny_text.insert(tk.END, f"Kora: {kor} év\n")
            self.eredmeny_text.insert(tk.END, f"Kiválasztott állapot: {kivalasztott_allapot}\n")
            self.eredmeny_text.insert(tk.END, f"Becsült piaci érték: {becsult_ertek:,.0f} Ft\n".replace(",", " "))

    def statisztika_esemeny_KIG(self):
        osszertek = bm.gyujtemeny_osszertek_KIG(self.auto_objektumok)
        legregebbi = bm.legregebbi_bogar_kereses_KIG(self.auto_objektumok)

        self.eredmeny_text.delete("1.0", tk.END)
        self.eredmeny_text.insert(tk.END, f"=== GYŰJTEMÉNYI STATISZTIKA ===\n")
        self.eredmeny_text.insert(tk.END, f"Összes regisztrált modell: {len(self.auto_objektumok)} db\n")
        self.eredmeny_text.insert(tk.END, f"Gyűjtemény becsült összértéke: {osszertek:,.0f} Ft\n".replace(",", " "))
        if legregebbi:
            self.eredmeny_text.insert(tk.END,
                                      f"Legrégebbi modell: {legregebbi.modell_nev} ({legregebbi.gyartasi_ev})\n")


if __name__ == "__main__":
    gyoker = tk.Tk()
    alkalmazas = BogarApp(gyoker)
    gyoker.mainloop()