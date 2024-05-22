# FinTech ETL Project

This project is a FinTech ETL (Extract, Transform, Load) pipeline that processes financial data from two files (`holdings.txt` and `securityData.txt`). It calculates the total market value and sector weights, writing the results to `responses.txt`.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [File Descriptions](#file-descriptions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Results](#results)

## Overview

This ETL pipeline reads data from two input files, processes the data to calculate the market value and sector weights, and writes the results to an output file. The project is designed to demonstrate data processing capabilities and financial calculations.

## Features

- **Data Extraction:** Reads financial data from `holdings.txt` and `securityData.txt`.
- **Data Transformation:** Calculates total market value and sector weights.
- **Data Loading:** Writes results to `responses.txt` with timestamps.

## File Descriptions

- **holdings.txt:** Contains stock ticker symbols, quantities, and associated values.
- **securityData.txt:** Contains stock ticker symbols, company names, sectors, and stock prices.
- **main.py:** Main script that performs the ETL process.
- **responses.txt:** Output file containing the results of the ETL process.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This project was developed using Python 3.9.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jduffey1990/fintechETL.git
   cd fintechETL
   ``` 

2. Install necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ``` 

## Usage

Run the ETL process by executing the main script:
```bash
python main.py
``` 

This will read the input files, process the data, and write the results to `responses.txt`.

## Results

The `responses.txt` file will contain output messages like the following:
```text
The Market Value Calculation has given us total market value of $XXXX.XX at MM-DD-YYYY HH:MM:SS
The Information Technology sector has given us weight of XX.XX% at MM-DD-YYYY HH:MM:SS
The Health Care sector has given us weight of XX.XX% at MM-DD-YYYY HH:MM:SS
...
```
