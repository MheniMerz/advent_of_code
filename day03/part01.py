
def get_priority_from_char(char):
    priority = 0
    if ord(char)>96 and ord(char)<123:
        priority = ord(char) - 96
    elif ord(char)>64 and ord(char)<91:
        priority = ord(char) - 38
    return priority

def find_duplicate_char(compartment_1:str, compartment_2:str):
    for char in compartment_1:
        if char in compartment_2:
            return get_priority_from_char(char)
    return 0

def main():
    total = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            compartment_1 = line[:len(line)//2]
            compartment_2 = line[len(line)//2:]
            total += find_duplicate_char(compartment_1, compartment_2)
            
    print(f'the total score is : {total}')
 

if __name__=="__main__":
    main()
