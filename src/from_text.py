import marko
import os

def from_text(text, filename, output_location):
   markdown = marko.convert(text)
   filepath = os.path.join(output_location, filename)
   if not os.path.exists(output_location):
      os.makedirs(output_location)
   f = open(filepath, 'a')
   f.write(markdown)
   f.close()
   f = open(filepath, 'r')
   print(f.read())