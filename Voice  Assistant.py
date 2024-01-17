import speech_recognition as sr
import pyttsx3

class Assistant:
    def __init__(self):
        self.memory = {}  
    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Couldn't request results from Google Speech Recognition service; {e}")
            return ""

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        print(f"Assistant: {text}")  

    def learn(self, question, answer):
        self.memory[question.lower()] = answer

    def answer_question(self, question):
        question = question.lower()
        if question in self.memory:
            return self.memory[question]
        else:
            return "I'm sorry, I don't have an answer for that."

    def assistant(self):
        self.speak("Hello! I'm your voice assistant. How can I help you today?")

        while True:
            query = self.listen()

            if "stop" in query:
                self.speak("Goodbye!")
                break
            elif "hello" in query:
                self.speak("Hello! How can I assist you?")
            elif "learn" in query:
                self.speak("Sure! What is the question you want me to learn?")
                new_question = self.listen()
                self.speak(f"Got it! What is the answer to '{new_question}'?")
                new_answer = self.listen()
                self.learn(new_question, new_answer)
                self.speak("Thank you! I have learned a new piece of information.")
            else:
                response = self.answer_question(query)
                self.speak(response)

if __name__ == "__main__":
    assistant = Assistant()
    assistant.assistant()
