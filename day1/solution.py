
# Advent of Code 2024, day 1

def parsing():
    first_list, second_list = [], []
    
    with open("day1/input.txt", "r") as file:
        for line in file:
            a, b = map(int, line.strip().split())
            
            first_list.append(a)
            second_list.append(b)
    
    return first_list, second_list
            

def part1(first_list: list[int], second_list: list[int]) -> int:
            
    first_list = sorted(first_list)
    second_list = sorted(second_list)
    
    length = len(first_list)
    total_distance = 0
    
    for i in range(length):
        diff = abs(first_list[i]-second_list[i])
        total_distance +=  diff
    
    return total_distance


def part2(first_list: list[int], second_list: list[int]) -> int:
    
    first_set = set(first_list)
    frequency_dict = {num: 0 for num in first_set}
    
    for num in second_list:
        if num in first_set:
            frequency_dict[num] += 1
            
    similarity_score = 0
    for num in first_list:
        similarity_score += num * frequency_dict[num]
        
    return similarity_score
        

a, b = parsing()
print(f'The total distance is {part1(a, b)}.')
print(f'The similarity score is {part2(a, b)}.')
