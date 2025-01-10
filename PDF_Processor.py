import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def remove_pages_gui(pdf_path, pages_to_remove, output_dir):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()

            for i in range(len(reader.pages)):
                if i + 1 not in pages_to_remove:
                    writer.add_page(reader.pages[i])

            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            output_path = os.path.join(output_dir, f"{base_name}_removed_pages.pdf")
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

        messagebox.showinfo("Success", f"File created: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def split_pdf_gui(pdf_path, ranges, output_dir):
    try:
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

            messagebox.showinfo("Success", "PDF split successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def merge_pdfs_gui(pdf_paths, output_dir):
    try:
        writer = PyPDF2.PdfWriter()

        for pdf_path in pdf_paths:
            with open(pdf_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    writer.add_page(page)

        base_name = "merged_file"
        output_path = os.path.join(output_dir, f"{base_name}.pdf")
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        messagebox.showinfo("Success", f"File created: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file(entry_field, output_entry=None):
    file_path = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, file_path)
        if output_entry is not None:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, os.path.dirname(file_path))


def browse_directory(entry_field):
    dir_path = filedialog.askdirectory(initialdir=os.path.expanduser("~"))
    if dir_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, dir_path)

def show_menu():
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("600x450")
    root.configure(padx=20, pady=20)

    tk.Label(root, text="PDF Manager", font=("Helvetica", 16)).pack(pady=20)

    button_width = 15
    tk.Button(root, text="Remove Pages", command=show_remove_pages, width=button_width).pack(pady=10)
    tk.Button(root, text="Split PDF", command=show_split_pdf, width=button_width).pack(pady=10)
    tk.Button(root, text="Merge PDFs", command=show_merge_pdfs, width=button_width).pack(pady=10)

def show_remove_pages():
    for widget in root.winfo_children():
        widget.destroy()

    root.grid_columnconfigure(0, weight=3)
    root.grid_columnconfigure(1, weight=1)

    tk.Label(root, text="Remove Pages", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)
    
    tk.Label(root, text="PDF File:").grid(row=1, column=0, columnspan=2, sticky="w")
    pdf_entry = tk.Entry(root, width=40)
    pdf_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Browse PDF", command=lambda: browse_file(pdf_entry, output_entry), width=15).grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Pages to remove (e.g., 1,2,3):").grid(row=3, column=0, columnspan=2, sticky="w")
    pages_entry = tk.Entry(root, width=40)
    pages_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    tk.Label(root, text="Output Directory:").grid(row=5, column=0, columnspan=2, sticky="w")
    output_entry = tk.Entry(root, width=40)
    output_entry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Browse Output", command=lambda: browse_directory(output_entry), width=15).grid(row=6, column=1, padx=5, pady=5)

    def handle_remove_pages():
        pdf_path = pdf_entry.get()
        output_path = output_entry.get()
        pages_text = pages_entry.get()

        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file.")
            return
        if not output_path:
            messagebox.showerror("Error", "Please select an output directory.")
            return
        if not pages_text.strip():
            messagebox.showerror("Error", "Please specify pages to remove.")
            return

        try:
            pages_to_remove = list(map(int, pages_text.split(',')))
            remove_pages_gui(pdf_path, pages_to_remove, output_path)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid page numbers.")

    tk.Button(root, text="Remove Pages", command=handle_remove_pages, width=15).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Menu", command=show_menu, width=15).grid(row=8, column=0, columnspan=2, pady=5)

def show_split_pdf():
    for widget in root.winfo_children():
        widget.destroy()

    root.grid_columnconfigure(0, weight=3)
    root.grid_columnconfigure(1, weight=1)

    tk.Label(root, text="Split PDF", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="PDF File:").grid(row=1, column=0, columnspan=2, sticky="w")
    pdf_entry = tk.Entry(root, width=40)
    pdf_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    output_entry = tk.Entry(root, width=40)
    tk.Button(root, text="Browse PDF", command=lambda: browse_file(pdf_entry, output_entry), width=15).grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Ranges (e.g., 1-3,4-5):").grid(row=3, column=0, columnspan=2, sticky="w")
    ranges_entry = tk.Entry(root, width=40)
    ranges_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    tk.Label(root, text="Output Directory:").grid(row=5, column=0, columnspan=2, sticky="w")
    output_entry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Browse Output", command=lambda: browse_directory(output_entry), width=15).grid(row=6, column=1, padx=5, pady=5)

    def handle_split_pdf():
        pdf_path = pdf_entry.get()
        output_path = output_entry.get()
        ranges_text = ranges_entry.get()

        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file.")
            return
        if not output_path:
            messagebox.showerror("Error", "Please select an output directory.")
            return
        if not ranges_text.strip():
            messagebox.showerror("Error", "Please specify ranges to split.")
            return

        try:
            ranges = []
            for r in ranges_text.split(','):
                if '-' not in r or len(r.split('-')) != 2:
                    raise ValueError(f"Invalid range format: {r}")
                start, end = r.split('-')
                start = int(start)
                end = "end" if end.lower() == "end" else int(end)
                ranges.append((start, end))

            split_pdf_gui(pdf_path, ranges, output_path)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")


    tk.Button(root, text="Split PDF", command=handle_split_pdf, width=15).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Menu", command=show_menu, width=15).grid(row=8, column=0, columnspan=2, pady=5)

def show_merge_pdfs():
    for widget in root.winfo_children():
        widget.destroy()

    root.grid_columnconfigure(0, weight=3)
    root.grid_columnconfigure(1, weight=1)

    tk.Label(root, text="Merge PDFs", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="PDF 1:").grid(row=1, column=0, columnspan=2, sticky="w")
    pdf1_entry = tk.Entry(root, width=40)
    pdf1_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    output_entry = tk.Entry(root, width=40)
    tk.Button(root, text="Browse PDF 1", command=lambda: browse_file(pdf1_entry, output_entry), width=15).grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="PDF 2:").grid(row=3, column=0, columnspan=2, sticky="w")
    pdf2_entry = tk.Entry(root, width=40)
    pdf2_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Browse PDF 2", command=lambda: browse_file(pdf2_entry, output_entry), width=15).grid(row=4, column=1, padx=5, pady=5)

    tk.Label(root, text="Output Directory:").grid(row=5, column=0, columnspan=2, sticky="w")
    output_entry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Browse Output", command=lambda: browse_directory(output_entry), width=15).grid(row=6, column=1, padx=5, pady=5)

    def handle_merge_pdfs():
        pdf1_path = pdf1_entry.get()
        pdf2_path = pdf2_entry.get()
        output_path = output_entry.get()

        if not pdf1_path:
            messagebox.showerror("Error", "Please select the first PDF file.")
            return
        if not pdf2_path:
            messagebox.showerror("Error", "Please select the second PDF file.")
            return
        if not output_path:
            messagebox.showerror("Error", "Please select an output directory.")
            return

        merge_pdfs_gui([pdf1_path, pdf2_path], output_path)

    tk.Button(root, text="Merge PDFs", command=handle_merge_pdfs, width=15).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Menu", command=show_menu, width=15).grid(row=8, column=0, columnspan=2, pady=5)

root = tk.Tk()
root.title("PDF Manager")
show_menu()
root.mainloop()
