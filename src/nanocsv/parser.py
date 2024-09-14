from src.nanocsv.commands import AddRow, RemoveRow, SearchRow
from src.nanocsv.tokenizer import TokenType

def parse(tokens):
    commands = []
    i = 0
    while i < len(tokens):
        token, value = tokens[i]

        if token == TokenType.ADD and i + 1 < len(tokens) and tokens[i+1][0] == TokenType.ROW:
            i += 2
            values = []
            while i <= len(tokens):
                if tokens[i][0] == TokenType.VALUE or tokens[i][0] == TokenType.NUMBER:
                    values.append(tokens[i][1])
                    i += 1
                    if i < len(tokens) and tokens[i][0] == TokenType.COMMA:
                        i += 1
                    else:
                        break
                else:
                    break

            commands.append(AddRow(values))
        elif token == TokenType.REMOVE and i + 1 < len(tokens) and tokens[i+1][0] == TokenType.ROW:
            i += 2
            if i < len(tokens) and tokens[i][0] == TokenType.NUMBER:
                row_number = int(tokens[i][1])
                commands.append(RemoveRow(row_number))
                i += 1
            else:
                raise SyntaxError("Expected row number after 'remove row'")
        elif token == 'SEARCH' and i + 1 < len(tokens) and tokens[i+1][0] == 'ROW':

            i += 2
            conditions = {}
            while i < len(tokens):
                if tokens[i][0] == TokenType.VALUE:
                    key, value = tokens[i][0], tokens[i][1]
                    conditions[key] = value
                    i += 1
                else:
                    break
            commands.append(SearchRow(conditions))
        else:
            raise SyntaxError(f"Unknown command starting with '{value}'")
    return commands
