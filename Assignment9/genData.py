# Bruce A. Maxwell
# Payal Chavan
# CS 5800 Algorithms (Seattle)
# Summer 2024
# Assignment 9
# Program for generating noisy data to test RANSAC
# Date: 08/16/2024


# Import necessary libraries
import sys
import random
import numpy as np
from matplotlib import pyplot as plt

'''
Generates an (x, y) pair using the following rule

if the point should be noise
   return a random x in the range x in [xmin, xmax] and y in [xmin*slope + intersect, xmax*slope + intersect]
else
   return a point (x, x  * slope + intersect + G(gauss_noise_sigma))  where x is in [xmin, xmax]
'''
# Function to generate a single point
def generatePoint(slope, intersect, gauss_noise_sigma, xmin, xmax, frac_noise):
    x = random.random() * (xmax - xmin) + xmin
    if random.random() < frac_noise:
        ymin = xmin * slope + intersect
        ymax = xmax * slope + intersect
        if ymin > ymax:
            tmp = ymin
            ymin = ymax
            ymax = tmp
            
        y = random.random() * (ymax - ymin) + ymin
        return (x, y)

    y = x * slope + intersect + random.gauss(0, gauss_noise_sigma)
    return (x, y)


'''
Generates N (x, y) data points using the given model parameters
Returns a list of tuples

The frac_noise determines the number of pure noise data points
'''
# Function to generate data points
def generateData(N, xmin=0.0, xmax=1.0, slope=1.0, intersect=0.0, gauss_noise_sigma=0.07, frac_noise=0.3):
    data = []
    for i in range(N):
        data.append(generatePoint(slope, intersect, gauss_noise_sigma, xmin, xmax, frac_noise))
    return data

# Function to compute the distance of a point from a line
def point_line_distance(point, line):
    x, y = point
    slope, intercept = line
    return abs(slope * x - y + intercept) / np.sqrt(slope**2 + 1)

# Function to fit a line to two points
def fit_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return (slope, intercept)

# RANSAC algorithm for line fitting
def ransac(data, threshold, iterations):
    best_inliers = []
    best_line = None
    
    for _ in range(iterations):
        # Randomly select 2 points
        sample = random.sample(data, 2)
        line = fit_line(sample[0], sample[1])
        
        inliers = []
        for point in data:
            if point_line_distance(point, line) < threshold:
                inliers.append(point)
        
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_line = line
    
    return best_line, best_inliers

# Testing RANSAC for different frac_noises, slopes, and intersects
def test_ransac():
    # Parameters
    frac_noises = [0.1, 0.3, 0.5]
    slopes = [1, 3, 7]
    intersects = [-1.0, 0.0, 1.0]
    N = 100
    xmin = 0
    xmax = 10
    gauss_noise_sigma = 0.5
    threshold = 1.0
    iterations = 100

    # Create subplots
    fig, axes = plt.subplots(len(frac_noises), len(slopes), figsize=(12, 12))
    fig.suptitle('RANSAC Line Fitting for Different Parameters')

    # Generate data, run RANSAC, and plot for each combination of parameters
    for i, frac_noise in enumerate(frac_noises):
        for j, slope in enumerate(slopes):
            intersect = intersects[j]  # Assuming intersects aligns with slopes
            data = generateData(N, xmin=xmin, xmax=xmax, slope=slope, intersect=intersect, gauss_noise_sigma=gauss_noise_sigma, frac_noise=frac_noise)
            best_line, best_inliers = ransac(data, threshold, iterations)

            ax = axes[i, j]
            ax.scatter(*zip(*data), color='red', label='Noisy Data')
            ax.scatter(*zip(*best_inliers), color='blue', label='Inliers')
            x_vals = np.array(ax.get_xlim())
            y_vals = best_line[0] * x_vals + best_line[1]
            ax.plot(x_vals, y_vals, color='green', label='Fitted Line')
            ax.set_title(f'frac_noise={frac_noise}, slope={slope}, intersect={intersect}')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Execute the main function
if __name__ == '__main__':
    test_ransac()
