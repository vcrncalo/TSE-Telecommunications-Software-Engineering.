import numpy as np # Koristi se za matematičke operacije koje budu predsatvljene grafikom
import matplotlib.pyplot as plt # Neophodno za kreiranje grafika kao u Matlab-u

# Frekvencija signala nosioca za signal s informacijom (x)
Fc = 10  # (Hz)

# Frekvencija uzorkovanja
Fs = 1000  # (Hz)

# Vremensko trajanje od dvije sekunde
t = np.arange(0, 2, 1 / Fs)  # Vremensko trajanje od dvije sekunde s povećanjem vrijednosti od 1 / Fs

# Signal s informacijom (x): sin(2*pi*t)
x = np.sin(2 * np.pi * t)

# Signal nosilac: sin(2*pi*Fc*t)
y = np.sin(2 * np.pi * Fc * t)

# Amplitudna modulacija
z = x * y  #
# ili
#z = x * np.cos(2 * np.pi * Fc * t)

# Crtanje prvog grafika (signal s informacijom)
plt.subplot(3, 1, 1)  # 3 reda, 1 kolona, prvi po redu
plt.plot(t, x)
plt.xlim([0, 2])  # Ograničenje x ose od 0 do 2 sekunde
plt.grid(True) # Crtanje koordinatne mreže
plt.title('Sinusoida sin(2*pi*t)')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Amplituda')

# Crtanje drugog signala (signal nosilac)
plt.subplot(3, 1, 2)
plt.plot(t, y)
plt.xlim([0, 2])
plt.grid(True)
plt.title('Signal nosilac sin(2*pi*Fc*t)')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Amplituda')
plt.text(0, 0.5, f'Fc = {Fc} Hz', fontsize=12, color='red') # Tekst koji predstavlja vrijednost Fc frekvencije

# Crtanje trećeg grafika (modulisani signal)
plt.subplot(3, 1, 3)
plt.plot(t, z)
plt.xlim([0, 2])
plt.grid(True)
plt.title('Amplitudna modulacija')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Amplituda')

# Prikaz svih grafika
plt.tight_layout()  # Podešavanje rasporeda grafika kako ne bi došlo do njihovog preklapanja
plt.show()
