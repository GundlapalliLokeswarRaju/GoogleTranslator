import googletrans
from googletrans import Translator
import speech_recognition as spr
from gtts import gTTS
import os
print(googletrans.LANGUAGES)
print("""Choose translation options:
        1.For google assistent audio to text-to-translate
        2.For google text-to-translator to audio translator
        3.For google text-to-translator
        4.For google assistent to translate""")
options=int(input("choose your option:"))
if(options==1):
    recog1 = spr.Recognizer()
    mc = spr.Microphone()
    with mc as source:
        print("Speak 'ok google' to initiate the Translation !")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        recog1.adjust_for_ambient_noise(source, duration=0.02)
        audio = recog1.listen(source)
        MyText = recog1.recognize_google(audio)
        MyText = MyText.lower()
    if 'ok google' in MyText:
        translator = Translator()
        from_lang = input("Enter source language:")
        to_lang = input("Enter destination language:")

        with mc as source:
            print("Speak a stentence...")
            recog1.adjust_for_ambient_noise(source, duration=2.00)
            audio = recog1.listen(source)
            get_sentence = recog1.recognize_google(audio)
            try:
                print("Phase to be Translated :" + get_sentence)
                text_to_translate = translator.translate(get_sentence,
                                                         src=from_lang,
                                                         dest=to_lang)

                text = text_to_translate.text
                print(text)
            except text.UnknownValueError:
                print("Unable to Understand the Input")
            except text.RequestError as e:
                print("Unable to provide Required Output".format(e))
elif(options==2):
    translator = Translator()
    from_lang = input("Enter source language:")
    to_lang = input("Enter destination  language:")
    text = input("Enter text :")
    print("your text is", text)
    try:
        print("Phase to be Translated :" +text)
        text_to_translate = translator.translate(text,
                                                 src=from_lang,
                                                 dest=to_lang)

        Text = text_to_translate.text

        speak = gTTS(text=Text, lang=to_lang, slow=False)
        speak.save("captured_voice.mp3")
        os.system("start captured_voice.mp3")

    except spr.UnknownValueError:
        print("Unable to Understand the Input")
    except spr.RequestError as e:
        print("Unable to provide Required Output".format(e))

if(options==3):
    translator=Translator()
    from_lang=input("Enter source language:")
    to_lang=input("Enter destination  language:")
    text=input("Enter text :")
    print("your text is",text)
    try:
        text_to_translator=translator.translate(text,src=from_lang,dest=to_lang)
        Text=text_to_translator.text
        print(Text)
    except text.UnknownValueError:
        print("Unable to Understand the Input")
    except text.RequestError as e:
        print("Unable to provide Required Output".format(e))
elif(options==4):
    recog1=spr.Recognizer()
    mc = spr.Microphone()
    with mc as source:
        print("Speak 'ok google' to initiate the Translation !")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        recog1.adjust_for_ambient_noise(source, duration=0.02)
        audio = recog1.listen(source)
        MyText = recog1.recognize_google(audio)
        MyText = MyText.lower()

    if 'ok google' in MyText:
        translator = Translator()
        from_lang =input("Enter source language:")
        to_lang = input("Enter destination language:")

        with mc as source:

           print("Speak a stentence...")
           recog1.adjust_for_ambient_noise(source, duration=0.02)

           audio = recog1.listen(source)
           get_sentence = recog1.recognize_google(audio)
        try:
            print("Phase to be Translated :" + get_sentence)
            text_to_translate = translator.translate(get_sentence,
                                                     src=from_lang,
                                                     dest=to_lang)


            text = text_to_translate.text

            speak = gTTS(text=text, lang=to_lang, slow=False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")

        except spr.UnknownValueError:
            print("Unable to Understand the Input")
        except spr.RequestError as e:
            print("Unable to provide Required Output".format(e))


