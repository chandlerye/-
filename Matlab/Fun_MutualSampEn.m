
function SampEnVal2 = mutual_sampEn(data,data2, m)
% SAMPEN  计算时间序列data的样本熵
% 输入：data是要分析的一维行向量，data为输入数据序列,向空间重构的时间延迟默认为1，
%       m重构维数，一般选择1或2，优先选择2，一般不取m>2
%       r 阈值大小，一般选择r=0.1~0.25*Std(data)
% 输出：SampEnVal样本熵值大小
% $Author: lskyp
% 修改：yuhansgg
% $Date:   2018.03.05
% Orig Version: V1.0--------分开计算长度为m的序列和长度为m+1的序列
%                           这一版的计算有些问题，需要注意两个序列总数都要为N-m
% Modi Version: V1.1--------综合计算，计算距离时通过矩阵减法完成，避免重循环
% V1.1 Modified date: 2018.03.05
% 样本熵公式参考论文：《A review on sample entropy applications for the non-invasive analysis of atrial fibrillation electrocardiograms》


% std_data = [data,data2];
% 
% r = 0.2*std(std_data);

r=0.2;
data = data(:)';
data2 =data2(:)';
N = length(data);
Nkx1 = 0;
Nkx2 = 0;

% 分段计算距离，x1为长度为m的序列，x2为长度为m+1的序列

for k = N - m:-1:1
    x1(k, :) = data(k:k + m - 1);
    
    
    x11(k, :) = data2(k:k + m - 1);
    
    
    x2(k, :) = data(k:k + m );
    
    
    x22(k, :) =  data2(k:k + m );
end

for k = N - m:-1:1
    % x1序列计算
    % 统计距离，由于每行都要与其他行做减法，因此可以先将该行复制为N-m的矩阵，然后
    % 与原始x1矩阵做减法，可以避免两重循环，增加效率
    x1temprow = x1(k, :);
    x1temp    = ones(N - m, 1)*x1temprow;
    
    % 可以使用repmat函数完成上面的语句，即
    % x1temp = repmat(x1temprow, N - m, 1);
    % 但是效率不如上面的矩阵乘法
    % 计算距离，每一行元素相减的最大值为距离
    dx1(k, :) = max(abs(x1temp - x11), [], 2)';
    
    % 模板匹配数
    Nkx1 = Nkx1 + (sum(dx1(k, :) < r) - 1)/(N - m - 1);  %% N-m+1 ？？？
    
    % x2序列计算，和x1同样方法
    x2temprow = x2(k, :);
    x2temp    = ones(N - m, 1)*x2temprow;
    dx2(k, :) = max(abs(x2temp - x22), [], 2)';
    Nkx2      = Nkx2 + (sum(dx2(k, :) < r) - 1)/(N - m - 1);
end

% 平均值
Bmx1 = Nkx1/(N - m);
Bmx2 = Nkx2/(N - m);

% 样本熵
SampEnVal2 = -log(Bmx2/Bmx1);

end
