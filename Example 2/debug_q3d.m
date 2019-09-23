clear all
data=load('debug_q3d.txt')

slices=sort(unique(data(:,4)),'descend')
C=zeros(length(data),3); %colors
S=ones(length(data),1)*5; %size

sliceN=3
cnt=1
for i = 1:length(data)
    if data(i,4)==slices(sliceN)
        sliceData(cnt,1:5)=data(i,:);
        cnt=cnt+1;
    end
end

% for i = 1:length(data)
%     C(i,:)=[data(i,5),data(i,5),data(i,5)].*max
% end
% figure;scatter3(sliceData(:,2),sliceData(:,4))
pointsize = 10;
figure;scatter3(sliceData(:,2), sliceData(:,3),sliceData(:,5), pointsize, sliceData(:,5));