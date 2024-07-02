import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Generate 200 rows of dummy data
num_rows = 200

# Generate IP semester data between 2.0 and 4.0
ip_data = np.random.uniform(2.0, 4.0, (num_rows, 6))

# Calculate IPK as the mean of the IP semester data
ipk_data = ip_data.mean(axis=1)

# Assign 'Tepat Waktu' if IPK >= 3.0, else 'Tidak Tepat Waktu'
hasil_data = np.where(ipk_data >= 3.0, 'Tepat Waktu', 'Tidak Tepat Waktu')

# Create DataFrame
dummy_data = pd.DataFrame(
    ip_data,
    columns=[f'IP Semester {i+1}' for i in range(6)]
)
dummy_data['IPK'] = ipk_data
dummy_data['Hasil'] = hasil_data

# Save to Excel
dummy_data.to_excel('Data_Training_Dummy.xlsx', index=False)
