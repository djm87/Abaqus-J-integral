data1=load('Js-Abaqus-at-time-1p000.txt')
figure;
for i=9%:size(data,1)
     plot(data1(1,2:end),data1(i,2:end),'--b')
     hold on
end
data2=load('Js-at-time-1.0.txt')
for i=7%:size(data,1)
     plot(data2(1,2:end),data2(i,2:end))
     hold on
end

%Difference between Abaqus and Mine
figure; plot(data1(1,2:end),abs(data1(9,2:end)-data2(7,2:end))./data1(9,2:end)*100)

%% Difference from analytical solution
sig=10000
a=0.5

KI_Infinite=sig*sqrt(pi*a)
v=0.32
E=200e9
K1=sqrt(data1(10,2)*(E/(1-v^2)))
K2=sqrt(7.213E-04*(E/(1-v^2)))
K1=1.268935E+04
Error1 =abs(KI_Infinite-K1)/KI_Infinite*100
Error2 =abs(KI_Infinite-K2)/KI_Infinite*100
Error3 =abs(K1-K2)/K1*100
%%
E1=70e9
v=0.3
K1=sqrt(32.285*(E1/(1-v^2)))
K2=sqrt(32.2998*(E1/(1-v^2)))
Error3 =abs(K1-K2)/K1*100
