import marko
import os

def generate_markdown(input_text, filename, output_location, overwrite):
   markdown = marko.convert(input_text)
   filepath = os.path.join(output_location, filename)
   # Deletes the file if overwrite is true
   if overwrite == "Yes" and os.path.exists(filepath):
      open(filepath, 'w').close()
   # If the output directory does not exists it is created
   if not os.path.exists(output_location):
      os.makedirs(output_location)

   f = open(filepath, 'a')
   f.write(markdown)
   f.close()
   f = open(filepath, 'r')