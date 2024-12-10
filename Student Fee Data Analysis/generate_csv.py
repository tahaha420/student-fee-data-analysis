import pandas as pd
from datetime import datetime, timedelta
import random

def generate_csv_files():
    # List of sample Muslim names
    male_names = ["Ahmed", "Ali", "Omar", "Hassan", "Zaid", "Yusuf", "Salman", "Farhan", "Ibrahim", "Hamza"]
    female_names = ["Aisha", "Fatima", "Zainab", "Maryam", "Khadija", "Hafsa", "Amina", "Sana", "Noor", "Iqra"]

    # Generate data for students.csv
    num_students = 100
    students_data = {
        "student_id": [i + 1 for i in range(num_students)],
        "name": [
            random.choice(male_names) if random.choice([True, False]) else random.choice(female_names)
            for _ in range(num_students)
        ],
        "roll_number": [f"RN{random.randint(10000, 99999)}" for _ in range(num_students)],
        "semester": [random.randint(1, 8) for _ in range(num_students)],
    }

    students_df = pd.DataFrame(students_data)
    students_df.to_csv("students.csv", index=False)

    # Generate data for fees.csv
    num_fees = 200
    fees_data = {
        "student_id": [random.randint(1, num_students) for _ in range(num_fees)],
        "semester": [random.randint(1, 8) for _ in range(num_fees)],
        "fee_amount": [random.randint(5000, 20000) for _ in range(num_fees)],
        "fee_submission_date": [
            (datetime(2022, 1, 1) + timedelta(days=random.randint(0, 365 * 2))).strftime("%Y-%m-%d")
            for _ in range(num_fees)
        ],
    }

    fees_df = pd.DataFrame(fees_data)
    fees_df.to_csv("fees.csv", index=False)

    print("CSV files generated: students.csv and fees.csv")

if __name__ == "__main__":
    generate_csv_files()
