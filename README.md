# Setup Backend
To set up the backend locally, follow these steps:

Clone the repository:
```bash
git clone https://github.com/GradeAI/gradeai.git
```

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

Run the Flask application:
```bash
python app.py
```

Access the back-end in your browser at http://localhost:5000.

## **Endpoint: /image**

```rust

POST /image

Uses OCR to retrieve text from an image file

Parameters:
- file: The image file to extract text from (multipart/form-data).

Returns:
The extracted text from the PDF file.
```

**Example Request:**
```rust

POST /image
Content-Type: multipart/form-data

file: <file attachment>
```

**Example Response:**
```http

HTTP/1.1 200 OK
Content-Type: text/plain

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tristique mauris vel nibh...
```

## **Endpoint: /pdf**

```rust

POST /pdf

Extracts text from a single PDF file.

Parameters:
- file: The PDF file to extract text from (multipart/form-data).

Returns:
The extracted text from the PDF file.
```

**Example Request:**
```rust

POST /pdf
Content-Type: multipart/form-data

file: <file attachment>
```

**Example Response:**
```http

HTTP/1.1 200 OK
Content-Type: text/plain

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tristique mauris vel nibh...
```

## **Endpoint: /query_essay**
```rust
POST /query_essay

Assess a student's essay and provide graded points, levels, and feedback.

Parameters:
- course_information (str): Course name and grade.
- rubric (str): The rubric for grading the essay.
- assignment_instructions (str): Instructions for the assignment.
- essay (str): The student's essay.

Returns:
A JSON response containing graded points, levels, feedback, and overall grade. The response is in the following format:
[
    {
        "Criteria": "...",
        "Level": "4",
        "Feedback": "Student must..."
    },
    {
        "Grade": "B",
        "Percentage": "75%"
    }
]

Each individual criterion is represented by a Criteria object, and the Grade represents the overall assignment grade.
```

**Example Request:**
```json

POST /query_essay
Content-Type: application/json

{
    "course_information": "Grade 12 English AP",
    "rubric": "<table>...</table>",
    "assignment_instructions": "Write a persuasive essay on the importance of reading.",
    "essay": "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
}
```

**Example Response:**
```json

HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "Criteria": "Introduction",
        "Level": "4",
        "Feedback": "The introduction effectively engages the reader and clearly presents the main argument."
    },
    {
        "Criteria": "Organization",
        "Level": "3",
        "Feedback": "The essay is generally well-organized, but some paragraphs could be more logically structured."
    },
    ...
    {
        "Grade": "B",
        "Percentage": "75%"
    }
]
```
