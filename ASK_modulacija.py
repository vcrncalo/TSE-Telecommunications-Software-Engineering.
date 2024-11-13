# Kod za ASK modulaciju
# --------------------
import numpy as np # Dodatak koji omogućava korištenje broja pi (np.pi) i definisanje sinusa (np.sin).
import matplotlib.pyplot as plt # Dodatak koji omogućuava crtanje grafika.
# --------------------
def ask_modulacija(binarna_sekvenca):
    # Generiše se ASK modulacija komponenata za datu sekvencu.
    n = len(binarna_sekvenca) # Dužina binarne sekvence
    bw = np.repeat(binarna_sekvenca, 100) # Svaki bit se ponavlja 100 puta
    t = np.linspace(0, n, len(bw)) # Definisanje vremenskog vektora od 0 do dužine bita sekvence. Vremenski vektor ima ukupno len(bw) tačaka.
    sint = np.sin(2 * np.pi * t) # Definisanje sinusoidalnog signala
    st = bw * sint # ASK modulisani signal je jednak proizvodu digitalnog signala i sinusoidalnog signala.
    return t, bw, sint, st # Vraćaju se vrijednosti t, bw, sint i st.
# --------------------
def plot_ask_signals(t, bw, sint, st):
    # U ovoj funkciji se crtaju sljedeći signali: digitalni signal, signal nosilac i ASK modulisani signal.
    plt.figure(figsize=(10, 5)) # Definisanje veličine grafika.
# --------------------
    # Crtanje grafika digitalnog signala.
    plt.subplot(3, 1, 1) # Tri reda, jedna kolona, prvi grafik po redu.
    plt.plot(t, bw, linewidth=1.5) # Crtanje digitalnog signala.
    plt.grid(True) # Koordinatna mreža je omogućena.
    plt.axis([0, max(t), -2, 2]) # Granice x ose: (0, max(t), granice y ose: (-2, 2).
    plt.title('Digitalni signal') # Naslov grafika.
    plt.xlabel('Vrijeme') # Oznaka x ose.
    plt.ylabel('Amplituda') # Oznaka y ose.
# --------------------
    # Crtanje signala nosioca
    plt.subplot(3, 1, 2)
    plt.plot(t, sint, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('Signal nosilac')
    plt.xlabel('Vrijeme')
    plt.ylabel('Amplituda')
# --------------------
    # Crtanje modulisanog signala
    plt.subplot(3, 1, 3)
    plt.plot(t, st, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('ASK modulisani signal')
    plt.xlabel('Vrijeme')
    plt.ylabel('Amplituda')
# --------------------
    plt.tight_layout() # Definisanje načina prikazivanja grafika.
    plt.show() # Grafik se prikazuje.
# --------------------
if __name__ == "__main__": # Ovo se definiše kako bi se program mogao pokrenuti i prikazati vrijednosti grafika te kako bi se mogla pokrenuti test datoteka koja zaobilazi ovaj dio koda za razliku od toga kad se ovaj kod pokrene.
    binarna_sekvenca = input("Unesite binarnu sekvencu kao što je: [1, 0, 1, 0] sa uglastim zagradama, zarezima i razmacima između brojeva: ")
    #print(binarna_sekvenca)
    binarna_sekvenca = list(map(int, binarna_sekvenca.strip('[]').split(","))) # Unos korisnika se pretvara u listu pogodnu za izvršavanje koda. Uklanjaju se uglaste zagrade, brojevi se razdvajaju kada se naiđe na zarez, map(int, ...) pretvara svaki broj kao što je "1" u 1 u (int), list() to sve pretvara u listu.
    t, bw, sint, st = ask_modulacija(binarna_sekvenca) # ask_modulacija() se izvršava i vrijednosti sa lijeve strane znaka jednakosti se spremaju u varijable. binarna_sekvenca je ulaz funkcije.
    plot_ask_signals(t, bw, sint, st) # Crtanje grafika koristeći navedene varijable kao ulaze.
