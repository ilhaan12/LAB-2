# Part 3: Student dataclass
# ITEC 2905-80 - Lab 2

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float  # Added GPA field

def main():
    # Create example students
    s1 = Student("Ilhaan Mohamed", 15560595, 3.8)
    s2 = Student("Ayan Abdi", 45734265, 3.4)
    s3 = Student("Sahra Sheikh", 12685097, 3.9)

    # Verify reading fields
    print(f"{s1.name} has ID {s1.college_id} with GPA {s1.gpa}")
    print(f"{s2.name} has ID {s2.college_id} with GPA {s2.gpa}")
    print(f"{s3.name} has ID {s3.college_id} with GPA {s3.gpa}")

    # Printing a dataclass automatically includes all fields
    print(s1)


if __name__ == "__main__":
    main()

# --- Notes comparing dataclass vs traditional class ---
# Traditional classes (like Author) require writing __init__ and __str__ manually.
# Dataclasses (like Student) auto-generate these methods, which saves time.
# Dataclasses are best when storing structured data (like name, ID, GPA).
