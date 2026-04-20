import csv
import argparse
import os

def clean_row(row):
    return [item.strip().lower() for item in row]

def process_file(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}")
        return

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                cleaned = clean_row(row)
                writer.writerow(cleaned)

        print(f"Processed file saved to {output_file}")

    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    parser = argparse.ArgumentParser(description="CSV File Processing Utility")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output CSV file"
    )

    args = parser.parse_args()

    process_file(args.input, args.output)

if __name__ == "__main__":
    main()
