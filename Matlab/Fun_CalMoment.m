% 计算阶距 传入参数（数据源，阶数） 传出（阶距）
function moment = cal_moment(H, order)
    len = size(H,1);
    fea_num = size(H,2);
    mean_H = mean(H);
    if order == 1
        moment = mean_H;
    else
        mean_H = repmat(mean_H, len, 1);
        H = H - mean_H;
        H = H.^(order);
        H = mean(H);
        H = H.^(1/order);
        moment = H;
    end
end