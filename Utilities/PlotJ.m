v=0.3
E=70e9

data1=load('Js-Abaqus-at-time-1p000.txt')
figure;
offset=-1
level=12
for i=level%:size(data,1)
     plot(fliplr(data1(1,2:end)),sqrt(data1(i,2:end).*(E/(1-v^2))),'--b')
     hold on
end
data2=load('Js-at-time-1.0.txt')
for i=level+offset%size(data,1)
     plot(data2(1,2:end),sqrt(data2(i,2:end).*(E/(1-v^2))))
     hold on
end
ylabel('Value of K')
xlabel('Position along crack front')
%%
%Difference between Abaqus and Mine
figure; plot(data1(1,2:end),abs(fliplr(sqrt(data1(level,2:end).*(E/(1-v^2))))-sqrt(data2(level+offset,2:end).*(E/(1-v^2))))./fliplr(sqrt(data1(level,2:end).*(E/(1-v^2))))*100)
ylim([0,100])
ylabel('% difference from Abaqus')
xlabel('Position along crack front')
%% Difference from analytical solution
% sig=10000
% a=0.5
% 
% KI_Infinite=sig*sqrt(pi*a)
% v=0.32
% E=200e9
% K1=sqrt(data1(10,2)*(E/(1-v^2)))
% K2=sqrt(data2(5,2)*(E/(1-v^2)))
% Error1 =abs(KI_Infinite-K1)/KI_Infinite*100
% Error2 =abs(KI_Infinite-K2)/KI_Infinite*100
