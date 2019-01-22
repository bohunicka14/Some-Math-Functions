function lagrange(X, Y)
    hold on;
    plot(X,Y,'b*');
    interval_begin = min(X);
    interval_end = max(X);
    for x = interval_begin : .01 : interval_end
        y = compute_y(X, Y, x);
        plot(x,y, 'r.');
    end
end

function result = compute_y(X,Y, value)
    result = 0;
    for y = 1:length(Y)
        result = result + Y(y)*(compute_l(X, value, y));
    end
end

function result = compute_l(X, value, index)
    result = 1;
    for i = 1:length(X)
        if index ~= i
           result = result * ((value - X(i))/(X(index) - X(i))); 
        end
    end
end

% priklad na spustenie
% lagrange([0 1 -1 3],[1 2 2 0]); 
