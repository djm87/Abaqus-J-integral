% data=load('Js_Interface_spatial_3.000.txt');
% data=load('Js_lowest_micron_final_Interface_spatial_0.350.txt');
data=load('Js_lowest_micron_final_Interface_spatial_10.000.txt');
indz=data(:,4)==2.762742;Ztmp=data(indz,4);
Xtmp=data(indz,2);Ytmp=data(indz,3);
Cint=-data(indz,1);
Ytmpu=unique(Ytmp);
Ytmpu=Ytmpu(Ytmpu<2.71551);
Ytmpu=sort(Ytmpu);
figure
for i=1:2:length(Ytmpu)
    indy=Ytmp==Ytmpu(i);%4.069440%2.210560%2.16032%3.71776%3.76800%2.16032
    Xtmp2=Xtmp(indy);Ytmp2=Ytmp(indy);Ztmp2=Ztmp(indy);
    Cint2=Cint(indy);
     [Xtmp2,indx]=sort(Xtmp2);
     Cint2=Cint2(indx);
    plot(Xtmp2-11.98,Cint2)
    pause(1)
    hold on
end
ylabel('Material force')
xlabel('Distance from crack in x')

% gx=linspace(min(Xtmp),max(Xtmp),100)
% gz=linspace(min(Ztmp),max(Ztmp),100)
% 
% [xq,zq] = meshgrid(gx,gz);
% vq = griddata(Xtmp,Ztmp,Cint,xq,zq);
% figure
% plot3(Xtmp,Ztmp,Cint,'ro')
% % hold on
% surf(xq,zq,vq)