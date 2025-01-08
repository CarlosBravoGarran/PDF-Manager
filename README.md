# PDF Processor

A Python-based tool for performing operations on PDF files such as removing pages, splitting into multiple files, and merging multiple PDFs. This program supports intuitive inputs and provides automatic naming for output files.

## Features

1. **Remove Pages**
   - Remove specific pages from a PDF.
   - Page numbering starts from 1.

2. **Split PDF**
   - Split a PDF into multiple files based on page ranges.
   - Use `end` to denote the last page if the exact number is unknown.

3. **Merge PDFs**
   - Merge multiple PDF files into a single PDF.
   - Supports input with or without spaces after commas.

## Prerequisites

Make sure you have Python installed on your system. Additionally, install the required libraries using:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/CarlosBravoGarran/PDF-Processor.git  # HTTPS
   git clone git@github.com:CarlosBravoGarran/PDF-Processor.git      # SSH
   cd PDF-Processor
   ```

2. Run the program:
   ```bash
   python PDF_Processor.py
   ```

3. Follow the on-screen menu:
   - Option 1: Remove specific pages from a PDF.
   - Option 2: Split a PDF into parts based on page ranges.
   - Option 3: Merge multiple PDFs into one.
   - Option 4: Exit the program.

## Input Format

### Remove Pages
- Provide the path to the PDF file.
- Specify the pages to remove (comma-separated, starting from 1).

Example:
```
Pages to remove: 2,4,5
```

### Split PDF
- Provide the path to the PDF file.
- Specify the ranges for splitting (e.g., `1-3,4-end`).

Example:
```
Ranges to split: 1-3,4-end
```

### Merge PDFs
- Provide the paths to the PDFs (comma-separated, with or without spaces).

Example:
```
Paths to the PDFs to merge: file1.pdf, file2.pdf
```

## Output

- Output files are saved in the specified directory with auto-generated names based on the operation performed and the input file name.
  - For removal: `<original_name>_removed_pages.pdf`
  - For splitting: `<original_name>_<range>.pdf`
  - For merging: `<base_name_of_first_file>_merged.pdf`

