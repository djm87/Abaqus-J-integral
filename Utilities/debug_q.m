data=load('debug_q_surface.txt')
% figure;
% scatter3(data(:,4),data(:,5),data(:,6),data(:,2)+1)


% clear all
% data=load('debug_q.txt')

slices=sort(unique(data(:,4)),'descend')
C=zeros(length(data),3); %colors
S=ones(length(data),1)*5; %size
pointsize = 10;
figure;scatter3(data(:,4),data(:,6),data(:,2), pointsize, data(:,2));