
def parsing(location: str) -> list[str]:
    
    input_data = []
    
    with open(location, "r") as file:
        for line in file:
            input_data.append(line)
            
    return input_data


def part_one(input: list[str], word: str) -> int:

    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    word_length = len(word)
    rows, columns = len(input), len(input[0])
    count = 0
    
    for r in range(rows):
        for c in range(columns):
            
            if input[r][c] == word[0]:
                for dr, dc in neighbors:
                    if all(valid_index(r+i*dr, c+i*dc, rows, columns)
                           and input[r+i*dr][c+i*dc] == word[i] for i in range(1, word_length)):
                        count += 1
    
    return count


def part_two(input: list[str]) -> int:
    
    word = "MAS"
    neighbors = [(-1, -1), (-1, 1)]
    rows, columns = len(input), len(input[0])
    count = 0
    
    for r in range(rows):
        for c in range(columns):
        
            if input[r][c] == word[1]:
                valid_diagonals = 0
                
                for dr, dc in neighbors:
                    letters = set(['S', 'M'])
                    
                    if valid_index(r+dr, c+dc, rows, columns) and input[r+dr][c+dc] in letters:
                        letters.remove(input[r+dr][c+dc])
                        
                        if valid_index(r-dr, c-dc, rows, columns) and input[r-dr][c-dc] in letters:
                            valid_diagonals += 1
                            
                if valid_diagonals == 2:
                    count+=1
    
    return count
                            
                                   
def valid_index(row_index: int, col_index: int, rows: int, columns: int) -> bool:
    return 0 <= row_index < rows and 0 <= col_index < columns  

    
if __name__ == '__main__':
    
    input_xmas = parsing("day4/input.txt")
    count_xmas = part_one(input_xmas, "XMAS")
    count_x_mas = part_two(input_xmas)
    
    print(f'XMAS occurs a total of {count_xmas} times.')
    print(f'X-MAS occurs a total of {count_x_mas} times.')
    