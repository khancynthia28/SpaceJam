 % Read the sample image in
    im = imread('houghlines3.jpg');
    
    % Find edges using the Canny operator with hysteresis thresholds of 0.1
    % and 0.2 with smoothing parameter sigma set to 1.
    edgeim = edge(im,'canny', [0.1 0.2], 1);

    figure(1), imshow(edgeim);

    
    % Link edge pixels together into lists of sequential edge points, one
    % list for each edge contour. A contour/edgelist starts/stops at an 
    % ending or a junction with another contour/edgelist.
    % Here we discard contours less than 10 pixels long.

    [edgelist, labelededgeim] = edgelink(edgeim, 10);
    
    % Display the edgelists with random colours for each distinct edge 
    % in figure 2

    drawedgelist(edgelist, size(im), 3, 'rand', 4); axis off        
