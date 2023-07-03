import openai, os, dirtyjson
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from blueprint_module import blueprint

# Load env variables from .env
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("API_KEY")

# Create application server
app = Flask(__name__)

# Register blueprint from blueprint_module
app.register_blueprint(blueprint)

# Allow external domains to access JSON data
CORS(app)


@app.route("/")
def index():
    return "hi!!!!"
