from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

class ResourceTranslator:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        self.bs = BeautifulSoup(file)

    def translate(self, langs):
        for lang in langs:
            out_file = 'strings-' + lang + '.xml'
            names = []
            texts = []
            for text in self.bs.find_all('string', attrs={'translatable': None}):
                if text.string is None or text.attrs['name'] is None:
                    continue

                names.append(text.attrs['name'])
                texts.append(text.string)

            translations = translator.translate(texts, dest=lang)

            out = BeautifulSoup()

            for i in range(len(names)):
                t = out.new_tag('string', attrs={'name': names[i]})
                t.string = translations[i].text
                out.append(t)
            f = open(out_file, "w")
            f.write(out.prettify())
            f.close()
