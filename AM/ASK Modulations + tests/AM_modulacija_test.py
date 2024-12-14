# --------------------
import numpy as np  # Koristi se za matematičke operacije koje budu predsatvljene grafikom.
from AM_modulacija import amplitudna_modulacija # Korištenje funkcije "amplitudna_modulacija" iz prvog zadatka.
# ---------------------
Fc = 10 # Frekvencija signala nosioca.
Fs = 1000 # Frekvencija uzorkovanja.
duration = 2 # Trajanje.
# ---------------------
def test_amplitudne_modulacije_dužina_vektora(): # Prvi test: Provjeravanje dužine vektora.
    t, x, y, z = amplitudna_modulacija(Fc, Fs, duration) # Pozivanje funkcije amplitudne modulacije iz prvog zadatka.
    assert len(t) == len(x) == len(y) == len(z) == Fs * duration # Provjeravanje dužine vektora.
# --------------------
def test_amplitudne_modulacije_signal_nosilac(): # Drugi test: Provjeravanje vrijednosti amplitude signala nosioca.
    t, x, y, z = amplitudna_modulacija(Fc, Fs, duration) # Pozivanje funkcije amplitudne modulacije iz prvog zadatka.
    assert np.all(y <= 1) and np.all(y >= -1) # Provjerava se da li su vrijednosti signala nosioca u opsegu [-1, 1], tj. da li je amplituda u tom opsegu.
# --------------------
def test_amplitudne_modulacije_modulisani_signal(): # Drugi test: Provjeravanje vrijednosti amplitude signala nosioca.
    t, x, y, z = amplitudna_modulacija(Fc, Fs, duration) # Pozivanje funkcije amplitudne modulacije iz prvog zadatka.
    assert np.all(z <= 1) and np.all(z >= -1) # Provjerava se da li su vrijednosti u modulisanoj sinusoidi u opsegu [-1, 1].
# --------------------
