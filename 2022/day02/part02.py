

def get_score_per_choice(choice):
    if choice == "X":
        return 0
    if choice == "Y":
        return 3
    if choice == "Z":
        return 6

def get_score_based_on_desired_outcome(elf_choice:str, desired_outcome:str):
    
    possible_resutls = {
                ("A", "X"): 3,
                ("A", "Y"): 1,
                ("A", "Z"): 2,
                
                ("B", "X"): 1,
                ("B", "Y"): 2,
                ("B", "Z"): 3,
                
                ("C", "X"): 2,
                ("C", "Y"): 3,
                ("C", "Z"): 1,
            }
    return possible_resutls[(elf_choice, desired_outcome)]


def main():
    total = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            plays = line.split(' ')
            plays[1] = plays[1].strip('\n')
            total += get_score_based_on_desired_outcome(plays[0], plays[1])
            total += get_score_per_choice(plays[1])
    print(f'the total score is : {total}')
 

if __name__=="__main__":
    main()
