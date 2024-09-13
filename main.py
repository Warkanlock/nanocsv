import argparse
import sys

from src.nanocsv.tokenizer import tokenize
from src.nanocsv.parser import parse
from src.nanocsv.executor import execute_commands

def main():
    parser = argparse.ArgumentParser(description='Process CSV queries.')
    parser.add_argument('--file', required=True, help='Path to CSV file.')
    parser.add_argument('--query', nargs='+', required=True, help='Queries to execute.')
    args = parser.parse_args()

    queries = ' '.join(args.query)
    tokens = tokenize(queries)
    try:
        commands = parse(tokens)
    except SyntaxError as e:
        print(f"Syntax error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error during parsing: {e}")
        sys.exit(1)
    try:
        execute_commands(commands, args.file)
    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
