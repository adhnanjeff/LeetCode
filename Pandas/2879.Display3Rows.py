# Import pandas package 
import pandas as pd 
	
# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
		'Age':[27, 24, 22, 32], 
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
		'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
	
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
	
# select top three rows 
print(df.loc[1:3]) 
print(df.head(3)) 
# select bottom three rows

print(df.tail(3)) 
