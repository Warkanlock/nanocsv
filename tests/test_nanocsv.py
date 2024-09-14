import unittest
import os
import sys
import csv
from nanocsv.tokenizer import tokenize
from nanocsv.parser import parse
from nanocsv.executor import execute_commands

class TestNanoCSV(unittest.TestCase):
    def setUp(self):
        # Set up a test CSV file
        self.test_csv = 'test_demo.csv'
        with open(self.test_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'last_name', 'age'])
            writer.writerow(['Alice', 'Smith', '30'])
            writer.writerow(['Bob', 'Jones', '25'])
            writer.writerow(['Charlie', 'Brown', '35'])
    
    def tearDown(self):
        # Remove the test CSV file after each test
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
    
    def test_add_row(self):
        query = 'add row Diana, Prince, 28'
        tokens = tokenize(query)
        commands = parse(tokens)
        execute_commands(commands, self.test_csv)
        
        # Check if the row was added
        with open(self.test_csv, 'r', newline='') as f:
            reader = list(csv.reader(f))
            self.assertEqual(len(reader), 5)  # 4 rows + header
            self.assertEqual(reader[-1], 'Diana,Prince,28'.split(','))
    
    def test_remove_row(self):
        query = 'remove row 2'
        tokens = tokenize(query)
        commands = parse(tokens)
        execute_commands(commands, self.test_csv)
        
        # Check if the row was removed
        with open(self.test_csv, 'r', newline='') as f:
            reader = list(csv.reader(f))
            self.assertEqual(len(reader), 3)  # 2 rows + header
            self.assertNotIn(['Bob', 'Jones', '25'], reader)
    
    def test_search_row(self):
        query = 'search row name:Charlie'
        tokens = tokenize(query)
        commands = parse(tokens)
        
        # Capture the output of execute_commands
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        execute_commands(commands, self.test_csv)
        sys.stdout = sys.__stdout__
        
        # Check if the search results are correct
        output = captured_output.getvalue()
        self.assertIn('Charlie,Brown,35', output)
    
    def test_add_row_value_mismatch(self):
        query = 'add row Bruce, Wayne'
        tokens = tokenize(query)
        commands = parse(tokens)
        with self.assertRaises(ValueError):
            execute_commands(commands, self.test_csv)
    
    def test_remove_row_out_of_range(self):
        query = 'remove row 10'
        tokens = tokenize(query)
        commands = parse(tokens)
        with self.assertRaises(IndexError):
            execute_commands(commands, self.test_csv)
    
    def test_invalid_command(self):
        query = 'update row 1 name:Bob'
        tokens = tokenize(query)
        with self.assertRaises(SyntaxError):
            parse(tokens)
    
    def test_multiple_commands(self):
        query = 'add row Diana, Prince, 28 remove row 1 search row age:28'
        tokens = tokenize(query)
        commands = parse(tokens)
        
        # Capture the output
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        execute_commands(commands, self.test_csv)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn('Diana,Prince,28', output)
        # Check final CSV content
        with open(self.test_csv, 'r', newline='') as f:
            reader = list(csv.reader(f))
            self.assertNotIn(['Alice', 'Smith', '30'], reader)  # Removed row 1

if __name__ == '__main__':
    unittest.main()
