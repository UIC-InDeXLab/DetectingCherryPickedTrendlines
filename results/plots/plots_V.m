%%--------------------------- V1
goodplot();
y = [0.01726, 0, 7.13E-05, 0.000353722, 0.000431931, 0.000907684, 0.001138327, 0.004462099, 0.007826339 ,0.068838902,0.114507012];
bar(y);
hold on; grid on;
ylabel('support (log-scale)');
axis([0 12 10^-5 1]);
%set(gca,'XTick',1:1:7);
set(gca,'xticklabels',{'Overall',' ', 'Vancouver (min)','New York','Seattle','Las Vegas','Boston','Chicago','Dallas','Los Angeles','Beersheba (max)'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(gca,'YScale','log');
set(gca,'YTick',[10^-5, 10^-4, 10^-3, 10^-2, 10^-1, 10^0]);
text(1.5,0.01726,'\leftarrow support = 0.01726','FontSize', 16,'FontWeight','Bold');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 v1.pdf;
hold off;
%%

