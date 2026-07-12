import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return ""
        except sr.RequestError:
            print("❌ API unavailable")
            return ""

def route(text):
    if "bill" in text or "payment" in text:
        print("📞 Connecting to Billing Department...")
    
    elif "problem" in text or "error" in text or "issue" in text:
        print("🛠 Connecting to Technical Support...")
    
    elif "buy" in text or "price" in text or "purchase" in text:
        print("💼 Connecting to Sales Department...")
    
    else:
        print("❓ Please try again.")

def main():
    print("=== Smart Customer Switchboard ===")

    while True:
        text = listen()
        if text:
            route(text)

        choice = input("\nPress Enter to continue or type 'exit' to quit: ")
        if choice.lower() == "exit":
            break

if __name__ == "__main__":
    main()
