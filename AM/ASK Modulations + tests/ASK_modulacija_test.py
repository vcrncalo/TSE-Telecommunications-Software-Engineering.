# Kod sa testovima za z2_novo.py (ASK modulacija).
import numpy as np # Dodatak koji omogućava kreiranje kompleksnih nizova i matrica.
from ASK_modulacija import ask_modulacija # Iz koda zadatka ASK modulacije se koristi funckija "ask_modulacija".
# --------------------
binarna_sekvenca = [0, 1] # Definisanje binarne sekvence. Ako su definisane ove vrijednosti, drugi test će proći bez grešaka.
# binarna_sekvenca = [1, 0]
# --------------------
def test_ask_modulacija_dužina_nizova():
    t, bw, sint, st = ask_modulacija(binarna_sekvenca) # Pozivanje funkcije "ask_modulacija" sa parametrom "binarna_sekvenca" koji je proslijeđen i korištenjem t, bw, sint i st i dodjeljivanje tih vrijednosti varijablama.
    assert len(t) == len(bw) == len(sint) == len(st) == len(binarna_sekvenca) * 100 # Provjerava se da li su dužine svih nizova jednake.
# --------------------
def test_ask_modulacija_vrijednosti():
    t, bw, sint, st = ask_modulacija(binarna_sekvenca)
    assert np.all(bw[:100] == 0)  # Prvih 100 vrijednosti treba biti 0
    assert np.all(bw[100:] == 1)  # Ostalih 100 vrijednosti treba biti 1
# --------------------
