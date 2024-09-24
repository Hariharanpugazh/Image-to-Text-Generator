import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import google.generativeai as genai
import requests

# Set up Google Gemini API (using environment variable for security)
API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')  # Ensure you have set this environment variable
if not API_KEY:
    messagebox.showerror("API Key Error", "Google Gemini API Key is missing!")

genai.configure(api_key=API_KEY)

# Configure the model generation settings
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image to Text Generator")

        # Widgets for the GUI
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.process_button = tk.Button(root, text="Generate Text", command=self.process_image)
        self.process_button.pack(pady=10)

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack(pady=10)

        self.image_path = None

    def upload_image(self):
        # Open a file dialog to select an image file
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((250, 250))
            photo = ImageTk.PhotoImage(image)

            if hasattr(self, 'image_label'):
                self.image_label.config(image=photo)
                self.image_label.image = photo
            else:
                self.image_label = tk.Label(self.root, image=photo)
                self.image_label.photo = photo
                self.image_label.pack(pady=10)

    def upload_to_gemini(self, path, mime_type=None):
        """Uploads the image file to Google Gemini."""
        try:
            file = genai.upload_file(path, mime_type=mime_type)
            return file
        except Exception as e:
            messagebox.showerror("Upload Error", f"Failed to upload image: {e}")
            return None

    def process_image(self):
        # Check if the user uploaded an image
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first.")
            return

        try:
            # Upload the image to Gemini
            file = self.upload_to_gemini(self.image_path, mime_type="image/jpeg")
            if not file:
                return

            # Start a chat session with the image
            chat_session = model.start_chat(
                history=[{"role": "user", "parts": [file]}]
            )

            # Send a message to the chat with the image context
            response = chat_session.send_message("Generate text from this image.")
            
            # Display the response in the text box
            self.text_output.delete(1.0, tk.END)  # Clear previous text
            self.text_output.insert(tk.END, response.text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
