# File-Handling

# File Read & Write with Error Handling

A comprehensive Python program that demonstrates safe file operations with robust error handling. This program reads text files, applies various modifications, and writes the results to new files while gracefully handling common file operation errors.

## Features

### 📖 File Reading
- Safe file reading with comprehensive validation
- Checks for file existence, permissions, and file type
- Handles encoding errors for binary files
- Provides clear error messages for different failure scenarios

### ✏️ Content Modification
Choose from 5 different modification options:
1. **Add Line Numbers** - Prepends line numbers to each line
2. **Convert to Uppercase** - Transforms all text to uppercase
3. **Add Timestamp Header** - Adds a timestamp header to the file
4. **Reverse Lines** - Reverses the order of lines in the file
5. **Count Words and Add Summary** - Adds a summary with line, word, and character counts

### 💾 File Writing
- Automatically generates output filenames (adds "_modified" suffix)
- Prompts for confirmation before overwriting existing files
- Handles write permission errors
- Reports file size after successful write operations

## Error Handling

The program handles these common file operation errors:

| Error Type | Description | Example |
|------------|-------------|---------|
| `FileNotFoundError` | File doesn't exist | Entering "nonexistent.txt" |
| `PermissionError` | No read/write permissions | Protected system files |
| `IsADirectoryError` | Path points to directory | Entering a folder name |
| `UnicodeDecodeError` | Binary file read as text | Trying to read .exe or .jpg files |
| `OSError` | General OS-related errors | Disk full, invalid characters |


## Usage

### Running the Program
```bash
python file_handler.py
```

### Basic Workflow
1. **Start the program** - You'll see a menu with options
2. **Choose "Process a file"** - Enter option 1
3. **Enter filename** - Type the name of the file you want to process
4. **Preview content** - See a preview of your file content
5. **Select modification** - Choose from 5 modification options
6. **File is saved** - Modified content is written to a new file

### Example Session
```
🖋️  FILE READ & WRITE CHALLENGE
================================
This program reads a file, modifies it, and writes to a new file.

Options:
1. Process a file
2. Exit

Enter your choice (1-2): 1

Enter the filename to read: example.txt
✅ Successfully read 245 characters from 'example.txt'

📄 File preview:
----------------------------------------
Hello world!
This is a test file.
It has multiple lines.
----------------------------------------

Select modification type:
1. Add line numbers
2. Convert to uppercase
3. Add timestamp header
4. Reverse lines
5. Count words and add summary

Enter choice (1-5): 1
✨ Added line numbers
✅ Successfully wrote modified content to 'example_modified.txt'
📊 File size: 289 characters
🎉 File processing completed successfully!
```

## Error Examples

### File Not Found
```
Enter the filename to read: missing.txt
❌ File Error: File 'missing.txt' not found
```

### Permission Denied
```
Enter the filename to read: /etc/shadow
❌ Permission Error: No read permission for '/etc/shadow'
```

### Directory Instead of File
```
Enter the filename to read: Documents
❌ Directory Error: 'Documents' is a directory, not a file
```

## File Output

The program automatically generates output filenames by adding "_modified" before the file extension:

- `document.txt` → `document_modified.txt`
- `data.csv` → `data_modified.csv`
- `notes` → `notes_modified`

If the output file already exists, you'll be prompted to confirm overwriting or provide a new filename.

## Code Structure

### Functions Overview

- **`get_filename()`** - Prompts user for filename with validation
- **`read_file_safely(filename)`** - Reads file with comprehensive error handling
- **`modify_content(content)`** - Applies user-selected modifications to content
- **`write_file_safely(content, original_filename)`** - Writes modified content to new file
- **`main()`** - Main program loop with menu system

### Key Programming Concepts Demonstrated

- **Exception Handling** - Multiple try/catch blocks for different error types
- **File I/O Operations** - Safe file reading and writing with context managers
- **Input Validation** - User input validation and retry loops
- **String Manipulation** - Various text processing techniques
- **Error Reporting** - Clear, user-friendly error messages
