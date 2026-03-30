import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- CONFIGURATION ---
num_rows = 1000000
num_unique_patients = 120000  # Large pool for realistic repeat/churn analysis
np.random.seed(42)

# --- 1. DIM_PRODUCT (Clinical Specs & Finance Metrics) ---
# Pack_Qty: Tablets/Pens per box. Strength: Concentration per unit.
# Prod_Cost: Only for internal brand (GlucaShield).
products_data = [
    [101, 'GlucaShield', 'SGLT-2', '10 mg', 'Tablet', 30, 1, 110.0, 24.50],
    [102, 'Ozempic', 'GLP-1', '0.5 mg', 'Pen', 1, 0, 295.0, np.nan],
    [103, 'Jardiance', 'SGLT-2', '10 mg', 'Tablet', 30, 0, 142.0, np.nan],
    [104, 'Januvia', 'DPP-4', '100 mg', 'Tablet', 30, 0, 95.0, np.nan],
    [105, 'Basaglar', 'Insulin', '100 U/mL', 'KwikPen', 5, 0, 80.0, np.nan],
    [106, 'Mounjaro', 'GIP/GLP-1', '5 mg', 'Vial', 4, 0, 325.0, np.nan],
    [107, 'Farxiga', 'SGLT-2', '10 mg', 'Tablet', 30, 0, 138.0, np.nan],
    [108, 'Trulicity', 'GLP-1', '1.5 mg', 'Pen', 4, 0, 288.0, np.nan],
    [109, 'Metformin', 'Biguanide', '500 mg', 'Tablet', 60, 0, 15.0, np.nan],
    [110, 'Victoza', 'GLP-1', '6 mg/mL', 'Pen', 3, 0, 240.0, np.nan]
]

dim_product = pd.DataFrame(products_data, columns=[
    'DrugID', 'BrandName', 'Category', 'Strength', 'Unit_Type', 'Pack_Qty', 'Is_Internal', 'Unit_WAC', 'Prod_Cost'
])

# --- 2. DIM_PHARMACY (Expanded Canadian Geography) ---
provinces = {
    'ON': ['Toronto', 'Ottawa', 'Mississauga', 'Brampton', 'Hamilton', 'London', 'Markham', 'Vaughan', 'Kitchener', 'Windsor', 'Oshawa', 'Barrie'],
    'QC': ['Montreal', 'Quebec City', 'Laval', 'Gatineau', 'Longueuil', 'Sherbrooke', 'Lévis', 'Saguenay', 'Trois-Rivières', 'Terrebonne'],
    'BC': ['Vancouver', 'Surrey', 'Burnaby', 'Richmond', 'Abbotsford', 'Coquitlam', 'Kelowna', 'Langley', 'Saanich', 'Delta'],
    'AB': ['Calgary', 'Edmonton', 'Red Deer', 'Lethbridge', 'Airdrie', 'Medicine Hat', 'Grande Prairie', 'St. Albert'],
    'MB': ['Winnipeg', 'Brandon', 'Steinbach'],
    'SK': ['Saskatoon', 'Regina', 'Prince Albert'],
    'NS': ['Halifax', 'Cape Breton', 'Dartmouth'],
    'NB': ['Moncton', 'Saint John', 'Fredericton'],
    'PE': ['Charlottetown', 'Summerside'],
    'NL': ["St. John's", 'Mount Pearl']
}

pharm_list = []
for i in range(1000, 1400): # 400 Pharmacy locations
    prov = np.random.choice(list(provinces.keys()))
    city = np.random.choice(provinces[prov])
    pharm_list.append({
        'PharmacyID': i, 'City': city, 'Province': prov,
        'Address': f"{np.random.randint(10, 9999)} {np.random.choice(['Main', 'King', 'Queen', 'Maple', 'Bay', 'Dundas', 'St-Catherine'])} St"
    })
dim_geo = pd.DataFrame(pharm_list)

# --- 3. PATIENT MASTER POOL (Locked Traits) ---
# Normal distribution of birth years centered at 1965 (approx. age 60 in 2025)
birth_years = np.random.normal(1965, 12, num_unique_patients).astype(int)
patient_pool = pd.DataFrame({
    'PatientID': range(50000, 50000 + num_unique_patients),
    'Gender': np.random.choice(['M', 'F', 'Other'], num_unique_patients, p=[0.48, 0.50, 0.02]),
    'BirthYear': np.clip(birth_years, 1930, 2005) # Age range 20 to 95
})

# --- 4. FACT_SALES (1,000,000 Transactions) ---
dates = [datetime(2021, 1, 1) + timedelta(days=x) for x in range((datetime(2025, 12, 31) - datetime(2021, 1, 1)).days)]

fact_sales = pd.DataFrame({
    'SalesID': range(1, num_rows + 1),
    'Date': pd.to_datetime(np.random.choice(dates, num_rows)),
    'PatientID': np.random.choice(patient_pool['PatientID'], num_rows),
    'PharmacyID': np.random.choice(dim_geo['PharmacyID'], num_rows),
    'DrugID': np.random.choice(dim_product['DrugID'], num_rows, p=[0.25, 0.20, 0.12, 0.10, 0.08, 0.10, 0.05, 0.05, 0.03, 0.02]),
    'Units_Sold': np.random.randint(1, 4, num_rows), # Number of Boxes/Packs
    'Payment_Method': np.random.choice(['Private Insurance', 'Government Plan', 'Self-Pay', 'Co-Pay'], num_rows, p=[0.50, 0.30, 0.10, 0.10])
})

# Merge Patient traits & Calculate Dynamic Age
# This ensures that as the Date moves from 2021 to 2025, the Age_at_Sale increases correctly.
fact_sales = fact_sales.merge(patient_pool, on='PatientID')
fact_sales['Age_at_Sale'] = fact_sales['Date'].dt.year - fact_sales['BirthYear']

# Final Fact Table Selection
final_sales = fact_sales[['SalesID', 'Date', 'PatientID', 'Gender', 'Age_at_Sale', 'PharmacyID', 'DrugID', 'Units_Sold', 'Payment_Method']]

# --- SAVE TO CSV ---
final_sales.to_csv('Fact_Sales_Canada_2021_2025.csv', index=False)
dim_product.to_csv('Dim_Product.csv', index=False)
dim_geo.to_csv('Dim_Pharmacy_Geography.csv', index=False)

print("Files Generated: Fact_Sales_Canada_2021_2025.csv (1M Rows), Dim_Product.csv, Dim_Pharmacy_Geography.csv")