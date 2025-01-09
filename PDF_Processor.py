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

def browse_file(entry_field):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, file_path)

def browse_directory(entry_field):
    dir_path = filedialog.askdirectory()
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

    tk.Label(root, text="Remove Pages", font=("Helvetica", 14)).pack(pady=10)
    pdf_entry = tk.Entry(root, width=50)
    pdf_entry.pack(pady=5)
    tk.Button(root, text="Browse PDF", command=lambda: browse_file(pdf_entry), width=15).pack(pady=5)

    tk.Label(root, text="Pages to remove (e.g., 1,2,3):").pack()
    pages_entry = tk.Entry(root, width=50)
    pages_entry.pack(pady=5)

    tk.Label(root, text="Output Directory:").pack()
    output_entry = tk.Entry(root, width=50)
    output_entry.pack(pady=5)
    tk.Button(root, text="Browse Output", command=lambda: browse_directory(output_entry), width=15).pack(pady=5)

    tk.Button(root, text="Remove Pages", command=lambda: remove_pages_gui(pdf_entry.get(), list(map(int, pages_entry.get().split(','))), output_entry.get()), width=15).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=show_menu, width=15).pack(pady=5)

def show_split_pdf():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Split PDF", font=("Helvetica", 14)).pack(pady=10)
    pdf_entry = tk.Entry(root, width=50)
    pdf_entry.pack(pady=5)
    tk.Button(root, text="Browse PDF", command=lambda: browse_file(pdf_entry), width=20).pack(pady=5)

    tk.Label(root, text="Ranges (e.g., 1-3,4-5):").pack()
    ranges_entry = tk.Entry(root, width=50)
    ranges_entry.pack(pady=5)

    tk.Label(root, text="Output Directory:").pack()
    output_entry = tk.Entry(root, width=50)
    output_entry.pack(pady=5)
    tk.Button(root, text="Browse Output", command=lambda: browse_directory(output_entry), width=15).pack(pady=5)

    tk.Button(root, text="Split PDF", command=lambda: split_pdf_gui(pdf_entry.get(), [(int(r.split('-')[0]), r.split('-')[1] if 'end' in r.split('-')[1] else int(r.split('-')[1])) for r in ranges_entry.get().split(',')], output_entry.get()), width=15).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=show_menu, width=15).pack(pady=5)

def show_merge_pdfs():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Merge PDFs", font=("Helvetica", 14)).pack(pady=10)
    pdf_entry = tk.Entry(root, width=50)
    pdf_entry.pack(pady=5)
    tk.Label(root, text="Paths (comma-separated):").pack()

    output_entry = tk.Entry(root, width=50)
    output_entry.pack(pady=5)
    tk.Button(root, text="Browse Output", command=lambda: browse_directory(output_entry), width=15).pack(pady=5)

    tk.Button(root, text="Merge PDFs", command=lambda: merge_pdfs_gui(pdf_entry.get().split(','), output_entry.get()), width=15).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=show_menu, width=15).pack(pady=5)

# Main Application
root = tk.Tk()
root.title("PDF Manager")
show_menu()
root.mainloop()
