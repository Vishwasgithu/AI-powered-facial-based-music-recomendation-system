import cv2
from deepface import DeepFace
from youtubesearchpython import VideosSearch
import time
import webbrowser

# Emotion to genre mapping
emotion_to_genre = {
    'happy': 'party pop songs',
    'sad': 'lofi chill songs',
    'angry': 'rock music',
    'neutral': 'relaxing instrumental',
    'surprise': 'EDM hits',
    'fear': 'soothing music',
    'disgust': 'classical or jazz music'
}

# Music recommendation function
def recommend_and_play_music(emotion):
    genre = emotion_to_genre.get(emotion, 'relaxing music')
    print(f"\n🎧 Based on your emotion ({emotion}), recommended genre: {genre}\n")

    search = VideosSearch(genre, limit=1)
    results = search.result().get('result', [])
    
    if results:
        video = results[0]
        title = video.get('title', 'No Title')
        link = video.get('link', '')
        print(f"🎵 {title}\n🔗 {link}\n")
        webbrowser.open(link)
    else:
        print("No video found.")

# Real-time emotion detection
def run_realtime_recommender():
    cap = cv2.VideoCapture(0)
    last_emotion = ""
    display_emotion = "Detecting..."
    last_time = time.time()

    print("📸 Webcam ON - Real-time Emotion Music Recommender")
    print("Press 'q' to quit anytime.")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Show emotion on screen even if not updated
        cv2.putText(frame, f"Emotion: {display_emotion}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Detect every 5 seconds
        if time.time() - last_time > 5:
            try:
                analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = analysis[0]['dominant_emotion'] if isinstance(analysis, list) else analysis['dominant_emotion']
                
                print(f"Detected emotion: {emotion}")
                display_emotion = emotion  # Update text to be shown

                if emotion != last_emotion:
                    recommend_and_play_music(emotion)
                    last_emotion = emotion

                last_time = time.time()

            except Exception as e:
                print("Error during emotion detection:", e)

        # Show live frame
        cv2.imshow("Live Emotion Detection - Press 'q' to Quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the script
if __name__ == "__main__":
    run_realtime_recommender()
