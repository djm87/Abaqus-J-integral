data=load('Js_Interface_fineStep_spatial_1.000.txt')
ind=data(:,4)>1.9;Ztmp=data(ind,4);
Xtmp=data(ind,2);Ytmp=data(ind,3);
Cint=-data(ind,1)

figure; scatter(Xtmp,Cint)

% gx=linspace(min(Xtmp),max(Xtmp),100)
% gz=linspace(min(Ztmp),max(Ztmp),100)
% 
% [xq,zq] = meshgrid(gx,gz);
% vq = griddata(Xtmp,Ztmp,Cint,xq,zq);
% figure
% plot3(Xtmp,Ztmp,Cint,'ro')
% % hold on
% surf(xq,zq,vq)