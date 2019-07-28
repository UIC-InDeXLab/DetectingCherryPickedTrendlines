%%---------------------------
goodplot();
A = csvread('4-rand1.csv');
h = bar(A);
hold on; grid on;
% set(gca,'YScale','log');
ylabel('variance');
xlabel('support');
legend('pair smp,N','pair smp,NlogN','point sampling')
set(gca,'xticklabels',{'0.1','0.3','0.5','0.7','0.9','0.98'});
set(gca,'FontSize',22);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 22, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 22, 'FontWeight', 'Bold');
print -dpdf -r150 4_rand1.pdf;
hold off;
%%
goodplot();
A = csvread('4-rand1_2.csv');
h = bar([10,20,30,40,50,60,70,80,90,100],A);
hold on; grid on;
% set(gca,'YScale','log');
ylabel('variance');
xlabel('N');
legend('pair smp,N','pair smp,NlogN','point sampling')
set(gca,'XLim',[5 105])
% set(gca,'xticklabels',{'10','20','30','40','50','60','70','80','90','100'});
% set(gca,'xticklabels',{10,20,30,40,50,60,70,80,90,100});
set(gca,'FontSize',22);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 22, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 22, 'FontWeight', 'Bold');
print -dpdf -r150 4_rand1_2.pdf;
hold off;
%% stock time
goodplot();
A = csvread('4-rand2-stock.csv');
plot(A(:,1), A(:,5), 's-', 'LineWidth', 4,'markers',22,'Color', [20, 200, 20]/256);
hold on; grid on;
plot(A(:,1), A(:,6), '^-', 'LineWidth', 4,'markers',22,'Color', [20, 20, 200]/256);
%text(1.2,A(1,6),strcat('\leftarrow',num2str(100*A(1,8)),'% non-zero cells'),'FontSize',22,'FontWeight','Bold');
legend('Exact','Randomized','location','nw');
ylabel('time (sec) -- logscale');
xlabel('n');
% axis([8*10^6,10^7,10^-1,10^3]);
set(gca,'YTick',[10^-1,10^0,10^1,10^2,10^3]);
%set(gca,'xticklabels',{'N1','N2','N3','N4','N5','N6','N7'});
%set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',22);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 22, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 22, 'FontWeight', 'Bold');
set(gca,'YScale','log');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 4_rand2t.pdf;
hold off;
%% stock error
goodplot();
A = csvread('4-rand2-stock.csv');
plot(A(:,1), A(:,2), ':', 'LineWidth', 6,'Color', [20, 200, 20]/256);
hold on; grid on;
errorbar(A(:,1), A(:,3), A(:,4),'--', 'LineWidth', 4,'Color', [20, 20, 200]/256);
%text(1.2,A(1,6),strcat('\leftarrow',num2str(100*A(1,8)),'% non-zero cells'),'FontSize',22,'FontWeight','Bold');
legend('Exact','Randomized','location','nw');
ylabel('support');
xlabel('n');
axis([8*10^6,10^7,0.1,.3]);
% set(gca,'YTick',[10^-1,10^0,10^1,10^2,10^3]);
%set(gca,'xticklabels',{'N1','N2','N3','N4','N5','N6','N7'});
%set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',22);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 22, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 22, 'FontWeight', 'Bold');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 4_rand2e.pdf;
hold off;