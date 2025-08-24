from pathlib import Path
import random
import time
import sys

# Define file paths
STUDENTS_FILE = Path("students.txt")
MARKS_FILE = Path("marks.txt")
RESULTS_FILE = Path("results.txt")

# --- Goodbye Wave Animation ---
def wave_goodbye():
    message = "Goodbye"
    for i in range(3):  # repeat wave 3 times
        sys.stdout.write("\r👋 " + message + "   ")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r  " + message + " 👋")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")  # new line at the end


# --- Task 1 ---
def task1_create_and_read_students():
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]
    with STUDENTS_FILE.open("w", encoding="utf-8") as f:
        f.write("\n".join(names) + "\n")

    with STUDENTS_FILE.open("r", encoding="utf-8") as f:
        content = f.read()
        print("\nTask 1 - students.txt:\n")
        print(content)
    print("✅ Task 1 completed successfully!\n")


# --- Task 2 ---
def task2_add_marks():
    marks = [random.randint(60, 100) for _ in range(5)]
    with MARKS_FILE.open("w", encoding="utf-8") as f:
        f.write("\n".join(map(str, marks)) + "\n")

    with MARKS_FILE.open("r", encoding="utf-8") as f:
        content = f.read()
        print("\nTask 2 - marks.txt:\n")
        print(content)
    print("✅ Task 2 completed successfully!\n")


# --- Task 3 ---
def task3_display_results():
    try:
        with STUDENTS_FILE.open("r", encoding="utf-8") as f:
            names = f.read().splitlines()
        with MARKS_FILE.open("r", encoding="utf-8") as f:
            marks = list(map(int, f.read().splitlines()))

        results = [f"{name} - {mark}" for name, mark in zip(names, marks)]

        with RESULTS_FILE.open("w", encoding="utf-8") as f:
            f.write("\n".join(results) + "\n")

        print("\nTask 3 - results.txt:\n")
        for r in results:
            print(r)
        print("✅ Task 3 completed successfully!\n")

    except FileNotFoundError as e:
        print(f"⚠️ Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# --- Task 4 ---
def task4_exception_demo():
    try:
        with open("non_existent_file.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("\nTask 4 - Exception Handling Demo:")
        print("⚠️ File not found! Handled gracefully.")
    print("✅ Task 4 completed successfully!\n")


# --- Menu ---
def menu():
    while True:
        print("======= FILE & EXCEPTION HANDLING ASSIGNMENT =======")
        print("1. Task 1 - Create and Read Students")
        print("2. Task 2 - Add Marks")
        print("3. Task 3 - Display Results")
        print("4. Task 4 - Exception Handling Demo")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task1_create_and_read_students()
        elif choice == "2":
            task2_add_marks()
        elif choice == "3":
            task3_display_results()
        elif choice == "4":
            task4_exception_demo()
        elif choice == "5":
            print("Exiting program...")
            wave_goodbye()
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# Run Program
if __name__ == "__main__":
    menu()
