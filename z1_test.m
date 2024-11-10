% Prvi test za signal s informacijom (x)
%!test
%! Fc = 10;
%! Fs = 1000;
%! t = (0 : 1 / Fs : 2);
%! x = sin(2*pi*t);
%! assert(length(x) == Fs * 2 + 1, 'Dužina signala x je netačna');
%! assert(all(abs(x) <= 1), 'Signal x treba biti u rasponu od -1 do 1');

% Test za signal nosilac (y)
%!test
%! Fc = 10;
%! Fs = 1000;
%! t = (0 : 1 / Fs : 2);
%! y = sin(2*pi*Fc*t);
%! assert(abs(max(y) - 1) < 0.1, 'Amplituda signala nosioca nije tačna.');
%! assert(abs(min(y) + 1) < 0.1, 'Amplituda signala nosioca nije tačna.');

% Test za modulisani signal (z)
%!test
%! Fc = 10;
%! Fs = 1000;
%! t = (0 : 1 / Fs : 2);
%! x = sin(2*pi*t);
%! z = ammod(x, Fc, Fs);
%! assert(length(z) == length(x), 'Dužina modulisanog signala se ne podudara s dužinom signala x');
%! assert(all(abs(z) <= 1), 'Amplituda modulisanog signala treba biti u rasponu od -1 do 1');

