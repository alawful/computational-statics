clear; clc; close all;

r = 1;
theta_eq = acos(2 / (0.5 + pi));

A = [0 0];
e_AB = [-sin(theta_eq) cos(theta_eq)];
B = A + r * e_AB;

phi = linspace(-pi/2, pi/2, 400);
x_semi = r * cos(phi);
y_semi = r * sin(phi);

R = [cos(theta_eq) -sin(theta_eq); sin(theta_eq) cos(theta_eq)];
pts = R * [x_semi; y_semi];
x_semi_r = pts(1,:);
y_semi_r = pts(2,:);

B = [x_semi_r(end) y_semi_r(end)];
C = [x_semi_r(1)   y_semi_r(1)];

figure; hold on; grid on; axis equal;

plot(x_semi_r, y_semi_r, 'r', 'LineWidth', 4);
plot([A(1) B(1)], [A(2) B(2)], 'r', 'LineWidth', 4);

plot(A(1), A(2), 'ks', 'MarkerSize', 10, 'MarkerFaceColor', 'k');
plot(B(1), B(2), 'bo', 'MarkerSize', 8, 'MarkerFaceColor', 'b');
plot(C(1), C(2), 'go', 'MarkerSize', 8, 'MarkerFaceColor', 'g');

text(A(1)+0.03, A(2)-0.06, 'A');
text(B(1)-0.18, B(2)+0.05, 'B');
text(C(1)+0.03, C(2)-0.06, 'C');

xlabel('x'); ylabel('y');
title(['\theta_{eq} = ' num2str(rad2deg(theta_eq),'%.2f') '^{\circ}']);

xlim([-1.2*r 1.2*r]);
ylim([-0.7*r 1.2*r]);
