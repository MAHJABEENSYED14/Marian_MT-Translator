# Marian_MT-Translator
A web-based AI translator built with Flask and Hugging Face Transformers. It auto-detects the language of user input and translates it into the target language (default: English) using MarianMT models. Features a simple, backend for real-time text translation.

## Features
- Automatic language detection using `langdetect`
- High-quality translations with MarianMT models
- Interactive web interface for instant translation
- API endpoints for programmatic use
- CPU-compatible deployment in Docker

## Tech Stack
- Python, Flask
- PyTorch, Hugging Face Transformers (MarianMT)
- Docker for containerized deployment

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

2. Build the Docker image:
    ```bash
    docker build -t translator_ui .

3. Run the Docker container:
    ```bash
    docker run -p 5006:5006 translator_ui
   
5. Open your browser and go to:
    http://localhost:5006/

## Usage
# Web Interface
* Type or paste text into the input field
* The app auto-detects the language
* The translated text appears instantly in the output field

## API Endpoint
 * POST /translate with JSON payload:
{
  "text": "Bonjour",
  "src_lang": "fr",
  "tgt_lang": "en"
}

**Example response:**
{
  "src_lang": "fr",
  "tgt_lang": "en",
  "translation": "Hello"
}
If src_lang is not provided, the language is automatically detected.

## Future Improvements
 * Support additional target languages
 * Add text filtering or profanity detection
 * Integrate chat completion or other NLP features
 * Enhance frontend UI/UX for mobile devices
