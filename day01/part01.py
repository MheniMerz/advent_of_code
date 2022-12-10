

def main():
    sum_of_calories = 0
    max_calories = 0
    
    with open("input.txt", "r") as file:
      lines = file.readlines()
      for line in lines:
        if line == '\n':
            if sum_of_calories > max_calories:
                max_calories = sum_of_calories
            sum_of_calories = 0
        else:
            sum_of_calories += int(line)
    
    print(f"The max calories is {max_calories}")

if __name__=="__main__":
    main()
