import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import sys

def extract_table(file_path, output_csv):
    # Determine the file type based on the extension
    file_type = file_path.split('.')[-1]

    # Read the file content
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()

    # Parse the content based on the file type
    if file_type == 'xml':
        soup = BeautifulSoup(content, 'xml')
    else:
        soup = BeautifulSoup(content, 'html.parser')

    # Locate the table
    table = soup.find('table', {'id': 'scrollable'})

    # Convert the table to a DataFrame using StringIO to handle deprecation warning
    df = pd.read_html(StringIO(str(table)))[0]

    # Print the columns to understand the structure
    print("Columns in the DataFrame:", df.columns)

    # Define the column names
    columns = [
        'كد درس', 'نام درس', 'نوع درس', 'تعداد واحد نظري', 'تعداد واحد عملي', 
        'كد ارائه کلاس درس', 'نام كلاس درس', 'زمانبندي تشکيل کلاس', 'استاد', 
        'ساير اساتيد', 'حداكثر ظرفيت', 'تعداد ثبت نامي تاکنون', 'زمان امتحان', 
        'مكان برگزاري', 'مقطع ارائه درس', 'نوع ارائه', 'سطح ارائه', 
        'دانشجويان مجاز به اخذ کلاس', 'گروه آموزشی', 'دانشکده', 'واحد'
    ]

    # Assign the column names to the DataFrame if the number of columns match
    if len(df.columns) == len(columns):
        df.columns = columns
    else:
        print(f"Expected {len(columns)} columns, but found {len(df.columns)} columns in the DataFrame.")

    # Save the DataFrame as a CSV file with utf-8-sig encoding
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')

    print(f"Table has been saved to '{output_csv}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_table.py <input_file> <output_csv>")
    else:
        input_file = sys.argv[1]
        output_csv = sys.argv[2]
        extract_table(input_file, output_csv)
