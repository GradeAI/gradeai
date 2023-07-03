from PyPDF2 import PdfReader
from flask import request
from . import blueprint


@blueprint.route("/pdf", methods=["POST"])
def pdf_to_text():
    """
    POST /pdf

    Extracts text from a single PDF file
    """
    # Check if POST has file attached
    if "file" not in request.files:
        return "<h2>Missing file to the input</h2>", 400

    # Get file from request
    file = request.files["file"]
    filename = file.filename

    # Empty filename
    if filename == "":
        return "<h2>Missing filename to the input</h2>", 400

    # Check for invalid file type
    elif not filename.lower().endswith(".pdf"):
        return "<h2>Invalid filetype: please attach a pdf file</h2>", 400

    try:
        # Read the PDF file
        pdf = PdfReader(file)

        # Extract text from each page
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

        # Return text from PDF file
        return text

    except Exception as e:
        return f"Error reading PDF file: {e}", 400
