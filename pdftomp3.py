import pyttsx3,pypdf

#insert name of your pdf 
pdfreader = pypdf.PdfReader(open(r"C:\\Users\\billy\\Desktop\\book.pdf", 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'bruh.mp3')
speaker.runAndWait()

speaker.stop()

