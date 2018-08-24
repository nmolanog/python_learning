file=open("/media/nicolas/644E386C4E38395E/nicolas/python/python labs/moby_dick.txt",mode="r")
print(file.read())
print(file.closed)
file.close()
print(file.closed)
with open('/media/nicolas/644E386C4E38395E/nicolas/python/python labs/moby_dick.txt','r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
	
####import csv file	
import numpy as np
file = '/media/nicolas/644E386C4E38395E/nicolas/python/python labs/taller loc disp.csv'

# Load file as array: digits
###np.loadtxt requires "." as decimal separator
digits = np.loadtxt(file, delimiter=';')

# Print datatype of digits
print(type(digits))
# Print datatype of digits
print(digits)

import matplotlib.pyplot as plt
plt.scatter(digits[:,0], digits[:,1])
plt.show()

####cargar omitiendo primera fila
##y solo cols 1 y 3
###note que aqui se usa indexacion desde el 1 en filas,
###pero desde 0 en columnas
# Assign the filename: file
file = '/media/nicolas/644E386C4E38395E/nicolas/python/python labs/taller loc disp.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1,usecols=[0,2])

# Print data
print(data)

###using np.genfromtxt
file = '/media/nicolas/644E386C4E38395E/nicolas/python/python labs/Titanic.csv'
data = np.genfromtxt(file, delimiter=',', names=True, dtype=None)
np.shape(data)
data[0:4]
data['Freq']

##############
###using pandas to get dataframes
##############
# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = '/media/nicolas/644E386C4E38395E/nicolas/python/python labs/Titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
