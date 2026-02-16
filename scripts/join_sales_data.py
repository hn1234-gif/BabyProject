import pandas as pd
sales = pd.read_csv("../clean_data/chocolate_clean.csv")

regions = pd.read_csv("../data/country_regions.csv")

merged = pd.merge(sales, regions, how="left", on="Country")

merged.to_csv("../results/chocolate_with_regions.csv", index=False)

print("Join complete")
