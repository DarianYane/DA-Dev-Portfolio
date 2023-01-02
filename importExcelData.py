# This file is for importing food data from an excel file.

import pandas as pd

# Lee el archivo Excel y guarda los datos en un DataFrame
df = pd.read_excel('nutriplan/alimentos2.xlsx')
print(df)

from nutriplan.models import Alimentos

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
  # Create an instance of the model with the row data
  obj = Alimentos(nombre=row['nombre'], categoria=row['categoria'])
  # Save the instance in the database
  obj.save()