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
    docker build -t translator_ui .

3. Run the Docker container:
    docker run -p 5006:5006 translator_ui
   
5. Open your browser and go to:
    http://localhost:5006/
