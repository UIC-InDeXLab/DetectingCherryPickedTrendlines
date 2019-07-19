function goodplot( papersize, margin, fontsize )
%GOODPLOT Summary of this function goes here
%   Detailed explanation goes here
    if nargin == 0
        papersize = 5.5;
        margin = 0.2;
        fontsize = 18;
    elseif nargin == 1
        margin = 0.5;
        fontsize = 18;
    elseif nargin == 2
        fontsize = 18;
    end
    set(get(gca,'xlabel'),'FontSize', fontsize, 'FontWeight', 'Bold');
    set(get(gca,'ylabel'),'FontSize', fontsize, 'FontWeight', 'Bold');
    set(get(gca,'title'),'FontSize', fontsize, 'FontWeight', 'Bold');
    box off; 
    % axis square;
    set(gca,'defaultlinelinewidth',4)
    % set(gca,'LineWidth',2);
    set(gca,'FontSize',16);
    set(gca,'FontWeight','Bold');
    set(gcf,'color','w');
    set(gcf,'PaperUnits','inches');
    set(gcf,'PaperSize', [papersize*4/3 papersize]);
    set(gcf,'PaperPosition',[margin margin papersize*4/3-margin papersize-margin]);
    set(gcf,'PaperPositionMode','Manual');
end

