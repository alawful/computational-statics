clear; clc; close all;

L  = 30;
w  = 2;
xA = 0;  yA = 0;
xB = 30; yB = 6;

a = yB/(L^2);
H = w/(2*a);

fprintf('PART 1:\n');
fprintf('y(x) = a x^2,  a = %.10f  (1/m)\n', a);
fprintf('=> y(x) = %.10f x^2\n\n', a);

fprintf('PART 2:\n');
fprintf('H = %.10f kN\n\n', H);

VA = w*xA;
VB = w*xB;

TA = sqrt(H^2 + VA^2);
TB = sqrt(H^2 + VB^2);

x_minT = 0;
T_min  = H;

fprintf('PART 3:\n');
fprintf('T_A = %.10f kN\n', TA);
fprintf('T_B = %.10f kN\n', TB);
fprintf('Minimum tension at x = %.10f m,  T_min = %.10f kN\n\n', x_minT, T_min);

x = linspace(0, L, 400);
y = a*x.^2;
V = w*x;
T = sqrt(H^2 + V.^2);

figure(1);
plot(x, y, 'LineWidth', 2); grid on;
xlabel('x (m)'); ylabel('y (m)');
title('Cable shape y(x)');

figure(2);
plot(x, T, 'LineWidth', 2); grid on;
xlabel('x (m)'); ylabel('T (kN)');
title('Cable tension T(x)');

w2  = 1.2*w;
H2  = w2/(2*a);

Tmax1 = sqrt(H^2  + (w*L)^2);
Tmax2 = sqrt(H2^2 + (w2*L)^2);

pct_change = (Tmax2 - Tmax1)/Tmax1 * 100;

fprintf('PART 5:\n');
fprintf('Old Tmax = %.10f kN\n', Tmax1);
fprintf('New Tmax (w*1.2) = %.10f kN\n', Tmax2);
fprintf('Percent change in Tmax = %.10f %%\n', pct_change);
