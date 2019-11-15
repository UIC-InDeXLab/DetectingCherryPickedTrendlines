%%--------------------------- V1
goodplot();
A = readtable('V2_35.8845_few.csv');
A = table2array(A(:,2:6));
h = bar(A(:,[2,4]),'stacked','EdgeColor','none');
hold on; grid on;
line([0,10],[0,0],'color','black','LineWidth',1);
set(h,{'FaceColor'},{'w';[0, 0.4470, 0.7410]});
ylabel(sprintf('temp. difference between \n a summer and a winter day'));
axis([0 10 0 60]);
%set(gca,'XTick',1:1:7);
set(gca,'xticklabels',{'Vancouver','New York','Seattle','Las Vegas','Boston','Chicago','Dallas','Los Angeles','Beersheba'});
set(gca,'XTickLabelRotation',45)
set(gca,'FontSize',16);
set(gca,'FontWeight','Bold');
set(get(gca,'xlabel'),'FontSize', 16, 'FontWeight', 'Bold');
set(get(gca,'ylabel'),'FontSize', 16, 'FontWeight', 'Bold');
%set(gca,'YTick',[10^-5, 10^-4, 10^-3, 10^-2, 10^-1, 10^0]);
%text(1.5,0.01726,'\leftarrow support = 0.01726','FontSize', 16,'FontWeight','Bold');
%xlabel('');
%set(gca,'YTick',cellstr(num2str(round(log10(YTick(:))), '10^%d')));
print -dpdf -r150 v2.pdf;
hold off;
%%

