from googletrans import Translator

translator = Translator()

def translate(text):
    lang = translator.detect(text).lang
    print(lang)
    translation = translator.translate(text, src=lang, dest='en')
    return translation.text