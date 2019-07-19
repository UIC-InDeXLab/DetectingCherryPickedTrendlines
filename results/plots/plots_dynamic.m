goodplot();
bar([0.468809, 0.089391, 0.008971]);%, 's-', 'LineWidth', 4,'markers',14,'Color', [20, 200, 20]/256);
hold on; grid on;
%plot(A(:,2), A(:,3), 's-', 'LineWidth', 4,'markers',14,'Color', [20, 200, 20]/256);
ylabel('time (sec)');
%xlabel('number of columns (m)');
%axis([5*10^7 7*10^8 10^2 10^4]);
%set(gca,'XTick',[5*10^7,10^8,5*10^8]);
set(gca,'xticklabels',{'Direct-E','Direct-A','DynamicUpdate'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(gca,'YScale','log');
ylim([7*10^-3 10^0])
%set(gca,'XScale','log');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 Dyn_861.pdf;
hold off;
%%
goodplot();
bar([9.40675, 1.36323, 0.10505]);%, 's-', 'LineWidth', 4,'markers',14,'Color', [20, 200, 20]/256);
hold on; grid on;
ylabel('time (sec)');
set(gca,'xticklabels',{'Direct-E','Direct-A','DynamicUpdate'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(gca,'YScale','log');
ylim([8*10^-2 10^1])
set(gca,'YTick',[10^-1,10^0,10^1]);
%set(gca,'XScale','log');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 Dyn_1652.pdf;
hold off;
%%
goodplot();
bar([46.4114, 4.74315, 0.246313]);%, 's-', 'LineWidth', 4,'markers',14,'Color', [20, 200, 20]/256);
hold on; grid on;
ylabel('time (sec)');
set(gca,'xticklabels',{'Direct-E','Direct-A','DynamicUpdate'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(gca,'YScale','log');
%ylim([8*10^-2 10^2])
set(gca,'YTick',[10^-1,10^0,10^1]);
%set(gca,'XScale','log');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 Dyn_4549.pdf;
hold off;
%%
goodplot();
bar([151.104, 9.2722, 1.00985]);%, 's-', 'LineWidth', 4,'markers',14,'Color', [20, 200, 20]/256);
hold on; grid on;
ylabel('time (sec)');
set(gca,'xticklabels',{'Direct-E','Direct-A','DynamicUpdate'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(gca,'YScale','log');
ylim([8*10^-1 5*10^2])
set(gca,'YTick',[10^0,10^1,10^2]);
%set(gca,'XScale','log');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 Dyn_3486.pdf;
hold off;
%%
goodplot();
bar([1633.95, 57.4651, 6.78967]);%, 's-', 'LineWidth', 4,'markers',14,'Color', [20, 200, 20]/256);
hold on; grid on;
ylabel('time (sec)');
set(gca,'xticklabels',{'Direct-E','Direct-A','DynamicUpdate'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(gca,'YScale','log');
ylim([4*10^0 3*10^3])
set(gca,'YTick',[10^1,10^2,10^3]);
%set(gca,'XScale','log');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 Dyn_7081.pdf;
hold off;