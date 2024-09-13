# nanocsv

NanoCSV is a simple command-line tool that allows you to manipulate CSV files using a custom domain-specific language (DSL). It supports adding rows, removing rows, and searching for rows based on conditions.

## Features

- **Add Row**: Add a new row to the CSV file.
- **Remove Row**: Remove a row by its row number.
- **Search Row**: Search for rows matching specific conditions.

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/nanocsv.git
cd nanocsv
```

Make sure you have Python 3 installed.

## Usage

```bash
poetry run nanocssv --file <path_to_csv_file> --query "<command1>" "<command2>" ...
```

### Examples

Assuming `demo.csv` has the columns `name`, `last_name`, `age`.

#### Add a Row

```bash
poetry run nanocsv --file demo.csv --query "add row john, doe, 22"
```

#### Remove a Row

```bash
poetry run nanocsv --file demo.csv --query "remove row 1"
```

#### Search for Rows

```bash
poetry run nanocsv --file demo.csv --query "search row name:john"
```

You can combine multiple queries:

```bash
poetry run nanocsv --file demo.csv --query "add row jane, smith, 30" "search row last_name:smith"
```

## Command Syntax

### Add Row

```
add row <value1>, <value2>, ..., <valueN>
```

- Adds a new row with the specified values.
- The number of values must match the number of columns in the CSV.

### Remove Row

```
remove row <row_number>
```

- Removes the row at the specified row number (1-based index).

### Search Row

```
search row <column1>:<value1>, <column2>:<value2>, ...
```

- Searches for rows where the specified columns match the given values.
- Multiple conditions are combined using logical AND.

## Notes

- The tool modifies the CSV file in place.
- Search results are printed to the console.
- Make sure the CSV file has headers (column names) in the first row.

## Error Handling

- The tool will report syntax errors in queries.
- It will check for mismatches in the number of values when adding rows.
- It will report if a specified row number is out of range when removing rows.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please open an issue on the GitHub repository.
