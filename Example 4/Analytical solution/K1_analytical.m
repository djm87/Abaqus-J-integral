%% Analytical solution to 3P flexural test with edge crack 
%https://en.wikipedia.org/wiki/Three-point_flexural_test 
P= %N?? 
B=2.7815 %um width
W=6.28 %um height
a=2.13520 %um crack length
aoW=a/W %um

KI=6*P/(B*W)*sqrt(a)*Y(aoW)


%Need to run model with support at 4W

%based on ASTM D5045-14 E1290-08 for crack lengths a less than 0.6 W
function output=Y(aoW)
    output=(1.99-aoW*(1-aoW)*(2.15-3.93*aoW+2.7*aoW^2)/((1+2*aoW)*(1-aoW)^(3/2))
end