import os
import sys
from from_text import from_text

sys.path.append(os.path.realpath("."))
import inquirer

questions = [
   inquirer.List('type', 
      message="Are you converting a raw text?",
      choices=['Yes', 'No']
   ),
   inquirer.Text('filename', 
      message="What should the file be named?",
      default='markdown-note.md'
   ),
   inquirer.Path('output', 
      message='Relative path this file will be saved in.',
      path_type=inquirer.Path.DIRECTORY
   ),
]

answers = inquirer.prompt(questions)

if answers['type'] == 'Yes':
   test_questions = [
      inquirer.Text('text', 
         message='The markdown text',
         default=''
      )
   ]
   text_answer = inquirer.prompt(test_questions)
   from_text(text_answer['text'], answers['filename'], answers['output'])
if answers['type'] == 'No':
   print('File types are not yet supported')