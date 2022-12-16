

def main():
    sum_of_calories_per_elf = 0
    top_three_elfs = []
    total = 0
    
    with open("input.txt", "r") as file:
      lines = file.readlines()
      for line in lines:
        if line == '\n':
            if len(top_three_elfs) < 3:
                top_three_elfs.append(sum_of_calories_per_elf)
            elif sum_of_calories_per_elf > min(top_three_elfs):
                top_three_elfs.remove(min(top_three_elfs))
                top_three_elfs.append(sum_of_calories_per_elf)
            sum_of_calories_per_elf = 0
        else:
            sum_of_calories_per_elf += int(line)
    for value in top_three_elfs:
        total += value

    print(total)

if __name__=="__main__":
    main()
