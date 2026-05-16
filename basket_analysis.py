import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

print("Step 1: Loading your sales data...")
df = pd.read_excel("./01_Sales Dataset.xlsx")

# Cleaning column names
df.columns = df.columns.str.strip().str.replace('\n', ' ', regex=False)

print("Step 2: Sorting items into 'Shopping Baskets'...")
# Creating the basket
basket = (df.groupby(['Order ID', 'Sub-Category'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Order ID'))

# --- IMPROVED: Converting to True/False (Booleans) to stop all warnings ---
basket_sets = basket.astype(bool)

print("Step 3: Finding patterns (Searching for even tiny connections)...")
# We lowered 'min_support' to 0.002 to find more patterns
frequent_itemsets = apriori(basket_sets, min_support=0.002, use_colnames=True)

# Generate patterns
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Sort by strength
rules = rules.sort_values('lift', ascending=False)

# Make the item names look clean
rules['items_bought'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['likely_to_buy_next'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

print("Step 4: Saving results...")

# 1. First, we define what 'final_rules' is
final_rules = rules[['items_bought', 'likely_to_buy_next', 'support', 'confidence', 'lift']].copy()

# 2. Now we clean the text so we don't get the Unicode error
final_rules['items_bought'] = final_rules['items_bought'].apply(lambda x: str(x).encode('ascii', 'ignore').decode('ascii'))
final_rules['likely_to_buy_next'] = final_rules['likely_to_buy_next'].apply(lambda x: str(x).encode('ascii', 'ignore').decode('ascii'))

# 3. Finally, we save it using the better "pen" (openpyxl)
final_rules.to_excel("Market_Basket_Rules.xlsx", index=False, engine='openpyxl')

print("\n--- ANALYSIS COMPLETE ---")
print(f"I found {len(final_rules)} shopping patterns this time!")
print("\n--- ANALYSIS COMPLETE ---")

print("\n--- ANALYSIS COMPLETE ---")
print(f"I found {len(final_rules)} shopping patterns this time!")
print("\nTop 5 Patterns Found:")
print(final_rules[['items_bought', 'likely_to_buy_next']].head())
print("\nLook for 'Market_Basket_Rules.xlsx' in your folder.")
