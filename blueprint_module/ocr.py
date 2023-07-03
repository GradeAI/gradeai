import base64, requests, os
from flask import request
from . import blueprint


def parse_text(file):
    """
    Parse text from an image using OCR.space API.

    Args:
        file: The image to extract text from.

    Returns:
        The recognized text from the image.
    """
    image = file.read()
    encoded_image = base64.b64encode(image).decode("utf-8")

    # Send the API request
    response = requests.post(
        "https://api.ocr.space/parse/image",
        headers={"apikey": os.getenv("OCR_SPACE_API_KEY")},
        data={
            "base64Image": f"data:{file.content_type};base64,{encoded_image}",
            "language": "eng",
            "isOverlayRequired": False,
        },
    )
    response_data = response.json()

    # Extract the recognized text from the API response
    text_results = []
    if "ParsedResults" in response_data:
        parsed_results = response_data["ParsedResults"]
        for result in parsed_results:
            if "ParsedText" in result:
                text_results.append(result["ParsedText"])

    return " ".join(text_results)


@blueprint.route("/image", methods=["POST"])
def image_to_text():
    """
    POST /image

    Extracts text from a single image file
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

    # heic is the defualt ios photo file
    filetypes = [".png", ".jpg", ".jpeg", ".heic"]

    # Check for invalid file type
    if not any(filename.lower().endswith(filetype) for filetype in filetypes):
        return (
            f"<h2>Invalid filetype: please attach one of {', '.join(filetypes)} file</h2>",
            400,
        )

    try:
        # Parse text using magic
        text = parse_text(file)

        print(text)

        # Return text from image file
        return str(text)

    except Exception as e:
        return f"Error reading image: {e}", 400
