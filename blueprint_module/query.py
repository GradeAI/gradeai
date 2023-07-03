import openai, dirtyjson
from flask import request, jsonify
from . import blueprint
from blueprint_module import blueprint


# OpenAI Prompt Parameters
AI_ROLE = """You are GradeAI, a replacement for teachers in a High School, located in North America.
You are a trained expert on writing and literary analysis. Your job is to accurately and effectively grade a student's essay and give them helpful feedback according to the assignment prompt."""

SYSTEM_INSTRUCTIONS = """Assess the student's assignment based on the provided rubric.
Respond back with graded points and a level for each criteria. Don't rewrite the rubric in order to save processing power. In the end, write short feedback about what steps they might take to improve on their assignment. Write a total percentage grade and letter grade. In your overall response, try to be lenient and keep in mind that the student is still learning. While grading the essay remember the writing level the student is at while considering their course level, grade level, and the overall expectations of writing should be producing.
Your grade should only be below 70% if the essay does not succeed at all in any of the criteria. Your grade should only be below 80% if the essay is not sufficient in most of the criteria. Your grade should only be below 90% if there are a few criteria where the essay doesn't excell. Your grade should only be above 90% if the essay succeeds in most of the criteria.
Understand that the essay was written by a human and think about their writing expectations for their grade level/course level, be lenient and give the student the benefit of the doubt.

Give me your entire response in JSON format for easy processing.
Response Format:
[{"Criteria": "...", "Level": "4", "Feedback": "Student must..."}, {"Grade": "B", "Percentage": "85%"}, {"Feedback": "Some suggestions to improve..."}] where you create a Criteria object for each individual criteria, and Grade represents the overall assignment grade. Write out a list of bullet points regarding the specific suggestions in their essay with references to examples in the essay. as a "Feedback" key.
"""


@blueprint.route("/query_essay", methods=["POST"])
def query_essay():
    """
    POST /query_essay

    Assess a student's essay and provide graded points, levels, and feedback.
    """
    """
    Assess a student's essay and provide graded points, levels, and feedback.

    Args:
        COURSE_INFORMATION (str): Information about the course.
        RUBRIC (str): The rubric for grading the essay.
        ASSIGNMENT_INSTRUCTIONS (str): Instructions for the assignment.
        ESSAY (str): The student's essay.

    Returns:
        dict: A JSON response containing graded points, levels, feedback, and overall grade.
              The response is in the following format:
              [{"Criteria": "...", "Level": "4", "Feedback": "Student must..."}, {"Grade": "B", "Percentage": "75%"}]
              Each individual criterion is represented by a Criteria object, and the Grade represents the overall assignment grade.
    """

    data = request.get_json()

    required_parameters = [
        "course_information",
        "rubric",
        "assignment_instructions",
        "essay",
    ]

    for parameter in required_parameters:
        if parameter not in data:
            return f'"{parameter}" JSON Parameter Missing', 400

    COURSE_INFORMATION = data.get("course_information")
    RUBRIC = data.get("rubric")
    ASSIGNMENT_INSTRUCTIONS = data.get("assignment_instructions")
    ESSAY = data.get("essay")

    prompt = f"""
System Instructions:
{SYSTEM_INSTRUCTIONS}

Course Information:
{COURSE_INFORMATION}

Rubric:
{RUBRIC}

Assignment Instructions:
{ASSIGNMENT_INSTRUCTIONS}

Essay:
{ESSAY}
"""

    # Query response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": AI_ROLE,
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        top_p=0.3,
    )

    print(response)

    # Return OpenAI response in JSON format
    return jsonify(dirtyjson.loads(response["choices"][0]["message"]["content"]))
