
# J.A.R.V.I.S - Voice & Chat Assistant 🗣️💬

J.A.R.V.I.S is a **Python-based voice and chat assistant** built with a clean **PyQt5 GUI**, **Pyttsx3** for text-to-speech, and **SpeechRecognition** for voice commands. It offers seamless voice and text interactions, making it easy to access a range of functionalities with just your voice or typing.

## 🚀 Features

- **Voice & Chat Mode** – Switch between **voice** and **text-based commands** for flexibility.
- **Activation & Deactivation** – Use a button or voice command to toggle the assistant on/off.
- **News & Weather Updates** – Get real-time **weather** and **news** updates.
- **YouTube Playback** – Play YouTube videos with just a voice command.
- **Web Navigation** – Open popular websites such as Google, YouTube, and Wikipedia.
- **File & Music Search** – Search your local files and play songs.
- **Joke Generator** – Enjoy random jokes for entertainment.
- **Interactive GUI** – Clean and intuitive user interface designed using **PyQt5**.

---

## 📦 Installation

### **Prerequisites**  

Ensure you have **Python 3.x** installed on your system.

### **Install Dependencies**  

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-repo/voice-assistant.git
cd voice-assistant
pip install -r requirements.txt
```

Certainly! Here's the updated section of the README to reflect the use of a `.env` file for API keys:

---

### **Set up Required APIs**  

To enable the **weather** and **news** functionalities, you need to configure your API keys using a `.env` file.

1. **Create a `.env` File**  
   In the root directory of the project, create a `.env` file and add your API keys in the following format:

   ```
   WEATHER_API_KEY=your_openweathermap_api_key_here
   NEWS_API_KEY=your_newsapi_key_here
   ```

2. **Install `python-dotenv`**  
   You’ll need the `python-dotenv` package to load the environment variables. To install it, run the following command:

   ```bash
   pip install python-dotenv
   ```

3. **Update `utils.py`**  
   In the `utils.py` file, make sure to import and load the environment variables like so:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the API keys securely
   weather_api_key = os.getenv('WEATHER_API_KEY')
   news_api_key = os.getenv('NEWS_API_KEY')
   ```

This way, your API keys will be securely stored in the `.env` file and can be accessed in your code without exposing them directly.

---

## 🖥️ Usage

1. **Run the Assistant**  
   To start the assistant, run the following command:

   ```bash
   python main.py
   ```

2. **Activate Voice Mode**  
   You can activate the assistant by either clicking the **Activate** button on the interface or by typing in the text input box.

3. **Using Commands**  
   Once activated, you can either speak or type your command. Some sample commands include:
   
   - 🗣️ **"What's the weather in London?"**
   - 🎵 **"Play Coldplay on YouTube."**
   - 😂 **"Tell me a joke."**
   - 🌐 **"Open Wikipedia."**
   - 🔇 **"Deactivate"** (to turn off voice mode).

---

## 🗂️ Project Structure

```
📂 VoiceAssistant
├── main.py         # Main application logic with GUI
├── ui.py           # PyQt5-based user interface design
├── utils.py        # Core assistant functionalities and commands
├── requirements.txt # Python dependencies
└── README.md       # Project documentation
```

---

## 🛠️ Customization

You can easily extend and customize the assistant by adding new commands in `utils.py` under the `process_command()` function. Modify the file to include any additional functionality you need.

---

## 🤝 Contributing

Feel free to **fork** this repository and submit **pull requests** for bug fixes, new features, or improvements.

---

## 📸 Screenshots (Optional)

If you want to make your README more engaging, consider adding a few screenshots or GIFs of the assistant in action. Here’s an example of how you can add a screenshot:

```markdown
![Assistant Screenshot](.png)
```

