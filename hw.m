function x = hw()
    A = [9 -3 9 -12; -3 5 -5 8; 9 -5 19 -17; -12 8 -17 22];
    b = [-15; 13; -28; 34];
    x0 = [0;0;0;0];
    x = optimize(A, b, x0);
end


function result = computeDerivative(A,b,x)
    result = A*x - b;
end

function result = optimize(A, b, x)
    
    derivative = computeDerivative(A,b,x);
    epsilon = 0.001;
    while norm(derivative) > epsilon
        s = -(A*x - b);
        lambda = -(s'*derivative)/(s'*A*s);
        derivative = computeDerivative(A,b,x);
        x = x + lambda*s;
    end
    result = x;
end





