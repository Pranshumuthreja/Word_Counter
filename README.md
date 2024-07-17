Word Counter Application
A simple yet powerful Word Counter application built using Python and Tkinter. This application allows users to perform text analysis on both text entered manually and text from various file formats including .txt, .pdf, and .docx.
Features:
Count Words: Get the total number of words in the text.
Count Characters: Determine the number of characters in the text.
Count Sentences: Calculate the number of sentences in the text.
Count Paragraphs: Find out the number of paragraphs in the text.
Most Common Words: Display the top 5 most frequently used words in the text.

Supported File Formats:
Text Files (.txt)
PDF Files (.pdf) (Requires PyPDF2 library)
Word Files (.docx) (Requires python-docx library)

How it Works
File Analysis: The application reads the content of the selected file, processes it, and performs text analysis to display word count, character count, sentence count, paragraph count, and the most common words.
Manual Text Entry: Users can also enter text manually into the provided text area. The application then performs the same text analysis as with files.
