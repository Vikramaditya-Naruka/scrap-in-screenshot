#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pytesseract pillow reportlab


# In[13]:


import pdfplumber
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# Function to create a PDF from extracted text
def create_pdf_from_text(text, pdf_path):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Split the extracted text into lines and add them to the PDF
    lines = text.split('\n')
    for line in lines:
        p = Paragraph(line, styles["Normal"])
        story.append(p)

    doc.build(story)

# Input image path and PDF output path
image_path = 'ss.jpeg'  # Replace with the path to your screenshot image
pdf_path = 'out.pdf'  # Replace with the desired PDF output path

# Extract text from the image
extracted_text = extract_text_from_image(image_path)

# Create a PDF from the extracted text
create_pdf_from_text(extracted_text, pdf_path)

print(f"Text extracted from {image_path} and saved as {pdf_path}")


# In[15]:


import os
import pdfplumber
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# Function to create a PDF from extracted text
def create_pdf_from_text(text, pdf_path):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Adjust the lineSpacing and leading parameters for better spacing
    styles['Normal'].leading = 12  # Adjust this value as needed
    styles['Normal'].spaceAfter = 6  # Adjust as needed

    story = []

    # Split the extracted text into lines and add them to the PDF
    lines = text.split('\n')
    for line in lines:
        p = Paragraph(line, styles["Normal"])
        story.append(p)

    doc.build(story)

# Directory containing screenshot images
screenshot_directory = 'C:\\Users\\welcome\\Downloads\\screenshot'  # Replace with the path to your directory
pdf_output_path = 'output.pdf'  # Replace with the desired PDF output path

# Initialize an empty string to store all extracted text
all_extracted_text = ""

# Iterate through each image file in the directory
for filename in os.listdir(screenshot_directory):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(screenshot_directory, filename)
        extracted_text = extract_text_from_image(image_path)
        all_extracted_text += extracted_text + "\n"

# Create a PDF from all the extracted text
create_pdf_from_text(all_extracted_text, pdf_output_path)

print(f"Text extracted from all screenshots in '{screenshot_directory}' and saved as {pdf_output_path}")


# In[ ]:




