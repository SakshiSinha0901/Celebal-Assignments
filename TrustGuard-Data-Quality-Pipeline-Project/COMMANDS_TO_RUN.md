# Commands and Steps to Run the TrustGuard Project

This project is mainly executed on Databricks. VS Code is used to maintain the project folder, documentation, dataset, screenshots, and GitHub submission files.

## 1. Local Project Folder Path

The project folder should be placed at:

```text
C:\Celebal Assignments\Celebal-Assignments\TrustGuard-Data-Quality-Pipeline
```

## 2. Open Project in VS Code

Run these commands in PowerShell:

```powershell
cd "C:\Celebal Assignments\Celebal-Assignments\TrustGuard-Data-Quality-Pipeline"
code .
```

## 3. Dataset Location

The raw dataset should be placed at:

```text
data/raw/trustguard_retail_transactions.csv
```

## 4. Databricks Steps

### Step 1: Upload Dataset

In Databricks:

1. Click **Catalog** from the left sidebar.
2. Click **Add Data**.
3. Click **Create or Modify Table**.
4. Upload `trustguard_retail_transactions.csv`.
5. Make sure CSV header is enabled.
6. Create the table.

The uploaded table should be available as:

```text
workspace.default.trustguard_retail_transactions
```

### Step 2: Create Notebook

Create a new Databricks notebook with the name:

```text
TrustGuard_Databricks_Pipeline
```

Language:

```text
Python
```

### Step 3: Connect Compute

Attach the notebook to **Serverless** compute or any available compute.

### Step 4: Run Notebook

Run all cells from top to bottom.

The notebook will create:

- Raw Layer
- Clean Layer
- Final Layer
- Data Quality Report
- Rejected Records
- Customer Summary
- City Sales Report
- Payment Method Report
- Product Category Report
- Anomaly Log
- Pipeline Log

## 5. Export Notebook

After running successfully in Databricks:

1. Open the notebook.
2. Click **File**.
3. Click **Export**.
4. Select **IPython Notebook (.ipynb)**.
5. Save it inside the `notebooks` folder.

Final notebook path:

```text
notebooks/TrustGuard_Databricks_Pipeline.ipynb
```

## 6. Screenshots

Save Databricks screenshots inside:

```text
screenshots/
```

Recommended screenshots:

- Dataset uploaded
- Raw table output
- DQ report
- Rejected records
- Clean transactions
- Final transactions
- SQL reports
- Anomaly log
- Pipeline log
- SHOW TABLES output

## 7. GitHub Commands

Run these commands from the project folder:

```powershell
cd "C:\Celebal Assignments\Celebal-Assignments\TrustGuard-Data-Quality-Pipeline"
git status
git add .
git commit -m "Add TrustGuard Databricks data quality pipeline"
git push
```

If remote is not added, use:

```powershell
git remote add origin https://github.com/SakshiSinha0901/Celebal-Assignments.git
git branch -M main
git push -u origin main
```

If remote already exists but needs to be updated, use:

```powershell
git remote set-url origin https://github.com/SakshiSinha0901/Celebal-Assignments.git
git push -u origin main
```

## 8. Final Submission

Submit the GitHub repository link after pushing the complete project folder.
