# Chocolate Sales Data Project

## Overview
This project analyzes a chocolate sales dataset using Python and pandas in a Jupyter Notebook.

The goal of the project was to clean the dataset and combine it with another dataset that provides region information for each country.

## Data Sources
Main dataset:
Chocolate Sales dataset (Kaggle)

Second dataset:
Country and Region dataset used to add regional information.

## Project Structure

data/
contains the additional dataset used for the join

clean_data/
contains the cleaned dataset generated from the analysis

scripts/
contains Python scripts used to process and join the data

results/
stores the merged output dataset

## Data Processing

First, the chocolate sales data was cleaned and saved as a new dataset.

Then a second dataset was joined using the Country column.

A left merge was used so that all sales records remain in the dataset.

If a country does not exist in the region dataset, the Region column will show NA.

## Conclusion

This project demonstrates how datasets can be cleaned, organized, and merged using pandas while maintaining a clean project structure in GitHub.
