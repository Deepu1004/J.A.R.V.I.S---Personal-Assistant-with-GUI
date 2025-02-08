# ** J.A.R.V.I.S - Voice & Chat Assistant**  

A **Python-based voice and chat assistant** using **PyQt5 for GUI**, **Pyttsx3 for text-to-speech**, and **SpeechRecognition for voice input**. This assistant supports both voice and text commands, providing a seamless interactive experience.  

## **Features** 🚀  

✅ **Voice & Chat Mode** – Supports both **voice** and **text-based commands** for flexibility.  
✅ **Activation & Deactivation** – Activate or deactivate the assistant with a button or voice command.  
✅ **News & Weather Updates** – Get the latest news and real-time weather updates.  
✅ **YouTube Playback** – Play videos directly via voice command.  
✅ **Web Navigation** – Open popular websites like Google, YouTube, and Wikipedia.  
✅ **File & Music Search** – Search local files and play your favorite songs.  
✅ **Joke Generator** – Get random jokes for entertainment.  
✅ **Interactive GUI** – A simple and clean **PyQt5**-based graphical interface.  

## **Installation**  

### **Prerequisites**  
Ensure you have **Python 3.x** installed on your system.  

### **Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **Required APIs**  
To enable **weather** and **news** functionality, replace the placeholders in `utils.py` with your API keys:  
- **OpenWeatherMap API** → `self.weather_api_key`  
- **NewsAPI** → `self.news_api_key`  

## **Usage**  

1. **Run the assistant**  
```sh
python main.py
```
2. Click the **Activate** button or type in the text input box.  
3. Use voice or text commands such as:  
   - 🗣️ **"What's the weather in London?"**  
   - 🎵 **"Play Coldplay on YouTube."**  
   - 😂 **"Tell me a joke."**  
   - 🌐 **"Open Wikipedia."**  
   - 🔇 **"Deactivate"** (to turn off voice mode).  

## **Project Structure**  
```
📂 VoiceAssistant
├── main.py         # Main application with GUI logic
├── ui.py           # PyQt5-based user interface
├── utils.py        # Core assistant functionalities
├── requirements.txt # Dependencies
└── README.md       # Project documentation
```

## **Customization**  
Extend the assistant by adding more commands in `utils.py` under `process_command()`.  

## **Contributing**  
Feel free to **fork this project** and submit **pull requests** for improvements.  

