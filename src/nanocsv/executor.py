import csv
from src.nanocsv.commands import AddRow, RemoveRow, SearchRow

def execute_commands(commands, file_path):
    # Read existing CSV data
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        if not data:
            raise ValueError("CSV file is empty.")
        headers = data[0]
        rows = data[1:]

    for command in commands:
        if isinstance(command, AddRow):
            if len(command.values) != len(headers):
                raise ValueError("Value count does not match header count.")
            rows.append(command.values)
        elif isinstance(command, RemoveRow):
            index = command.row_number - 1  # this is just adjusted for zero-based index
            if 0 <= index < len(rows):
                rows.pop(index)
            else:
                raise IndexError("Row number out of range.")
        elif isinstance(command, SearchRow):
            results = [headers]
            for row in rows:
                match = all(
                    row[headers.index(col)] == val
                    for col, val in command.conditions.items()
                    if col in headers
                )
                if match:
                    results.append(row)
            print("Search Results:")
            for result in results:
                print(', '.join(result))
        else:
            raise TypeError("Unknown command type.")

    # Write updated data back to CSV
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
