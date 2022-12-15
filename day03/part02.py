
def get_priority_from_char(char):
    priority = 0
    if ord(char)>96 and ord(char)<123:
        priority = ord(char) - 96
    elif ord(char)>64 and ord(char)<91:
        priority = ord(char) - 38
    return priority

def find_group_badge(elf1, elf2, elf3):
    for char in elf1:
        if char in elf2 and char in elf3:
            return get_priority_from_char(char)
    return 0

def main():
    total = 0
    i = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        while i < len(lines) :
            total += find_group_badge(lines[i], lines[i+1], lines[i+2])
            i+=3
            
    print(f'the total score is : {total}')
 

if __name__=="__main__":
    main()
