import os
import sys
from datetime import datetime

def get_filename():
    while True:
        filename = input("\nEnter the filename to read: ").strip()
        if not filename:
            print("Please enter a filename.")
            continue
        return filename

def read_file_safely(filename):
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check if it's actually a file
        if not os.path.isfile(filename):
            raise IsADirectoryError(f"'{filename}' is a directory, not a file")
        
        # Check file permissions
        if not os.access(filename, os.R_OK):
            raise PermissionError(f"No read permission for '{filename}'")
        
        # Read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Successfully read {len(content)} characters from '{filename}'")
            return content
            
    except FileNotFoundError as e:
        print(f"File Error: {e}")
        return None
    except PermissionError as e:
        print(f"Permission Error: {e}")
        return None
    except IsADirectoryError as e:
        print(f"Directory Error: {e}")
        return None
    except UnicodeDecodeError as e:
        print(f"Encoding Error: Cannot read file - {e}")
        print(" Try a different encoding or check if it's a binary file")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

def modify_content(content):
    if not content:
        return content
    
    print("\nSelect modification type:")
    print("1. Add line numbers")
    print("2. Convert to uppercase")
    print("3. Add timestamp header")
    print("4. Reverse lines")
    print("5. Count words and add summary")
    
    while True:
        try:
            choice = int(input("Enter choice (1-5): "))
            if choice in range(1, 6):
                break
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")
    
    lines = content.split('\n')
    
    if choice == 1:
        # Add line numbers
        modified = '\n'.join(f"{i+1:3d}: {line}" for i, line in enumerate(lines))
        print("Added line numbers")
        
    elif choice == 2:
        # Convert to uppercase
        modified = content.upper()
        print("Converted to uppercase")
        
    elif choice == 3:
        # Add timestamp header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"=== File processed on {timestamp} ===\n\n"
        modified = header + content
        print("Added timestamp header")
        
    elif choice == 4:
        # Reverse lines
        modified = '\n'.join(reversed(lines))
        print("Reversed line order")
        
    elif choice == 5:
        words = content.split()
        summary = f"=== SUMMARY ===\n"
        summary += f"Lines: {len(lines)}\n"
        summary += f"Words: {len(words)}\n"
        summary += f"Characters: {len(content)}\n"
        summary += f"=== END SUMMARY ===\n\n"
        modified = summary + content
        print("Added word count summary")
    
    return modified

def write_file_safely(content, original_filename):
    name, ext = os.path.splitext(original_filename)
    output_filename = f"{name}_modified{ext}"
    
    if os.path.exists(output_filename):
        response = input(f"⚠️  '{output_filename}' already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            output_filename = input("Enter new filename: ").strip()
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully wrote modified content to '{output_filename}'")
        print(f"File size: {len(content)} characters")
        return True
        
    except PermissionError:
        print(f"Permission denied: Cannot write to '{output_filename}'")
        return False
    except OSError as e:
        print(f"OS Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error while writing: {e}")
        return False



def main():
    print("FILE READ & WRITE CHALLENGE")
    print("================================")
    print("This program reads a file, modifies it, and writes to a new file.")
    
    while True:
        print("\nOptions:")
        print("1. Process a file")
        print("2. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-2): "))
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if choice == 1:
            filename = get_filename()
            
            content = read_file_safely(filename)
            if content is None:
                continue
            
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"\nFile preview:\n{'-'*40}")
            print(preview)
            print("-" * 40)
            
            modified_content = modify_content(content)
            
            if write_file_safely(modified_content, filename):
                print("🎉 File processing completed successfully!")
            
        elif choice == 2:
            print("Goodbye!")
            break
            
        else:
            print("Please enter 1 or 2")

try:
    main()
except KeyboardInterrupt:
    print("\n\n Program interrupted by user. Goodbye!")
    sys.exit(0)
except Exception as e:
    print(f"\nFatal error: {e}")
    sys.exit(1)