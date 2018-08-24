import os
import pandas as pd
path="C:/Users/Usuario/python labs"
####setting wd
os.chdir(path)
###see what is in there
wd = os.getcwd()
print(os.listdir(wd))

# Save a dictionary into a pickle file.
import pickle
favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.pkl", "wb" ) )

###importing the .pkl file

with open('save.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))	

####how to load an script from python shell:
###exec(open('C:/Users/Usuario/python labs/importing 2.py').read())

###import .xlxs files
file = 'CAP.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('univarcat')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())
#############HDF5 
# Import packages
import numpy as np
import h5py
import matplotlib.pyplot as plt
# Assign filename: file
file='/media/nicolas/C28C49658C4954D7/Users/Usuario/python labs/ligotoy.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

# Get the HDF5 group: group
group=data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain =data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()