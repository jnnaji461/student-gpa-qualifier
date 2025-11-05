# Student: Judith Nnaji
# File: student_gpa_qualifier.py
# Description: 
# This application accepts student names and GPAs, then checks if each student
# qualifies for the Dean's List or Honor Roll. 

def main():
    print("Student GPA Qualification Checker")
    print("Enter 'ZZZ' for last name to quit.\n")
    
    while True:
        # Get student's last name
        last_name = input("Enter student's last name: ")
        
        # Check if we should quit processing
        if last_name.upper() == 'ZZZ':
            print("\nProcessing complete. Goodbye!")
            break
        
        # Get student's first name
        first_name = input("Enter student's first name: ")
        
        # Get and validate GPA
        while True:
            try:
                gpa = float(input("Enter student's GPA: "))
                if gpa < 0.0 or gpa > 4.0:
                    print("Invalid entry. GPA must be between 0.0 and 4.0.")
                    continue
                break
            except ValueError:
                print("Please enter a numeric value for GPA.")
        
        # Check qualifications and display results
        print(f"\nResults for {first_name} {last_name}:")
        
        if gpa >= 3.5:
            print("✓ This student has made the Dean's List!")
        elif gpa >= 3.25:
            print("✓ This student has made the Honor Roll!")
        else:
            print("This student does not qualify for Dean's List or Honor Roll.")
        
        print("-" * 50, "\n")

# Run the application
if __name__ == "__main__":
    main()

