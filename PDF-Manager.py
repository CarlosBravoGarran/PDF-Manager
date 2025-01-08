import PyPDF2
import os
import readline

def complete_path(text, state):
    """Auto-complete function for file paths."""
    line = readline.get_line_buffer()
    if not line:
        return [None][state]
    matches = [f for f in os.listdir('.') if f.startswith(text)]
    return matches[state] if state < len(matches) else None

readline.set_completer(complete_path)
readline.parse_and_bind('tab: complete')

def remove_pages(pdf_path, pages_to_remove, output_dir):
    """Removes specific pages from a PDF."""
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return

    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        for i in range(len(reader.pages)):
            if i + 1 not in pages_to_remove:  # Pages are 1-based now
                writer.add_page(reader.pages[i])

        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}_removed_pages.pdf")
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
    print(f"File created: {output_path}")

def split_pdf(pdf_path, ranges, output_dir):
    """Splits a PDF into multiple files based on given ranges."""
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return

    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        for start, end in ranges:
            writer = PyPDF2.PdfWriter()
            start_index = start - 1
            end_index = len(reader.pages) if end == "end" else int(end)

            for i in range(start_index, end_index):
                writer.add_page(reader.pages[i])

            range_str = f"{start}-{end if end != 'end' else len(reader.pages)}"
            output_path = os.path.join(output_dir, f"{base_name}_{range_str}.pdf")
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            print(f"File created: {output_path}")

def merge_pdfs(pdf_paths, output_dir):
    """Merges multiple PDF files into one."""
    writer = PyPDF2.PdfWriter()

    for pdf_path in [path.strip() for path in pdf_paths]:
        if not os.path.exists(pdf_path):
            print(f"Error: File '{pdf_path}' does not exist.")
            return

        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)

    base_name = os.path.splitext(os.path.basename(pdf_paths[0].strip()))[0]
    output_path = os.path.join(output_dir, f"{base_name}_merged.pdf")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    print(f"File created: {output_path}")

def menu():
    print("\nPDF Processor")
    print("1. Remove pages")
    print("2. Split PDF")
    print("3. Merge PDFs")
    print("4. Exit")

    option = input("Select an option: ")

    if option == '1':
        pdf_path = input("Path to the PDF: ")
        pages = input("Pages to remove (comma-separated, starting from 1): ")
        try:
            pages_to_remove = list(map(int, pages.split(',')))
            output_dir = input("Output directory: ")
            remove_pages(pdf_path, pages_to_remove, output_dir)
        except ValueError:
            print("Invalid input for pages. Please enter a comma-separated list of numbers.")

    elif option == '2':
        pdf_path = input("Path to the PDF: ")
        ranges = input("Ranges to split (e.g., 1-3,4-end): ")
        try:
            ranges = [tuple(r.split('-')) for r in ranges.split(',')]
            ranges = [(int(start), end if end == "end" else int(end)) for start, end in ranges]
            output_dir = input("Output directory: ")
            split_pdf(pdf_path, ranges, output_dir)
        except ValueError:
            print("Invalid input for ranges. Please enter ranges in the format start-end, separated by commas.")

    elif option == '3':
        pdf_paths = input("Paths to the PDFs to merge (comma-separated): ").replace(', ', ',').split(',')
        output_dir = input("Output directory: ")
        merge_pdfs(pdf_paths, output_dir)

    elif option == '4':
        print("Exiting the program...")
        exit()
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    while True:
        menu()
