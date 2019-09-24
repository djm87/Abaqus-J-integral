Jtip=load('Js_corrected_3.000.txt')
Jfar=load('Js_3.000.txt')

figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

% Create multiple lines using matrix input to plot
plot1 = plot(Jtip(1,2:end),[Jtip(2,2:end);Jfar(2,2:end)],'LineWidth',2);
set(plot1(1),'DisplayName','Jtip');
set(plot1(2),'DisplayName','Jfar');

% Create ylabel
ylabel('J Integral');

% Create xlabel
xlabel('Contour #');

box(axes1,'on');
% Create legend
legend1 = legend(axes1,'show');
set(legend1,...
    'Position',[0.209523811013925 0.737698415678645 0.141071427081312 0.110714282734053]);

