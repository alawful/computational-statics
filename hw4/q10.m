clc
clear

Lab = sqrt(4^2 + 2.5^2);
Lbc = sqrt(6^2 + 1^2);
Lec = sqrt(6^2 + 3.5^2);

cab = 4/Lab;
sab = 2.5/Lab;

cbc = 6/Lbc;
sbc = 1/Lbc;

cec = 6/Lec;
sec = 3.5/Lec;

A = [ cab    0     0     0     0    0   1   0   0   1;
      sab    0     0     0     0    0   0   0   0   0;
        0    0     0   cec     0    1  -1   0   0   0;
        0    1     0   sec     0    0   0   0   0   0;
        0    0     0     0     0   -1   0   0   0   0;
        0    0     0     0     1    0   0   0   0   0;
     -cab    0   cbc     0     0    0   0   0   0   0;
     -sab   -1   sbc     0     0    0   0   0   0   0;
        0    0  -cbc  -cec     0    0   0   1   0   0;
        0    0  -sbc  -sec    -1    0   0   0   1   0];

b = [0; 3000; 0; 4500; 0; 0; 0; 0; 0; 0];

x = A\b;

f2  = x(1);
f3  = x(2);
f4  = x(3);
f5  = x(4);
f6  = x(5);
f7  = x(6);
f8  = x(7);
Rcx = x(8);
Rcy = x(9);
Rax = x(10);

F = [f2 f3 f4 f5 f6 f7 f8];
Fkips = F/1000

state = cell(7,1);
for i = 1:7
    if F(i) > 0
        state{i} = 'Tension';
    elseif F(i) < 0
        state{i} = 'Compression';
    else
        state{i} = 'Zero';
    end
end
state
R = [Rcx Rcy Rax]
