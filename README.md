# Agentic AI Blog Generator

This project uses AI agents to automatically generate a blog post about **AI and cloud** computing applications.  
It saves the output as a `.html` file, ready for hosting on platforms like **AWS S3** for static website deployment.

## Features
- AI-generated blog content using OpenAI API
- Simple Python script to create clean `.html` blog pages
- Easy to extend or automate further into larger AI workflows
- Cloud-ready output for hosting

## Requirements
- Python 3.8+
- OpenAI Python SDK (`openai`)
- `python-dotenv` to manage environment variables safely

## How to Run
1. Install dependencies:
   ```bash
   pip install openai python-dotenv


2. Set your OpenAI API key as an environment variable or inside a .env file.
3. Run the project:
   ```bash
   python main.py

4. Find the generated .html in the project folder.

5. Deployment
Upload the generated .html file to AWS S3 (static website hosting) to make your blog live. 
[View sample live blog here]()


## Note
- API keys are securely hidden using environment variables and `.gitignore`.
- The S3 bucket only allows public **read** access.
