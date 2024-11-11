% --------------------------------------------------------------------- -----------------------
% Kod za ASK (amplitude shift keying) modulaciju
% --------------------------------------------------------------------- -----------------------
b = input('Unesite niz bitova kao što je: [0 1 0 1 1 0 1] (to uključuje uglaste zagrade i razmake između brojeva) \n ');
% Ako ne želimo unos od strane korisnika, možemo napisati sljedeće:
% b = [0 1 0 1 1 0 1];
% --------------------------------------------------------------------- -----------------------
n = length(b); % Određuje se dužina unesenog niza bitova (ako ne želimo da korisnik unosi brojeve).
% --------------------------------------------------------------------- -----------------------
bw = repelem(b, 100); % Svaka vrijednost bita se ponavlja 100 puta (više uzoraka po vremenskom periodu)
% Ako je b = [0 1 0 1] a druga vrijednost u zagradi 2, bw = [0 0 1 1 0 0 1 1]
% --------------------------------------------------------------------- -----------------------
t = linspace(0, n, length(bw)); % Definisanje vremenskog vektora (od 0 do dužine unesenog niza bitova)
% Posljednja vrijednost vremenskog vektora t označava ukupan broj tačaka signala
% --------------------------------------------------------------------- -----------------------
sint = sin(2 * pi * t); % Sinusoidalni signal se generiše
st = bw .* sint;
% --------------------------------------------------------------------- -----------------------
% Crtanje grafika digitalnog signala
subplot(3, 1, 1); % Tri reda, jedna kolona, prvi grafik u matrici
plot(t, bw, 'LineWidth', 1.5);
grid on; % Koordinatna mreža je omogućena
axis([0 n -2 2]); % Vidljivost po x osi od 0 do n, po y osi od -2 do 2
title('Digitalni signal'); % Naslov grafika
xlabel('Vrijeme'); % x osa označava vrijeme
ylabel('Amplituda'); % y osa označava amplitudu
% --------------------------------------------------------------------- -----------------------
% Crtanje grafika sinusoidalnog signala nosioca
subplot(3, 1, 2);
plot(t, sint, 'LineWidth', 1.5);
grid on;
axis([0 n -2 2]);
title('Sinusoidalni signal');
xlabel('Vrijeme');
ylabel('Amplituda');
% --------------------------------------------------------------------- -----------------------
% Crtanje modulisanog signala
subplot(3, 1, 3);
plot(t, st, 'LineWidth', 1.5);
grid on;
axis([0 n -2 2]);
title('Modulisani signal');
xlabel('Vrijeme');
ylabel('Amplituda');
% --------------------------------------------------------------------- -----------------------
