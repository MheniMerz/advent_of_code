
def contains(elf_1_start, elf_1_end, elf_2_start, elf_2_end):
    if elf_1_start <= elf_2_start and elf_2_end <= elf_1_end:
        return True
    if elf_2_start <= elf_1_start and elf_1_end <= elf_2_end:
        return True
    return False

def main():
    total = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            elfs = line.split(',')
            elf_1_start, elf_1_end = elfs[0].split('-')
            elf_2_start, elf_2_end = elfs[1].split('-')
            #need to cast the type to int because i had the wrong result when comparing strings
            elf_1_start, elf_1_end, elf_2_start, elf_2_end = [int(i) for i in [elf_1_start, elf_1_end, elf_2_start, elf_2_end]]
            if contains(elf_1_start, elf_1_end, elf_2_start, elf_2_end):
                total += 1
            
    print(f'the total score is : {total}')
 

if __name__=="__main__":
    main()
