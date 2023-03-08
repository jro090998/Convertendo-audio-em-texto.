import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Você disse: {}".format(text))
except sr.UnknownValueError:
    print("Não entendi o que você disse")
except sr.RequestError as e:
    print("Não foi possível obter resultados; {0}".format(e))
