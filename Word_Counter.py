import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

# Try to import PdfReader from PyPDF2 library for PDF support
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None
    print("Warning: PyPDF2 library is not installed. PDF support is disabled.")

# Try to import Document from python-docx library for DOCX support
try:
    from docx import Document
except ImportError:
    Document = None
    print("Warning: python-docx library is not installed. DOCX support is disabled.")

# Function to count the number of words in a given text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count the number of characters in a given text
def count_characters(text):
    return len(text)

# Function to count the number of sentences in a given text
def count_sentences(text):
    sentences = text.split('.')
    return len(sentences) - 1

# Function to count the number of paragraphs in a given text
def count_paragraphs(text):
    paragraphs = text.split('\n')
    return len([p for p in paragraphs if p.strip()])

# Function to get the most common words in a given text
def get_word_frequencies(text):
    words = text.split()
    return Counter(words).most_common(5)

# Function to read the content of a file and return it as a string
def count_words_from_file(filename):
    try:
        # Handle .txt files
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                content = file.read()
        # Handle .pdf files if PdfReader is available
        elif filename.endswith('.pdf') and PdfReader:
            reader = PdfReader(filename)
            content = ''.join([page.extract_text() for page in reader.pages])
        # Handle .docx files if Document is available
        elif filename.endswith('.docx') and Document:
            doc = Document(filename)
            content = '\n'.join([para.text for para in doc.paragraphs])
        else:
            messagebox.showerror("Error", f"Unsupported file type or required library not installed: '{filename}'")
            return None
        return content
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{filename}' was not found.")
        return None

# Function to handle the file button click event
def on_file_button_click():
    # Open a file dialog to select a file
    filename = filedialog.askopenfilename(
        title="Select a Text File", 
        filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf"), ("Word Files", "*.docx")]
    )
    if filename:
        content = count_words_from_file(filename)
        if content is not None:
            # Perform text analysis on the content
            word_count = count_words(content)
            char_count = count_characters(content)
            sentence_count = count_sentences(content)
            paragraph_count = count_paragraphs(content)
            word_freqs = get_word_frequencies(content)
            # Show the analysis results in a message box
            messagebox.showinfo(
                "Text Analysis",
                f"Word count: {word_count}\n"
                f"Character count: {char_count}\n"
                f"Sentence count: {sentence_count}\n"
                f"Paragraph count: {paragraph_count}\n"
                f"Most common words: {word_freqs}"
            )

# Function to handle the text button click event
def on_text_button_click():
    # Get the text from the text entry widget
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "You entered an empty string. Please enter some text.")
    else:
        # Perform text analysis on the entered text
        word_count = count_words(text)
        char_count = count_characters(text)
        sentence_count = count_sentences(text)
        paragraph_count = count_paragraphs(text)
        word_freqs = get_word_frequencies(text)
        # Show the analysis results in a message box
        messagebox.showinfo(
            "Text Analysis",
            f"Word count: {word_count}\n"
            f"Character count: {char_count}\n"
            f"Sentence count: {sentence_count}\n"
            f"Paragraph count: {paragraph_count}\n"
            f"Most common words: {word_freqs}"
        )

# Function to handle the exit button click event
def on_exit_button_click():
    messagebox.showinfo("Goodbye", "Thank you for using Word Counter. Goodbye!")
    root.quit()

# Creating the main application window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x400")

# Adding widgets to the window
title_label = tk.Label(root, text="Word Counter Application", font=("Helvetica", 16))
title_label.pack(pady=10)

file_button = tk.Button(root, text="Count Words from File", command=on_file_button_click, width=30, height=2)
file_button.pack(pady=10)

text_label = tk.Label(root, text="Or enter text below:", font=("Helvetica", 12))
text_label.pack(pady=5)

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=5)

text_button = tk.Button(root, text="Count Words from Text", command=on_text_button_click, width=30, height=2)
text_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=on_exit_button_click, width=30, height=2)
exit_button.pack(pady=10)

# Running the application
root.mainloop()
