import pyttsx3
import PyPDF2
book = open('python.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.pages

#print(pages)
speaker = pyttsx3.init()
page = pdfreader.getPage(12)
text = page.extractText()
#speaker.say(text)

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.say(text)

speaker.runAndWait()