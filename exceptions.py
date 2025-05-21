def modify_and_write_file(input_filename, output_filename):
    
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Modify the lines (example: add a line number to each line)
        modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
if __name__ == "__main__":
    while True:
        input_file = input("Enter the name of the input file: ")
        output_file = input("Enter the name of the output file: ")

        try:
            # Attempt to open the input file in read mode to check if it exists and is readable
            with open(input_file, 'r') as f:
                pass  # File exists and can be opened for reading
            break  # Exit the loop if the file is accessible
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist. Please enter a valid filename.")

    modify_and_write_file(input_file, output_file)