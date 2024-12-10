import pandas as pd
from collections import Counter

def load_data():
    """
    Load data from CSV files into Pandas DataFrames.
    """
    print("Loading data...")
    students_df = pd.read_csv("students.csv")
    fees_df = pd.read_csv("fees.csv")
    print("Data loaded successfully.")
    return students_df, fees_df

def process_data(students_df, fees_df):
    """
    Merges students and fees data to find relevant dates for each student.
    """
    print("Processing data...")
    # Merge students and fees data on student_id
    merged_df = pd.merge(students_df, fees_df, on="student_id", how="inner")
    
    # Extract the relevant fee submission dates
    relevant_dates = merged_df["fee_submission_date"].tolist()
    print("Data processing completed.")
    return relevant_dates, merged_df

def find_most_common_date(fees_df):
    """
    Finds the most common fee submission date and its frequency from the given DataFrame.
    """
    print("Calculating the most common fee submission date...")
    # Extract fee submission dates
    relevant_dates = fees_df["fee_submission_date"].tolist()
    
    # Calculate the frequency of each date
    date_frequency = Counter(relevant_dates)
    
    # Get the most common date and its count
    most_common_date, frequency = date_frequency.most_common(1)[0]
    print("Calculation completed.")
    return most_common_date, frequency

def main():
    try:
        # Load data from CSV files
        students_df, fees_df = load_data()

        # Process data to get relevant fee submission dates and merged DataFrame
        relevant_dates, merged_df = process_data(students_df, fees_df)

        # Calculate frequency of dates using Counter
        date_frequency = Counter(relevant_dates)

        # Find the most common fee submission date
        most_common_date, frequency = find_most_common_date(fees_df)

        # Display results
        print("\nRelevant Fee Submission Dates:", relevant_dates)
        print("\nFrequency of Relevant Fee Submission Dates:")
        for date, freq in date_frequency.items():
            print(f"{date}: {freq}")
        
        print(f"\nMost Common Fee Submission Date: {most_common_date} with {frequency} submissions.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure that the CSV files exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
