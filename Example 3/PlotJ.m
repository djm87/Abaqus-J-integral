data1=load('Js-Abaqus-at-time-3p000.txt')
figure;
for i=2:size(data,1)
     plot(data1(1,2:end),data1(i,2:end),'--b')
     hold on
end
% data2=load('Js-at-time-3.0.txt')
% for i=2:size(data,1)
%      plot(data2(1,2:end),data2(i,2:end))
%      hold on
% end
% figure; plot(data(1,2:end),abs(data1(9,2:end)-data2(7,2:end))./data1(9,2:end)*100)
% figure; plot(data(1,2:end),abs(data1(9,2:end)-data2(7,2:end))./data1(9,2:end)*100)