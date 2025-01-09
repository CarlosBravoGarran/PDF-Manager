# PDF Processor

A Python-based tool with a graphical user interface (GUI) for performing operations on PDF files such as removing pages, splitting into multiple files, and merging multiple PDFs. The program supports intuitive inputs and provides automatic naming for output files.
## Features

1. **Remove Pages**
   - Remove specific pages from a PDF.
   - Page numbering starts from 1.

2. **Split PDF**
   - Split a PDF into multiple files based on page ranges.
   - Allows specifying ranges and selecting output directories.

3. **Merge PDFs**
   - Merge multiple PDF files into a single PDF.
   - Supports browsing files for merging and selecting an output directory.

## Prerequisites

Make sure you have Python installed on your system. Additionally, ensure that `tkinter` is installed to support the graphical user interface (GUI). On most systems, `tkinter` comes pre-installed. If not, install it using your system's package manager (e.g., `sudo apt-get install python3-tk` on Ubuntu/Debian).

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:
   ```bash
   git clone git@github.com:CarlosBravoGarran/PDF-Processor.git      # SSH
   cd PDF-Processor
   ```
   ```bash
   git clone https://github.com/CarlosBravoGarran/PDF-Processor.git  # HTTPS
   cd PDF-Processor
   ```

2. Run the program:
   ```bash
   python PDF_Processor.py
   ```

3. Follow the on-screen GUI:
   - **Remove Pages**: Browse a PDF file, specify pages to remove, and select an output directory.
   - **Split PDF**: Browse a PDF file, specify ranges to split, and select an output directory.
   - **Merge PDFs**: Browse two PDF files to merge, and select an output directory.

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
- Specify the ranges for splitting (e.g., `1-3,4-5`).

Example:
```
Ranges to split: 1-3,4-end
```

### Merge PDFs
- Browse two PDF files to merge.

## Output

- Output files are saved in the specified directory with auto-generated names based on the operation performed and the input file name.
  - For removal: `<original_name>_removed_pages.pdf`
  - For splitting: `<original_name>_<range>.pdf`
  - For merging: `merged_file.pdf`
