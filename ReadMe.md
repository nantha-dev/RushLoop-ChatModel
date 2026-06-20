# Simple Chat Model

A full-stack chat application that integrates advanced AI models for both text and image generation.

## Features

- **Text Chat:** Powered by the **Llama 3 70B** model via the [Groq API](https://groq.com/).
- **Image Generation:** Powered by the **FLUX.1-schnell** model via the [Hugging Face Inference API](https://huggingface.co/docs/api-inference/index).
- **Frontend:** Built with React and Vite.
- **Backend:** Built with Python and Flask.

## Prerequisites

- Node.js (v18 or higher recommended)
- Python 3.8+
- API Keys:
  - [Groq API Key](https://console.groq.com/keys)
  - [Hugging Face Access Token](https://huggingface.co/settings/tokens)

## Setup Instructions

### 1. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install the required Python packages:
   ```bash
   pip install flask flask-cors requests groq python-dotenv
   ```
4. Configure Environment Variables:
   Create a `.env` file in the `backend` directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   ```
5. Run the Flask development server:
   ```bash
   python app.py
   ```
   The backend will run on `http://127.0.0.1:5000`.

### 2. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the Vite development server:
   ```bash
   npm run dev
   ```
   The frontend will typically be accessible at `http://localhost:5173`.

## Usage

Once both the backend and frontend servers are running, open your browser and navigate to the frontend URL. You can type messages to interact with the Llama 3 language model, and prompt it to generate images utilizing the Flux model via Hugging Face.
