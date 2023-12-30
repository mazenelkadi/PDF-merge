from PyPDF2 import PdfMerger  # Library for PDF manipulation
import tkinter as tk  # Tkinter for creating GUI elements
from tkinter import filedialog  # Dialogs for file selection


def select_pdfs():
    """Open a dialog to select multiple PDF files."""
    root = tk.Tk()
    root.withdraw()  # Hides the small tkinter window

    # Open the file picker dialog for PDFs
    file_paths = filedialog.askopenfilenames(
        title="Select PDFs to merge",
        filetypes=[("PDF Files", "*.pdf")]
    )

    return list(file_paths)


def merge_pdfs(pdfs, output_filename):
    """Merge the selected PDFs into a single file."""
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)  # Append each PDF to the merger

    merger.write(output_filename)  # Write the merged PDF to a file
    merger.close()  # Close the PdfMerger object


def save_file_dialog():
    """Open a dialog to save the merged PDF file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        filetypes=[("PDF Files", "*.pdf")],
        defaultextension=".pdf"
    )
    return file_path


# Main execution
if __name__ == "__main__":
    selected_pdfs = select_pdfs()  # Select PDFs to merge
    if selected_pdfs:
        output_file = save_file_dialog()  # Choose where to save the merged PDF
        if output_file:
            merge_pdfs(selected_pdfs, output_file)  # Merge the PDFs
            print(f"PDFs Merged Successfully into {output_file}!")
        else:
            print("File save cancelled.")
    else:
        print("No PDFs selected.")
