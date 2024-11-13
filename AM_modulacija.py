# --------------------
import numpy as np  # Koristi se za matematičke operacije koje budu predsatvljene grafikom.
import matplotlib.pyplot as plt  # Neophodno za kreiranje grafika kao u Matlab-u.
# --------------------
def amplitudna_modulacija(Fc, Fs, duration): # Funkcija za amplitudnu modulaciju, proslijeđuju se: frekvencija nosioca, frekvencija uzorkovanja i trajanje signala.
    """ Amplitudna modulacija sa datom frekvencijom signala nosioca (Fc),
    frekvencijom uzorkovanja (Fs), i vremenskim trajanjem signala (duration)."""
    t = np.arange(0, duration, 1 / Fs)  # Vremensko trajanje sa povećanjem vrijednosti od 1 / Fs.
    x = np.sin(2 * np.pi * t) # Signal s informacijom (x): sin(2*pi*t).
    y = np.sin(2 * np.pi * Fc * t) # Signal nosilac: sin(2*pi*Fc*t).
    z = x * np.cos(2 * np.pi * Fc * t) # Amplitudna modulacija.
    return t, x, y, z # Vraćanje vrijednosti.
# --------------------
def crtanje_grafika(t, x, y, z, Fc): # Funkcija za crtanje grafika.
    plt.subplot(3, 1, 1)  # 3 reda, 1 kolona, prvi po redu.
    plt.plot(t, x) # Crtanje prvog grafika (signal s informacijom), t je vrijeme.
    plt.xlim([0, max(t)])  # Ograničenje x ose od 0 do maksimalnog trajanja signala.
    plt.grid(True)  # Crtanje koordinatne mreže.
    plt.title('Sinusoida sin(2*pi*t)') # Naslov grafika.
    plt.xlabel('Vrijeme (s)') # Oznaka x ose.
    plt.ylabel('Amplituda') # Oznaka y ose.
# --------------------
    plt.subplot(3, 1, 2)
    plt.plot(t, y) # Crtanje drugog signala (signal nosilac).
    plt.xlim([0, max(t)])
    plt.grid(True)
    plt.title('Signal nosilac sin(2*pi*Fc*t)')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Amplituda')
    plt.text(0, 0.5, f'Fc = {Fc} Hz', fontsize=12, color='red')  # Tekst koji predstavlja vrijednost Fc frekvencije.
# --------------------
    plt.subplot(3, 1, 3)
    plt.plot(t, z) # Crtanje trećeg grafika (modulisani signal).
    plt.xlim([0, max(t)])
    plt.grid(True)
    plt.title('Amplitudna modulacija')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Amplituda')
# --------------------
    plt.tight_layout()  # Podešavanje rasporeda grafika kako ne bi došlo do njihovog preklapanja.
    plt.show()
# --------------------
def glavna_funkcija(Fc = 10, Fs = 1000, duration = 2): # Glavna funkcija koja poziva funkciju za amplitudnu modulaciju i grafički prikaz.
    t, x, y, z = amplitudna_modulacija(Fc, Fs, duration) # Pozivanje funkcije amplitudne modulacije i proslijeđivanje parametara.
    crtanje_grafika(t, x, y, z, Fc) # Pozivanje funkcije za crtanje signala.
    return t, x, y, z  # Vraćanje podataka za eventualno testiranje.
# --------------------
if __name__ == "__main__": # Pokretanje glavne funkcije ako se kod direktno izvršava. Ovo će biti zanemareno u pytest-u.
    glavna_funkcija() # Pozivanje glavne funkcije koja poziva ostale funkcije.
# --------------------
