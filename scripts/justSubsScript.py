import os
import re
from charset_normalizer import detect


# Function to process a .txt file and extract movie quotes
def extract_movie_quotes(file_path):
    with open(file_path, 'rb') as text_file:
        content = text_file.read()

    movie_quotes = []
    current_quote = []

    for line in content.splitlines():
        encoding = detect(line)['encoding']
        if encoding is None:
            encoding = 'utf-8'  # Use 'utf-8' for lines with unknown encoding
        line = line.decode(encoding, errors='ignore').strip()

        # Remove timestamps (e.g., "00:00:06,000 --> 00:00:12,074")
        if re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', line):
            continue

        # Remove HTML tags
        line = re.sub(r'<[^>]+>', '', line)

        # Remove numbering within curly braces (e.g., "{25}{175}")
        line = re.sub(r'\{\d+\}', '', line)

        # Remove numbering (e.g., "1", "2")
        if re.match(r'^\d+$', line):
            continue

        if line:
            current_quote.append(line)

    if current_quote:
        movie_quotes.append('\n'.join(current_quote))

    return '\n'.join(movie_quotes)


# Function to process files in directories
def process_directories(root_folder):
    processed_files = set()

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            print(file)
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)

                # Check if the file has already been processed
                if file_path in processed_files:
                    continue

                movie_quotes = extract_movie_quotes(file_path)

                # Create a new folder for extracted files
                extracted_folder = os.path.join('extractedSubs', os.path.basename(root))
                os.makedirs(extracted_folder, exist_ok=True)

                # Create a new file in the extracted folder
                output_file_path = os.path.join(extracted_folder, os.path.splitext(file)[0] + '_extracted.txt')
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(movie_quotes)

                # Add the processed file to the set
                processed_files.add(file_path)


# Specify the root folder to start the search
root_folder = 'subsNoDupes'

# Call the function to process directories
process_directories(root_folder)
