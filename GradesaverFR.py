def main():
    filename = "grades.txt"
    
    grades = read_grades(filename) # reads existing contents

    display_grades(grades) # displays current contents

    grades = modify_grades(grades)  # modifies the contents

    write_grades(filename, grades) # write/updates the contents

def read_grades(filename):
    grades = {} # starts an empty dictionary (array?)
    try:
        with open(filename, "r") as file:
            for line in file: # for loop: iterates over each line 
                subject, grades_str = line.strip().split(": ") # splits the line into subject and grades
                grades[subject] = grades_str.split() # list for grades? aswell as split for each grade
    except FileNotFoundError:
        print("File not founmd. Starting with an empty grade list") 
    return grades

def display_grades(grades):
    if not grades:
        print("No grades found.")
    else:
        print("Current grades:")
        for subject, grades_list in grades.items():
            print(f"{subject}: {' '.join(grades_list)}") # prints subject + grades 

def modify_grades(grades):
    while True:
        subject = input("Enter the subject(or 'done' to finish): ").strip()
        if subject.lower() == 'done': # stops the loop 
            break
        grades_str = input(f"Enter the grades for {subject} seperated by spaces: ").strip()
        grades[subject] = grades_str.split()
    return grades

def write_grades(filename, grades):
    with open(filename, 'w') as file:
        for subject, grades_list in grades.items():
            file.write(f"{subject}: {' '.join(grades_list)}\n")

if __name__ == "__main__":
    main()