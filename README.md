# Image-to-Text Generator

## My Journey Begins Here

This project holds a special place in my heart. It represents the very beginning of my coding journey - my first ever Python project, created during my AI & Data Science studies at SNS College of Engineering.

Back then, I didn't even own a laptop. I was just a student trying to understand the world of technology, with more curiosity than knowledge. Despite the challenges, I was determined to build something meaningful. This simple image-to-text generator became my first step into the vast world of programming.

## What This Project Does

This desktop application converts images into descriptive text using Google's Gemini AI. What started as a learning experiment has become a functional tool that demonstrates the power of AI in understanding visual content.

## The Story Behind the Code

When I first wrote this code, I barely understood what APIs were or how GUI applications worked. Every line was a learning experience:

- **Tkinter GUI** - My first attempt at creating a user interface
- **Google Gemini Integration** - Learning to work with AI APIs
- **File Handling** - Understanding how to manage image uploads
- **Error Handling** - Discovering the importance of robust code

This project taught me that you don't need to be an expert to start building. Sometimes, the best way to learn is by doing.

## From This Project to My Developer Journey

This humble image-to-text generator was my first commit to GitHub. It marked the beginning of my transformation from a curious student without a laptop to someone who could actually build software. Every developer has a first project, and this is mine.

## How to Use This Project

### Requirements
- Python 3.x
- Google Gemini API key
- Required packages: `tkinter`, `Pillow`, `google-generativeai`, `requests`

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Hariharanpugazh/Image-to-Text-Generator.git
   cd Image-to-Text-Generator
   ```

2. Install dependencies:
   ```bash
   pip install Pillow google-generativeai requests
   ```

3. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. Set your API key as an environment variable:
   ```bash
   # Windows
   set GOOGLE_GEMINI_API_KEY=your_api_key_here
   
   # Linux/Mac
   export GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

### Running the Application
```bash
python visions.py
```

1. Click "Upload Image" to select your image
2. Click "Generate Text" to let AI describe your image
3. Read the generated description in the text area

## A Message to Fellow Beginners

If you're just starting out like I was, remember that every expert was once a beginner. This project might not be the most sophisticated application you'll ever see, but it represents something more important - the courage to start.

Your first project doesn't have to be perfect. It just has to be yours.

## Technical Details

Built with:
- **GUI**: Tkinter (Python's built-in GUI library)
- **AI Model**: Google Gemini 1.5 Flash
- **Image Processing**: PIL (Python Imaging Library)
- **API Integration**: Google GenerativeAI

## License

MIT License - Feel free to learn from this code and build something even better!
