# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:19:46 2017

@author: nicolas
"""
###type of variables in python

a=194.87171000000012
print(type(a))

desc="compound interest"
type(desc)

profitable=True
print(type(profitable))

####create lists
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas=[hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Adapt list areas
areas = ["hallway",hall,"kitchen", kit, "living room", liv,"bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

###list type
print(type(areas))

#####list of lists
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]]

# Print out house
print(house)

print(type(house))


###subsetting lists
# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[-5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area=areas[3]+areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# first 6 elements of areas
downstairs = areas[:6]

# last 4 elements of areas
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

####modify lists
# Correct the bathroom area
print(areas)
areas[-1] = 10.50 

# Change "living room" to "chill zone"
areas[-6]="chill zone"
print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1= areas+["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2=areas_1+["garage",15.45]
print(areas_1)
print(areas_2)

########basic functions
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2=int(var2)
print(type(out2))

help(max)
?max

###pasting lists with +
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full= first+second
print(full)
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

########methods
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)
# Print out the number of o's in room
print(room.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

##########importing packages
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon if 12 degrees. Store in dist.
dist = r*radians(12)

# Print out dist
print(dist)

####numpys
# Create list baseball 
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
print(np_baseball)

# Convert np_baseball to m: np_baseball_m
np_height_m=np_baseball*0.0254
# Print np_baseball_m
print(np_height_m)

########
weight=[180, 215, 210, 210, 188, 176, 209, 200]
height=[74, 74, 72, 72, 73, 69, 69, 71]

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg 
np_weight_kg=np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi=np_weight_kg/ np_height_m**2

# Print out bmi
print(bmi)

####not posible in lists
weight/height

# Create the light array
light = bmi<26

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

####not posible in lists
weight<200

#####Subsetting NumPy Arrays
# Print out the weight at index 50
print(np_weight_kg[5])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height_m[2:5])
#####
##2D NumPy Array

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)

print(np_baseball)

# Print out the 50th row of np_baseball
print(np_baseball[2,:])

# Select the entire second column of np_baseball: np_weight = 
np_weight = np_baseball[:,1]

# Print out height of 4th player
print(np_baseball[3,0])

####2D Arithmetic
baseball=[[74.0, 180.0, 22.99],
 [74.0, 215.0, 34.69],
 [72.0, 210.0, 30.78],
 [72.0, 210.0, 35.43],
 [73.0, 188.0, 35.71]]
 
updated=np.array([[  1.2303559 , -11.16224898,   1.        ],
       [  1.02614252,  16.09732309,   1.        ],
       [  1.1544228 ,   5.08167641,   1.        ],
       [  0.64427532,  -5.09538071,   1.        ],
       [  1.00590086,   2.24342718,   1.        ]])
np_baseball = np.array(baseball)

# Print out addition of np_baseball and update
print(np_baseball+updated)

# Create Numpy array: conversion
conversion=np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion )

# Print out the mean of np_height
print(np.mean(np_height_m))
print(np.median(np_height_m))

print("Median: " + str(np.median(np_height_m)))
print(np.std(np_height_m))
corr=np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print(corr)
print("Correlation: " + "\n"+str(corr))