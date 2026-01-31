from PIL import Image
# from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
#import PyPDF2

def delete_files(files) -> None:
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted {file} successfully.")
        except OSError as e:
            print(f"Error deleting {file}: {e}")

def convert_jpg_to_pdf(jpg_files, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)

    for jpg_file in jpg_files:
        try:
            img = Image.open(jpg_file)
            width, height = img.size

            # Scale the image to fit within the page size
            if width > height:
                img_width = 700  # Adjust this value as needed
                img_height = int((float(height) / width) * img_width)
            else:
                img_height = 700  # Adjust this value as needed
                img_width = int((float(width) / height) * img_height)

            c.setPageSize((img_width, img_height))
            c.drawInlineImage(jpg_file, 0, 0, width=img_width, height=img_height)

            c.showPage()
            print(f"Added {jpg_file} to PDF")

        except Exception as e:
            print(f"Error processing {jpg_file}: {str(e)}")

    c.save()
    print(f"PDF saved as {output_pdf}")
    delete_files(jpg_files)

# def create_pdf_from_jpgs(image_paths, output_pdf):
#     with open(output_pdf, "wb") as pdf_file:
#         pdf_writer = PyPDF2.PdfFileWriter()
        
#         for image_path in image_paths:
#             page = PyPDF2.PdfFileReader(image_path)
#             pdf_writer.addPage(page.getPage(0))
        
#         pdf_writer.write(pdf_file)

# Example usage:
# jpg_files = ["image1.jpg", "image2.jpg", "image3.jpg"]  # List of JPG files
jpg_files = []
for i in range (1, 135):
    jpg_files.append(f'image{i}.jpg')
output_pdf = "Oracle_19C_PL_SQL_Advanced_Activity_Guide.pdf"

convert_jpg_to_pdf(jpg_files, output_pdf)
