import pyttsx3.voice
import PyPDF2

droid = pyttsx3.init()
livre = open('salut.pdf',)
lecture = PyPDF2.PdfFileReader(livre)
pages = lecture.numPages
print(pages)

#droid.say("Haha ! On dirait que tu as trouvé ça drôle.Veux‑tu que je fasse quand même le tableau comparatif Catholiques vs Protestants, ça rend tout beaucoup plus clair visuellement ?")
#droid.say("Bonjour Monsieur SONGA LUKEKA JEAN je suis un droid de la nouvel géneration et je suis Turuns")
droid.runAndWait() 
