
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

# Clean data
df.dropna(inplace=True)

# Summary stats
print(df.describe())

# Plot sales by region
df.groupby('Region')['Sales'].sum().plot(kind='bar', title='Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()
