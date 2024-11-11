% Frekvencija signala nosioca neophodna za modulaciju signala x
Fc = 10;
Fc2=30;

% Frekvencija uzorkovanja
Fs = 1000;

% Vremensko trajanje od dvije sekunde
% 0 - početak; 1/Fs - vrijednost povećavanja; 2 - kraj
t = (0 : 1 / Fs : 2);

% Sinusoida sa vremenskim trajanjem "t"
x = sin(2*pi*t);% Pva kolona grafika
x1 = cos(2*pi*t);% Druga kolona grafika
% Signal nosilac
y = sin(2*pi*Fc*t);
y2=sin(2*pi*Fc2*t);

% Amplitudna modulacija
z = ammod(x, Fc, Fs);
z2 = ammod(x1, Fc2, Fs);

% Crtanje prvog grafika (sinusoidalni signal s informacijom)
subplot(3, 2, 1); % 3 - broj redova, 2 - broj kolona, 1 - redni broj u koordinatnoj mreži
plot(x);
xlim([0 2000]); % X osa biva ograničena na maksimalnu vrijednost od 2 sekunde
grid on;
title('Sinusoida sin(2pi*t)');
xlabel('Vrijeme');
ylabel('Amplituda');
%
subplot(3, 2, 2); % 3 - broj redova, 2 - broj kolona, 1 - redni broj u koordinatnoj mreži
plot(x1);
xlim([0 2000]); % X osa biva ograničena na maksimalnu vrijednost od 2 sekunde
grid on;
title('Sinusoida cos(2pi*t)');
xlabel('Vrijeme');
ylabel('Amplituda');
% Crtanje drugog grafika (signal nosilac)
subplot(3, 2, 3);
plot(y);
text(1, 0.5, ['Fc = ' num2str(Fc) ' Hz'], 'FontSize', 12, 'Color', 'red');
xlim([0 2000])
grid on;
title('Signal nosilac sin(2pi*Fc*t)');
xlabel('Vrijeme');
ylabel('Amplituda');
subplot(3, 2, 4);
plot(y2);
xlim([0 2000])
grid on;
title('Signal nosilac sin(2pi*Fc*t)');
xlabel('Vrijeme');
ylabel('Amplituda');
text(1, 0.5, ['Fc2 = ' num2str(Fc2) ' Hz'], 'FontSize', 12, 'Color', 'red');

% Crtanje trećeg grafika (modulisani signal)
subplot(3, 2, 5);
plot(z);
xlim([0 2000])
grid on;
title('Amplitudna modulacija');
xlabel('Vrijeme');
ylabel('Amplituda');
subplot(3,2,6);
plot(z2);
xlim([0 2000])
grid on;
title('Amplitudna modulacija');
xlabel('Vrijeme');
ylabel('Amplituda');

