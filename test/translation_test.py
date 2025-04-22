from googletrans import Translator

translator = Translator()

if __name__ in "__main__":
    text = 'hello'
    translated = translator.translate(text, src='en', dest='ja')
    print(translated.text)
