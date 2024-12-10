import pandas as pd
from collections import Counter
from parallel_data_processing import load_data, process_data, find_most_common_date

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
