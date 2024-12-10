import pandas as pd
from collections import Counter

def load_data():
    """
    Load data from CSV files into Pandas DataFrames.
    """
    students_df = pd.read_csv("students.csv")
    fees_df = pd.read_csv("fees.csv")
    return students_df, fees_df

def find_most_common_date(fees_df):
    """
    Finds the most common fee submission date and its frequency from the fees DataFrame.
    """
    # Calculate the frequency of each fee submission date
    date_frequency = Counter(fees_df["fee_submission_date"])
    
    # Get the most common date and its count
    most_common_date, frequency = date_frequency.most_common(1)[0]
    return most_common_date, frequency

def process_data(students_df, fees_df):
    """
    Merges students and fees data to find relevant dates for each student.
    """
    # Merge students and fees data on student_id
    merged_df = pd.merge(students_df, fees_df, on="student_id", how="inner")
    
    # Extract the relevant fee submission dates
    relevant_dates = merged_df["fee_submission_date"].tolist()
    
    # Return the relevant dates and the merged DataFrame for additional analysis
    return relevant_dates, merged_df

if __name__ == "__main__":
    # Load data
    students_df, fees_df = load_data()
    
    # Process data
    relevant_dates, merged_df = process_data(students_df, fees_df)
    
    # Find the most common fee submission date
    most_common_date, frequency = find_most_common_date(fees_df)
    
    print(f"The most common fee submission date is {most_common_date} with {frequency} occurrences.")
