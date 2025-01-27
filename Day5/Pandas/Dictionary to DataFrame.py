# Dictionary to DataFrame:
import pandas as pd

data = ({'Age': [30, 20, 22, 40, 32, 28, 39],
         'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black', 'Red'],
         'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Beans'],
         'Height': [165, 70, 120, 80, 180, 172, 150],
         'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
         'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
         })
print(data)

df = pd.DataFrame(data)

print(df)
