data=load('Js-Abaqus-at-time-3p000.txt')
figure;
for i=2%:size(data,1)
     plot(data(1,2:end),data(i,2:end))
     hold on
end
data=load('Js-at-time-3.0.txt')
for i=2:size(data,1)
     plot(data(1,2:end),data(i,2:end))
     hold on
end