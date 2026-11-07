clc
clear

E = 200e9;
A = 100e-6;
P = 10e3;

coord = [0 0;
         3 0;
         1.5 2.598];

elem = [1 2;
        1 3;
        2 3];

nn = size(coord,1);
ne = size(elem,1);
ndof = 2*nn;

K = zeros(ndof);

for e = 1:ne
    i = elem(e,1);
    j = elem(e,2);
    xi = coord(i,1); yi = coord(i,2);
    xj = coord(j,1); yj = coord(j,2);
    L = sqrt((xj-xi)^2+(yj-yi)^2);
    c = (xj-xi)/L;
    s = (yj-yi)/L;
    k = (E*A/L)*[ c^2   c*s  -c^2  -c*s;
                  c*s   s^2  -c*s  -s^2;
                 -c^2  -c*s   c^2   c*s;
                 -c*s  -s^2   c*s   s^2];
    dof = [2*i-1 2*i 2*j-1 2*j];
    K(dof,dof) = K(dof,dof) + k;
end

F = zeros(ndof,1);
F(6) = -P;

fix = [1 2 4];
all = 1:ndof;
free = setdiff(all,fix);

u = zeros(ndof,1);
Kff = K(free,free);
Ff = F(free);
u(free) = Kff\Ff;

R = K*u - F;

N = zeros(ne,1);
for e = 1:ne
    i = elem(e,1);
    j = elem(e,2);
    xi = coord(i,1); yi = coord(i,2);
    xj = coord(j,1); yj = coord(j,2);
    L = sqrt((xj-xi)^2+(yj-yi)^2);
    c = (xj-xi)/L;
    s = (yj-yi)/L;
    T = [c s 0 0;
         0 0 c s];
    dof = [2*i-1 2*i 2*j-1 2*j];
    ue = T*u(dof);
    N(e) = E*A/L*(ue(2)-ue(1));
end

NkN = N/1000

state = cell(ne,1);
for e = 1:ne
    if N(e) > 0
        state{e} = 'Tension';
    elseif N(e) < 0
        state{e} = 'Compression';
    else
        state{e} = 'Zero';
    end
end
state

scale = 100;
ud = reshape(u,2,nn)';
coord_def = coord + scale*ud;

figure
hold on
axis equal
for e = 1:ne
    i = elem(e,1);
    j = elem(e,2);
    plot(coord([i j],1),coord([i j],2),'k-');
    plot(coord_def([i j],1),coord_def([i j],2),'r-');
end
legend('orig','def')
