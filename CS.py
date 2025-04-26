import os
import sys

def find_and_extract_code(root_dir, output_filename="code_summary.txt"):
    """
    Recursively finds all files in a directory and its subdirectories,
    extracts their content, and writes it to a summary text file.

    Args:
        root_dir (str): The path to the root directory to start searching from.
        output_filename (str): The name of the text file to generate.
    """
    # --- Input Validation ---
    if not os.path.isdir(root_dir):
        print(f"Error: The provided path '{root_dir}' is not a valid directory.")
        sys.exit(1) # Exit the script if the path is invalid

    # --- Initialization ---
    all_file_data = []
    file_counter = 0
    separator = "\n" * 11 # 10 line breaks means 11 newline characters

    print(f"Starting search in: {root_dir}")
    print(f"Output will be saved to: {output_filename}")

    # --- Recursive Traversal ---
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Optional: Skip certain directories if needed (e.g., .git, node_modules)
        # dirnames[:] = [d for d in dirnames if d not in ['.git', 'node_modules', '__pycache__']]

        for filename in filenames:
            file_counter += 1
            full_path = os.path.join(dirpath, filename)

            # Calculate relative path
            try:
                relative_path = os.path.relpath(full_path, root_dir)
                # Normalize path separators for consistency (optional but good practice)
                relative_path = relative_path.replace(os.path.sep, '/')
            except ValueError as e:
                print(f"Warning: Could not determine relative path for {full_path} (maybe on different drives?): {e}")
                relative_path = full_path # Fallback to full path if relative fails

            print(f"  Processing file {file_counter}: {relative_path}")

            # --- Read File Content ---
            file_content = ""
            try:
                # Open with utf-8 encoding, ignore errors for binary/non-standard files
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    file_content = f.read()
            except IOError as e:
                file_content = f"[Error reading file: {e}]"
                print(f"    -> Error reading file: {relative_path} - {e}")
            except Exception as e: # Catch other potential errors
                file_content = f"[Unexpected error reading file: {e}]"
                print(f"    -> Unexpected error reading file: {relative_path} - {e}")


            # --- Format Output for this file ---
            # Using a slightly more readable format with ``` block,
            # adjust if you strictly need CODE:"..."
            # file_entry = f"File {file_counter}: path= {relative_path}\nCODE:\"{file_content}\"" # Original request format
            file_entry = f"File {file_counter}: path= {relative_path}\n\nCODE:\n```\n{file_content}\n```" # More readable format

            all_file_data.append(file_entry)

    # --- Write to Output File ---
    if not all_file_data:
        print("No files found in the specified directory.")
        return

    print(f"\nFound {len(all_file_data)} files. Writing to {output_filename}...")
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            # Join all entries with the specified separator
            outfile.write(separator.join(all_file_data))
        print(f"Successfully created {output_filename}")
    except IOError as e:
        print(f"Error: Could not write to output file '{output_filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing the file: {e}")


# --- Main Execution ---
if __name__ == "__main__":
    input_path = input("Enter the directory path to scan: ")
    output_file = input("Enter the desired name for the output file (e.g., code_summary.txt): ")

    # Basic validation for output filename (optional)
    if not output_file:
        output_file = "code_summary.txt"
    elif not output_file.lower().endswith('.txt'):
         output_file += ".txt" # Ensure it has a .txt extension

    find_and_extract_code(input_path, output_file)
