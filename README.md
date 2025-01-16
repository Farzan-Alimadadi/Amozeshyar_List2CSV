#### Table Extractor

This repository contains a Python script that extracts tables from HTML or XML files and saves them as CSV files with specified column names. The script uses BeautifulSoup to parse the HTML or XML content and pandas to handle the table data.

#### Features:
1. **File Type Detection**: Automatically detects whether the input file is HTML or XML based on the file extension.
2. **Table Extraction**: Locates the table with the ID 'scrollable' in the HTML or XML content.
3. **DataFrame Conversion**: Converts the extracted table to a pandas DataFrame.
4. **Column Naming**: Assigns specified column names to the DataFrame if the number of columns matches.
5. **CSV Output**: Saves the DataFrame as a CSV file with UTF-8 encoding, ensuring proper handling of special characters.

#### Prerequisites:
- Python 3.x
- pandas
- BeautifulSoup4

#### Installation:
To install the required dependencies, run:
```sh
pip install pandas beautifulsoup4
```

#### Usage:
The script can be run from the command line with the following syntax:
```sh
python extract_table.py <input_file> <output_csv>
```

#### Steps to Use the Script:

1. **Select Options on the Website**:
   - Go to [https://eserv.iau.ir/EServices/pSearchAction.do](https://eserv.iau.ir/EServices/pSearchAction.do).
   - Pick the options that you wish to see on the website.

2. **Download the pSearchAction.do File**:
   - Open the web browser developer tools (usually by pressing F12 or right-clicking on the page and selecting "Inspect").
   - Go to the "Sources" tab.
   - Find and download the `pSearchAction.do` file.

3. **Use the File as Input for the Script**:
   - Save the downloaded `pSearchAction.do` file to your local machine.

4. **Run the Script**:
   - Use the downloaded file as the input for the script.
   - Specify where you want the output CSV file to be stored.
   - Example:
     ```sh
     python extract_table.py "C:\\path\\to\\pSearchAction.do" "C:\\path\\to\\output.csv"
     ```

#### Script Details:
- The script first reads the input file and detects whether it is an HTML or XML file based on the file extension.
- It then parses the content using BeautifulSoup and locates the table with the ID 'scrollable'.
- The table data is extracted and converted to a pandas DataFrame.
- If the number of columns in the table matches the specified column names, those names are assigned to the DataFrame.
- The DataFrame is saved as a CSV file with the specified output path.
- The CSV file is encoded in UTF-8 to handle special characters properly.
- If the table does not have the specified number of columns, a warning message is displayed.
- If the table is not found, an error message is displayed.
- If the output file already exists, a warning message is displayed, and the user can choose to overwrite the file.
- If the output file is successfully saved, a success message is displayed.
- If any errors occur during the process, an error message is displayed.
- The script is designed to handle various scenarios and provide informative messages to the user.
  
This script is useful for extracting and converting tabular data from HTML or XML files into a structured CSV format for further analysis or processing.

