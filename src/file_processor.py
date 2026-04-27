import csv
import argparse
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def clean_row(row):
    return [item.strip().lower() for item in row]

def process_file(input_file, output_file):
    if not os.path.exists(input_file):
        logging.warning(f"Input file not found: {input_file}")
        return

    try:
        with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                cleaned = clean_row(row)
                writer.writerow(cleaned)

        logging.info(f"Processed file saved to {output_file}")

    except Exception as e:
        logging.error(f"Error processing file: {e}")

def process_directory(input_dir, output_dir):
    if not os.path.exists(input_dir):
        logging.warning(f"Input directory not found: {input_dir}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".csv"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, f"cleaned_{file_name}")
            process_file(input_path, output_path)

def main():
    parser = argparse.ArgumentParser(description="CSV File Processing Utility")

    parser.add_argument("--input", help="Path to input CSV file")
    parser.add_argument("--output", help="Path to output CSV file")
    parser.add_argument("--input_dir", help="Path to input directory containing CSV files")
    parser.add_argument("--output_dir", help="Path to output directory for cleaned CSV files")

    args = parser.parse_args()

    if args.input_dir and args.output_dir:
        process_directory(args.input_dir, args.output_dir)
    elif args.input and args.output:
        process_file(args.input, args.output)
    else:
        logging.info("Usage:")
        logging.info("  Single file: python src/file_processor.py --input data.csv --output cleaned.csv")
        logging.info("  Directory:   python src/file_processor.py --input_dir raw_files --output_dir cleaned_files")

if __name__ == "__main__":
    main()
