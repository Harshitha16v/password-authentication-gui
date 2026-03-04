import pandas as pd
def load_dataset(file):
    print("Loading dataset...\n")
    df = pd.read_csv(file)
    return df
def dataset_health_report(df):
    print("----- Dataset Health Report (Before Cleaning) -----")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Missing Values:", df.isnull().sum().sum())
    print("Duplicate Rows:", df.duplicated().sum())
    print()
def clean_missing_values(df):
    missing_fixed = 0
    for col in df.columns:
        if df[col].dtype == "object":
            missing_fixed += df[col].isnull().sum()
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            missing_fixed += df[col].isnull().sum()
            df[col].fillna(df[col].mean(), inplace=True)
    return missing_fixed
def remove_duplicates(df):
    duplicates = df.duplicated().sum()
    df.drop_duplicates(inplace=True)
    return duplicates
def standardize_text(df):
    columns_fixed = 0
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.lower().str.strip()
        columns_fixed += 1
    return columns_fixed
def final_report(df, missing_fixed, duplicates_removed, columns_fixed):
    print("----- Cleaning Summary -----")
    print("Missing Values Fixed:", missing_fixed)
    print("Duplicates Removed:", duplicates_removed)
    print("Text Columns Standardized:", columns_fixed)
    health_score = 100 - (df.isnull().sum().sum())
    print("\nDataset Health Score:", health_score, "%")
    print("\n----- Dataset After Cleaning -----")
    print(df.head())
def main():
    file = "employee_data.csv"
    df = load_dataset(file)
    dataset_health_report(df)
    missing_fixed = clean_missing_values(df)
    duplicates_removed = remove_duplicates(df)
    columns_fixed = standardize_text(df)
    final_report(df, missing_fixed, duplicates_removed, columns_fixed)
if __name__ == "__main__":
    main()