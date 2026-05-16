import pandas as pd
import numpy as np

# --- STEP 1: LOADING THE DATA ---
# We tell Python to open your Excel file
print("Opening the Excel file...")
df = pd.read_excel("01_Sales Dataset.xlsx")

# We clean up the column names so there are no weird spaces or hidden characters
df.columns = df.columns.str.strip().str.replace('\n', ' ', regex=False)

# We make sure the computer knows the "Order Date" is actually a date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# --- STEP 2: DOING THE MATH (RFM) ---
# We find the 'Snapshot Date' (Imagine this is today)
snapshot_date = df['Order Date'].max() + pd.Timedelta(days=1)

print("Calculating scores for each customer...")
# We group by Customer Name to find:
# 1. Recency: How many days since their last visit?
# 2. Frequency: How many total orders did they make?
# 3. Monetary: How much total money did they spend?
rfm = df.groupby('CustomerName').agg({
    'Order Date': lambda x: (snapshot_date - x.max()).days,
    'Order ID': 'nunique',
    'Amount': 'sum'
}).reset_index()

# Rename the columns so they are easy to read
rfm.columns = ['CustomerName', 'Recency', 'Frequency', 'Monetary']

# --- STEP 3: GIVING GRADES (1 to 5 Stars) ---
# We use 'qcut' to split customers into 5 equal-sized groups
# For Recency: Smaller number is better, so '5' goes to the newest visitors
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])

# For Frequency: Bigger number is better (we use .rank to handle people with same visit counts)
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

# For Monetary: Bigger amount is better
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# --- STEP 4: GIVING NICKNAMES (SEGMENTATION) ---
# We use a standard marketing rulebook to name the groups based on R and F scores
segment_map = {
    r'[1-2][1-2]': 'Hibernating (Gone)',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Lose Them',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}

# We combine the R and F score into a string and replace it with the nickname
rfm['Segment'] = (rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str)).replace(segment_map, regex=True)

# --- STEP 5: SAVING THE RESULTS ---
# We save this as a new Excel file that you will use in Power BI
print("Saving the results...")
rfm.to_excel("Final_Customer_Segmentation.xlsx", index=False)

# Let's see a little preview of our work!
print("\n--- PROJECT PREVIEW ---")
print(rfm[['CustomerName', 'Segment', 'Monetary']].head(10))
print("\nSuccess! Your file 'Final_Customer_Segmentation.xlsx' is ready for Power BI.")
