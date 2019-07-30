from ResourceTranslator import ResourceTranslator
import sys

input_file = sys.argv[1]
langs = sys.argv[2]

langs = langs.split(',')

# input_file = 'source-strings.xml'
# langs = ['de', 'ja', 'nl']

rt = ResourceTranslator('strings.xml')
rt.translate(langs)
