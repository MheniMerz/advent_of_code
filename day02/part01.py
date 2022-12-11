

def get_score_per_choice(choice):
    if choice == "X":
        return 1
    if choice == "Y":
        return 2
    if choice == "Z":
        return 3

def rock_paper_scisors(elf_choice:str, my_choice:str):
    
    possible_resutls = {
                ("A", "X"): 3,
                ("A", "Y"): 6,
                ("A", "Z"): 0,
                
                ("B", "X"): 0,
                ("B", "Y"): 3,
                ("B", "Z"): 6,
                
                ("C", "X"): 6,
                ("C", "Y"): 0,
                ("C", "Z"): 3,
            }
    return possible_resutls[(elf_choice, my_choice)]


def main():
    total = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            plays = line.split(' ')
            plays[1] = plays[1].strip('\n')
            total += rock_paper_scisors(plays[0], plays[1])
            total += get_score_per_choice(plays[1])
    print(f'the total score is : {total}')
 

if __name__=="__main__":
    main()
