import tkinter as tk
import datetime
import speech_recognition as sr
import pyttsx3

# 🔊 Text to Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# 🧠 Chatbot Brain
def get_response(user):
    user = user.lower()

    # Greetings
    if "hello" in user or "hi" in user or "hey" in user:
        return "Hello buddy! How can I help you?"

    elif "how are you" in user:
        return "I'm doing great, thank you for asking!"

    elif "name" in user:
        return "I'm your College AI Assistant."

    # Date & Time
    elif "time" in user:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        return "The current time is " + time

    elif "date" in user:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        return "Today's date is " + date

    # College Queries
    elif "course" in user or "courses" in user:
        return "We offer AI, Data Science, Web Development and Python courses."

    elif "fees" in user or "fee" in user:
        return "Please contact the office for detailed fee structure."

    elif "placement" in user or "job" in user:
        return "Yes, we provide placement assistance for students."

    elif "library" in user:
        return "Library is open from 8 AM to 6 PM."

    elif "canteen" in user:
        return "Canteen is open from 9 AM to 4 PM."

    elif "bye" in user:
        return "Goodbye! Have a great day 😊"

    else:
        return "Sorry, I didn't understand that."

# 🎤 Voice input function
def listen_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat.insert(tk.END, "Listening...\n")
        chat.yview(tk.END)
        window.update()

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        entry.delete(0, tk.END)
        entry.insert(0, text)
        send()
    except:
        chat.insert(tk.END, "Could not understand voice\n")
        chat.yview(tk.END)

# 📤 Send message function
def send(event=None):
    user = entry.get()

    if user.strip() == "":
        return

    chat.insert(tk.END, "You: " + user + "\n")
    chat.yview(tk.END)

    # 🤖 Typing indicator
    chat.insert(tk.END, "Bot is typing...\n")
    chat.update()
    window.after(800)

    response = get_response(user)

    chat.insert(tk.END, "Bot: " + response + "\n\n")
    chat.yview(tk.END)

    speak(response)  # 🔊 bot speaks reply
    entry.delete(0, tk.END)

# 🧹 Clear chat function
def clear_chat():
    chat.delete('1.0', tk.END)

# 🪟 Create window
window = tk.Tk()
window.title("🎓 College AI Assistant")

# 🎓 App Heading
title = tk.Label(window, text="🎓 College AI Assistant", font=("Arial",16,"bold"))
title.pack(pady=5)

# 💬 Chat display box
chat = tk.Text(window, height=20, width=55)
chat.pack(padx=10, pady=5)

# ⌨️ Input frame (to align buttons nicely)
frame = tk.Frame(window)
frame.pack()

entry = tk.Entry(frame, width=35)
entry.grid(row=0, column=0, padx=5)
entry.bind("<Return>", send)

send_btn = tk.Button(frame, text="Send", command=send)
send_btn.grid(row=0, column=1, padx=5)

voice_btn = tk.Button(frame, text="🎤 Speak", command=listen_voice)
voice_btn.grid(row=0, column=2, padx=5)

clear_btn = tk.Button(frame, text="Clear Chat", command=clear_chat)
clear_btn.grid(row=0, column=3, padx=5)

# 🔁 Run app
window.mainloop()