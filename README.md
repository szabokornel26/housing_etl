# housing_etl
# Housing Data ETL Pipeline

## Overview
This project is an **ETL (Extract, Transform, Load) pipeline** for processing housing market data. The script reads a CSV file, performs data transformation and cleaning, and loads the processed data into a MySQL database.

## Features
- **Extract**: Reads housing data from a CSV file.
- **Transform**:
  - Converts `median_house_value` to thousands.
  - Calculates `bedrooms_per_room` ratio.
  - Removes duplicate rows.
- **Load**: Saves the transformed data into a MySQL table.

## Technologies Used
- **Python** (pandas, SQLAlchemy)
- **MySQL** (for storing processed data)

## Installation
### Prerequisites
Ensure you have Python and the required dependencies installed:
```bash
pip install pandas sqlalchemy pymysql
```

### Database Setup
Create a MySQL database (`myDB`) and configure user permissions accordingly. Update the `db_url` in `main()` to match your database credentials.

## Usage
1. Place your CSV file in the specified directory (`/Users/szabokornel/Downloads/housing.csv`).
2. Run the script:
   ```bash
   python script.py
   ```
3. The cleaned data will be loaded into the `housing` table in MySQL.

## Configuration
Modify these variables in `main()` to match your setup:
```python
file_path = '/path/to/housing.csv'
db_url = "mysql+pymysql://username:password@localhost:3306/database_name"
```

## Notes
- Ensure MySQL is running and accessible before executing the script.
- Update database credentials for security before deploying.

## License
This project is open-source and available for modification as needed.

