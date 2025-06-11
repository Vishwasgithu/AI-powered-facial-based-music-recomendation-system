# 🎵 AI-Powered Facial Expression Based Music Recommendation System

> Detect facial expressions in real-time and automatically play songs from YouTube that match your emotion.

---

## 👨‍💻 About the Project

This is an Artificial Intelligence-based project that recommends music based on the user’s facial expressions. It captures real-time webcam feed, detects the current emotion using deep learning, and then plays a matching song from YouTube — all automatically.

> It's like a mood-based DJ that changes the song when your face/emotion changes!

---

## 🧠 How It Works

1. 📸 Captures real-time video from your webcam
2. 😄 Detects your **dominant facial emotion** using `DeepFace`
3. 🎶 Maps that emotion to a music genre (e.g., happy → pop songs)
4. 🔍 Searches YouTube for a matching song using `youtubesearchpython`
5. 🌐 Automatically opens the top result in your browser and plays it
6. 🔁 When your emotion changes, it plays a new song

---

## 😍 Emotion to Music Genre Mapping

| Emotion   | Music Genre            |
|-----------|------------------------|
| happy     | party pop songs        |
| sad       | lofi chill songs       |
| angry     | rock music             |
| surprise  | EDM hits               |
| fear      | soothing music         |
| disgust   | classical or jazz      |
| neutral   | relaxing instrumental  |

---

## 🧰 Tech Stack

- Python 3.x
- OpenCV (`cv2`) – Webcam capture
- DeepFace – Emotion detection
- YouTubeSearchPython – Get top song video
- webbrowser – To play video in browser

---

## 📦 Installation
Install all dependencies:
pip install -r requirements.txt

# How to Run
 # bash
python main.py

📁 AI-powered-facial-based-music-recomendation-system
├── main.py               # Main emotion detection + music player
├── README.md             # Project documentation
├── requirements.txt      # Python libraries list
└── .gitignore

---

## 👨‍🎓 About Me

**Vishwas Choudhary**  
🎓 B.Tech 2nd Year – Artificial Intelligence & Data Science  
⚡ I love building cool AI projects  
📚 Always learning, improving, and experimenting  
🎤🏏 Hobbies: Singing and playing Cricket

---

## 🧠 Future Improvements

Here are some exciting ideas I have to take this project further:

- 🖥️ Build a user interface using **Streamlit**
- 🌐 Host the project online (web app version)
- 🧾 Track and show user's **emotion history**
- 🧠 Use CNN models for **more accurate emotion detection**

---

## ⭐ Support This Project

If you liked this project, please consider giving it a ⭐ on GitHub —  
it motivates me to build more such cool stuff! 🙌

Feel free to raise issues, give suggestions, or contribute via pull requests.

---





1. Clone the repository:
   ```bash
   git clone https://github.com/Vishwasgithu/AI-powered-facial-based-music-recomendation-system.git
   cd AI-powered-facial-based-music-recomendation-system
