# -----------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# -----------------------------------------------
# b = np.array([0, 1, 0, 1, 1, 0, 1]) # Definisanje dužine niza bitova (ako ne želimo da korisnik unosi brojeve)
b = input('Unesite niz binarnih brojeva kao što je: [0 1 0 1 1 0 1] (sa uglastim zagradama, zarezima i razmacima između brojeva): ')
b = np.array(eval(b))  # Pretvara se string u numpy niz brojeva
# -----------------------------------------------
n = len(b) # Dužina binarne sekvence 
# -----------------------------------------------
bw = np.repeat(b, 100) # Svaki bit se ponalja 100 puta, primjer: [1 0] postaje [1 1 1 ... (sto puta) 0 0 0 (sto puta)]
# -----------------------------------------------
# Time vector (from 0 to n with the same number of points as the length of bw)
t = np.linspace(0, n, len(bw)) # Vremenski vektor koji je definisan od 0 do n sa ukupnim brojem tačaka length(bw) što je u slučaju za b = [0 1 0 1 1 0 1] 7 * 100 = 700
# -----------------------------------------------
sint = np.sin(2 * np.pi * t) # Generisanje signala nosioca (sinusoidalni signal)
# -----------------------------------------------
st = bw * sint # Modulisani signal koji se dobije množenjem digitalnog i sinusoidalnog signala
# -----------------------------------------------
# Create the plots
plt.figure(figsize=(10, 8))
# -----------------------------------------------
# Crtanje digitalnog signala
plt.subplot(3, 1, 1)
plt.plot(t, bw, linewidth=1.5)
plt.grid(True)
plt.axis([0, n, -2, 2])
plt.title('Digitalni signal')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Amplituda')
# -----------------------------------------------
# Crtanje sinusoidalnog signala
plt.subplot(3, 1, 2)
plt.plot(t, sint, linewidth=1.5)
plt.grid(True)
plt.axis([0, n, -2, 2])
plt.title('Sinusoidalni signal nosilac')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Amplituda')
# -----------------------------------------------
# Crtanje ASK modulisanog signala
plt.subplot(3, 1, 3)
plt.plot(t, st, linewidth=1.5)
plt.grid(True)
plt.axis([0, n, -2, 2])
plt.title('ASK modulisani signal')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Amplituda')
# -----------------------------------------------
# Podešavanje prikaza grafika
plt.tight_layout()
plt.show()
# -----------------------------------------------
