import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Call it
load_dotenv()

# 🔹 Hardcode your Gemini API key here (temporary for dev)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# ipc_json_path = os.getenv("IPC_JSON_PATH")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.json
    # Get the 'prompt' from the request body, defaulting to a generic story if not found.
    user_prompt = data.get("prompt", "A short story") 

    # Construct the full prompt for the Gemini model.
    full_prompt = f"Write a creative, easy to understand, engaging short story about '{user_prompt}'. Make it around 300 words and use proper paragraphing with context"

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(full_prompt)
        story = response.text.strip()
        
        # Return the story with the correct 'story' key for the front end.
        return jsonify({"story": story})
    except Exception as e:
        # Handle potential errors and return an error message.
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)