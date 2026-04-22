# 🎤 Voice Assistant using Python

## 📌 Description

This project is a voice-controlled assistant developed using Python. It utilizes speech recognition to take user input and text-to-speech to provide responses. The assistant can perform various tasks such as telling the current time, opening websites, generating jokes, and setting alarms through voice commands.

---

## 🚀 Features

* 🎙️ Voice recognition using SpeechRecognition
* 🔊 Text-to-speech output using pyttsx3
* ⏰ Tells current time
* 🌐 Opens Google in browser
* 😂 Generates random jokes
* ⏱️ Sets alarm using voice input

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* pyjokes
* datetime
* webbrowser
* winsound

---

## ⚙️ Setup Instructions (Windows)

1. Install Python 3.11
2. Install required libraries:

   ```
   pip install pyttsx3 speechrecognition pyjokes pyaudio
   ```
3. Run the project:

   ```
   python assistant.py
   ```

---

## 🎤 How to Use

Say commands like:

* "hello"
* "time"
* "open google"
* "joke" / "something funny"
* "set alarm" → then say time (e.g., "9 30 pm")
* "exit"

---

## 📁 Project Structure

```
voice-assistant-python/
│
├── assistant.py
├── MyAlarm.py
├── README.md
├── requirements.txt
```

---

## 🧠 Future Improvements

* Natural language time understanding (e.g., "nine thirty pm")
* GUI interface
* More automation features (weather, apps control)

---

## 👨‍💻 Author

Aashish Sharma

---

## 📌 Note

The project is designed for educational purposes and demonstrates basic concepts of speech recognition and automation in Python.
