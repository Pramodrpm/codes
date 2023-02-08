import PyPDF2
import docx

def pdf_to_word(pdf_file, word_file):
    # Open the pdf file
    pdf_file = open(pdf_file, 'rb')

    # Create a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Create a docx object
    doc = docx.Document()

    # Loop through each page of the pdf
    for page in range(pdf_reader.numPages):
        # Extract the text from the page
        text = pdf_reader.getPage(page).extractText()

        # Add the text to the docx document
        doc.add_paragraph(text)

    # Save the docx file
    doc.save(word_file)

    # Close the pdf file
    pdf_file.close()

pdf_file = 'input.pdf'
word_file = 'output.docx'
pdf_to_word(pdf_file, word_file)