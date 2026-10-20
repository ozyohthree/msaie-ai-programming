import os
from pathlib import Path

def process_number_files():
    # Target current directory
    current_dir = Path('.')
    
    # Iterate through all text files
    for file_path in current_dir.glob('*.txt'):
        # Prevent infinite loops by skipping files we've already generated
        if 'processed' in file_path.name.lower():
            continue
            
        valid_numbers = []
        
        # Read the file and filter out non-numeric lines
        with open(file_path, 'r') as infile:
            for line in infile:
                clean_line = line.strip()
                if not clean_line:
                    continue
                
                try:
                    # Parse as float to handle decimals
                    num = float(clean_line)
                    # Convert back to int if it's a whole number for cleaner output
                    if num.is_integer():
                        num = int(num)
                    valid_numbers.append(num)
                except ValueError:
                    # Silently ignore lines that cannot be parsed as numbers
                    continue
        
        # Skip creating a new file if no numbers were found
        if not valid_numbers:
            continue
            
        # Sort numbers from low to high
        valid_numbers.sort()
        total_sum = sum(valid_numbers)
        
        # Construct output filename (e.g., data.txt -> data_processed.txt)
        new_filename = f"{file_path.stem}_processed{file_path.suffix}"
        
        # Write the sorted numbers and the sum to the new file
        with open(current_dir / new_filename, 'w') as outfile:
            for num in valid_numbers:
                outfile.write(f"{num}\n")
            outfile.write("---\n")
            outfile.write(f"Sum: {total_sum}\n")
            
        print(f"Processed: '{file_path.name}' -> '{new_filename}'")

if __name__ == "__main__":
    process_number_files()