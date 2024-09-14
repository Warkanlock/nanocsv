import csv
from src.nanocsv.commands import AddRow, RemoveRow, SearchRow
from src.nanocsv.msg import info_msg


def execute_commands(commands, file_path):
    # Read existing CSV data
    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)
        if not data:
            raise ValueError("CSV file is empty.")

        # extract information from file
        headers = data[0]
        rows = data[1:]

    for command in commands:
        if isinstance(command, AddRow):
            if len(command.values) != len(headers):
                raise ValueError("Value count does not match header count.")
            rows.append(command.values)
            info_msg(f"Row {len(rows)} added")
        elif isinstance(command, RemoveRow):
            index = command.row_number - 1
            if 0 <= index < len(rows):
                rows.pop(index)
                info_msg(f"Row {index} deleted")
            else:
                raise IndexError("Row number out of range.")
        elif isinstance(command, SearchRow):
            results = [headers]
            for row in rows:
                for col, full_value in command.conditions.items():
                    partial = full_value.split(":")
                    key, value = partial[0], partial[1]

                    if key is None or value is None:
                        raise ValueError("Cannot add a value that's not defined")

                    # get index of the column to be inserted
                    column_index = headers.index(key)

                    # check if value of the column match with the value per se
                    if value == row[column_index]:
                        results.append(row)

            info_msg(f"Found {len(results)} results")
            print("---")
            for result in results:
                print(",".join(result))
            print("---")
        else:
            raise TypeError("Unknown command type.")

    # Write updated data back to CSV
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
