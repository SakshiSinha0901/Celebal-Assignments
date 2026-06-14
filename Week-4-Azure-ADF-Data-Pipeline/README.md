# Azure Cloud Fundamentals and Data Pipeline Implementation using ADF

## Overview

This assignment focuses on understanding Azure cloud fundamentals and implementing an end-to-end data pipeline using Azure Storage Account, Blob Storage, and Azure Data Factory.

The main goal of this assignment is to upload a CSV file into Azure Blob Storage, connect it with Azure Data Factory, validate the file metadata, copy the file from a source container to a destination container, and monitor the successful execution of the pipeline.

## Objective

To understand Azure cloud concepts and build a complete data pipeline using:

* Azure Portal
* Resource Group
* Azure Storage Account
* Azure Blob Storage
* Azure Data Factory
* Linked Service
* Datasets
* Get Metadata Activity
* Copy Data Activity
* IAM Role Assignment

## Dataset Used

The dataset used in this assignment is the Superstore dataset.

Dataset Source:

```txt
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
```

The CSV file was uploaded into the Azure Blob Storage `source` container and used as the input file for the Azure Data Factory pipeline.

## Folder Structure

```txt
Week-4-Azure-ADF-Data-Pipeline/
│
├── dataset/
│   └── Sample_Superstore.csv
│
├── analysis/
│   ├── data_analysis.py
│   └── dataset_analysis_summary.md
│
├── screenshots/
│   ├── 01_resource_group.png
│   ├── 02_storage_account.png
│   ├── 03_blob_container_uploaded_file.png
│   ├── 04_adf_created.png
│   ├── 05_linked_service.png
│   ├── 06_source_dataset.png
│   ├── 07_destination_dataset.png
│   ├── 08_get_metadata_activity.png
│   ├── 09_pipeline_design.png
│   ├── 10_pipeline_debug_succeeded.png
│   ├── 11_pipeline_monitor_succeeded.png
│   ├── 12_iam_role_assignment.png
│   └── 13_destination_output_file.png
│
├── azure-commands/
│   └── azure_cli_commands.txt
│
├── summary.md
└── README.md
```

## Dataset Analysis

Before performing Azure operations, the dataset was analyzed using Python and Pandas.

The following checks were performed:

* Checked total rows and columns
* Displayed first few records
* Checked column names
* Checked data types
* Checked missing values
* Checked duplicate records
* Generated numerical summary
* Reviewed sales and profit-related fields

This helped in understanding the structure and quality of the dataset before uploading it to Azure Blob Storage.

## Azure Resources Created

The following Azure resources were created for this assignment:

| Resource              | Name                                 |
| --------------------- | ------------------------------------ |
| Resource Group        | `rg-celebal-adf-assignment`          |
| Storage Account       | `stcelebaladfsakshisinha`            |
| Source Container      | `source`                             |
| Destination Container | `destination`                        |
| Azure Data Factory    | `adf-celebal-assignment-sakshisinha` |
| Linked Service        | `LS_AzureBlobStorage`                |
| Source Dataset        | `DS_Source_Superstore_CSV`           |
| Destination Dataset   | `DS_Destination_Superstore_CSV`      |
| Pipeline              | `PL_Copy_Superstore_Blob_To_Blob`    |

## Task 1: Resource Group Creation

A Resource Group was created in Azure Portal to organize all the resources used in this assignment.

Resource Group Name:

```txt
rg-celebal-adf-assignment
```

Deliverable:

```txt
Screenshot of Resource Group
```

## Task 2: Storage Setup

A Storage Account was created inside the Resource Group.

Storage Account Name:

```txt
stcelebaladfsakshisinha
```

Inside the Storage Account, two Blob Containers were created:

```txt
source
destination
```

The Superstore CSV file was uploaded into the `source` container.

Deliverable:

```txt
Screenshot of container with uploaded CSV file
```

## Task 3: Azure Data Factory Basics

Azure Data Factory was created and ADF Studio was explored.

ADF Studio sections explored:

* Author
* Monitor
* Manage

A Linked Service was created to connect Azure Data Factory with Azure Blob Storage.

Linked Service Name:

```txt
LS_AzureBlobStorage
```

Two datasets were created:

```txt
DS_Source_Superstore_CSV
DS_Destination_Superstore_CSV
```

The source dataset points to the CSV file in the `source` container.
The destination dataset points to the output file path in the `destination` container.

Deliverables:

```txt
Screenshot of Linked Service
Screenshot of Source Dataset
Screenshot of Destination Dataset
Screenshot of Get Metadata Activity
```

## Task 4: Pipeline Development

A pipeline was created in Azure Data Factory.

Pipeline Name:

```txt
PL_Copy_Superstore_Blob_To_Blob
```

The pipeline contains two activities:

1. Get Metadata Activity
2. Copy Data Activity

The Get Metadata activity was used to validate the source file before copying.

Metadata fields used:

```txt
exists
size
itemName
lastModified
```

The Copy Data activity was used to copy the CSV file from the `source` container to the `destination` container.

Source:

```txt
source/Sample_Superstore.csv
```

Destination:

```txt
destination/copied_superstore.csv
```

Deliverable:

```txt
Screenshot of pipeline design
```

## Task 5: Pipeline Execution

The pipeline was executed using Debug/Trigger in Azure Data Factory.

After execution, the pipeline status was shown as:

```txt
Succeeded
```

The successful pipeline run was verified in the Monitor section of ADF Studio.

Deliverable:

```txt
Screenshot showing pipeline execution as Succeeded
```

## Task 6: IAM Role Assignment

IAM roles were assigned to provide required access between Azure Data Factory and Azure Storage Account.

Roles used:

* Reader
* Contributor
* Storage Blob Data Contributor

The Storage Blob Data Contributor role was assigned to the Azure Data Factory managed identity so that ADF could access Blob Storage.

Deliverable:

```txt
Screenshot of role assignment
```

## Final Pipeline Flow

```txt
Superstore CSV File
        ↓
Azure Blob Storage Source Container
        ↓
Azure Data Factory Linked Service
        ↓
Source Dataset
        ↓
Get Metadata Activity
        ↓
Copy Data Activity
        ↓
Destination Dataset
        ↓
Copied CSV File in Destination Container
```

## Output

The pipeline executed successfully.

Final copied file:

```txt
destination/copied_superstore.csv
```

The file was successfully copied from the `source` container to the `destination` container using Azure Data Factory.

## Screenshots Included

The following screenshots are included in the assignment:

* Resource Group
* Storage Account
* Blob Container with Uploaded File
* Azure Data Factory
* Linked Service
* Source Dataset
* Destination Dataset
* Get Metadata Activity
* Pipeline Design
* Pipeline Debug/Trigger Execution
* Pipeline Monitor Status
* IAM Role Assignment
* Destination Container Output File

## Conclusion

This assignment helped in understanding the basics of Azure cloud services and Azure Data Factory pipeline implementation.

Through this assignment, I learned how to create Azure resources, upload data to Blob Storage, connect Azure Data Factory with Blob Storage, create datasets, validate metadata, copy data using pipeline activities, monitor pipeline execution, and configure IAM roles.

The final pipeline was successfully executed, and the CSV file was copied from the source Blob container to the destination Blob container.
