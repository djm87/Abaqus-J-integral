data1=load('Js-at-time-0.20000000298Interface.txt')
figure;
for i=2:size(data1,2)
     plot(data1(2:end,1),-data1(2:end,i),'--b')
     hold on
end
data2=load('Js-at-time-0.20000000298.txt')
for i=2:size(data2,2)
     plot(data2(2:end,1),data2(2:end,i))
     hold on
end
for i=2:size(data2,2)
     plot(data2(2:end,1),data2(2:end,i)+data1(2:end,i))
     hold on
end
hold off

ylabel('Value of J')
xlabel('Position along crack front')
%%
%Difference between Abaqus and Mine
% figure; plot(data1(1,2:end),abs(fliplr(sqrt(data1(level,2:end).*(E/(1-v^2))))-sqrt(data2(level+offset,2:end).*(E/(1-v^2))))./fliplr(sqrt(data1(level,2:end).*(E/(1-v^2))))*100)
% ylim([0,100])
% ylabel('% difference from Abaqus')
% xlabel('Position along crack front')
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
