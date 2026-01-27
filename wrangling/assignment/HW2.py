import pandas as pd
import numpy as np

# 1st question
# Load data
df = pd.read_csv("c:/Users/tiany/Desktop/DS3001/DS3001-SP2/wrangling/assignment/data/airbnb_hw.csv")

# Inspect the raw Price column
print(df['Price'].head())

# Clean the Price column
df['Price_clean'] = (
    df['Price']
    .astype(str)           # ensure string
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)

# Convert to numeric, coercing errors to NaN
df['Price_clean'] = pd.to_numeric(df['Price_clean'], errors='coerce')

# Count missing values
missing_count = df['Price_clean'].isna().sum()

print(f"Number of missing values in cleaned Price column: {missing_count}")

# 2nd question
# Load data
df2 = pd.read_csv("c:/Users/tiany/Desktop/DS3001/DS3001-SP2/wrangling/assignment/data/mn_police_use_of_force.csv")

# Clean empty strings 
df2["subject_injury"] = df2["subject_injury"].replace("", pd.NA) 

# Proportion missing 
prop_missing = df2["subject_injury"].isna().mean()
print(f"Proportion of missing values in subject_injury column: {prop_missing}")
print(pd.crosstab(df2["force_type"], df2["subject_injury"], dropna=False))

#3rd question

df3 = pd.read_parquet("c:/Users/tiany/Desktop/DS3001/DS3001-SP2/wrangling/assignment/data/justice_data.parquet")

print(df3.head(50))


# Convert to numeric (in case some values are strings)
df3["WhetherDefendantWasReleasedPretrial"] = pd.to_numeric(
    df3["WhetherDefendantWasReleasedPretrial"], errors="coerce"
)

# Replace the dataset's missing code (9) with np.nan
df3["WhetherDefendantWasReleasedPretrial"] = df3["WhetherDefendantWasReleasedPretrial"].replace(
    {9: np.nan}
)

# Also treat blanks or impossible values as missing
df3["WhetherDefendantWasReleasedPretrial"] = df3["WhetherDefendantWasReleasedPretrial"].replace(
    {"": np.nan}
)

df3["ImposedSentenceAllChargeInContactEvent"] = (
    df3["ImposedSentenceAllChargeInContactEvent"]
    .replace("", np.nan)
    .replace(" ", np.nan)
)

df3["ImposedSentenceAllChargeInContactEvent"] = pd.to_numeric(
    df3["ImposedSentenceAllChargeInContactEvent"], errors="coerce"
)

mask_no_sentence = df3["SentenceTypeAllChargesAtConvictionInContactEvent"].isin([9, 99])

df3.loc[mask_no_sentence, "ImposedSentenceAllChargeInContactEvent"] = np.nan
