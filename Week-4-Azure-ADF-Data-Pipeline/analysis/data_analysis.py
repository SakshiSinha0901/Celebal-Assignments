import pandas as pd
import os

dataset_path = "../dataset/Sample_Superstore.csv"

if not os.path.exists(dataset_path):
    print("Dataset not found. Please check the file path.")
    exit()

df = pd.read_csv(dataset_path, encoding="latin1")

print("===== DATASET BASIC INFORMATION =====")
print("Rows and Columns:", df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== NUMERICAL SUMMARY =====")
print(df.describe())

print("\n===== CATEGORY SUMMARY =====")
if "Category" in df.columns:
    print(df["Category"].value_counts())

print("\n===== REGION SUMMARY =====")
if "Region" in df.columns:
    print(df["Region"].value_counts())

print("\n===== SALES AND PROFIT SUMMARY =====")
if "Sales" in df.columns and "Profit" in df.columns:
    print("Total Sales:", df["Sales"].sum())
    print("Total Profit:", df["Profit"].sum())
    print("Average Sales:", df["Sales"].mean())
    print("Average Profit:", df["Profit"].mean())

print("\nDataset analysis completed successfully.")