from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from groq import Groq
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY", "")

# Initialize Groq client if key exists
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

@app.route('/api/chat', methods=['POST'])
def chat():
    if not groq_client:
        return jsonify({"error": "Groq API Key is not set in backend. Please set GROQ_API_KEY environment variable."}), 500
        
    data = request.json
    messages = data.get("messages", [])
    
    # We use llama3-70b-8192 as requested
    try:
        completion = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        response_text = completion.choices[0].message.content
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate-image', methods=['POST'])
def generate_image():
    if not HUGGINGFACE_API_KEY:
        return jsonify({"error": "Hugging Face API Key is not set in backend. Please set HUGGINGFACE_API_KEY environment variable."}), 500
        
    data = request.json
    prompt = data.get("prompt", "")
    
    # Hugging Face Inference API for Flux
    API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            import base64
            encoded_string = base64.b64encode(response.content).decode("utf-8")
            image_url = f"data:image/jpeg;base64,{encoded_string}"
            return jsonify({"image_url": image_url})
        else:
            return jsonify({"error": f"Failed to generate image: {response.text}"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
