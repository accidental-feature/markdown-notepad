import marko 
import os

def from_file(input_file, filename, output_location):
   if input_file.endswith('.txt'):
      user_file = open(input_file, 'r')
      markdown = marko.convert(user_file.read())
      filepath = os.path.join(output_location, filename)
      if not os.path.exists(output_location):
         os.makedirs(output_location)
      f = open(filepath, 'a')
      f.write(markdown)
      f.close()
      f = open(filepath, 'r')
      print(f.read())
   else:
      print('Only txt files are excepted')