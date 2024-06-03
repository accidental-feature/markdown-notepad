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
   inquirer.Path('output', 
      message='Where should the created note be located?',
      path_type=inquirer.Path.DIRECTORY
   ),
   inquirer.Text('filename', 
      message="What should the file be named?",
      default='markdown-note.md'
   ),
   inquirer.Text('text', 
      message='The markdown text',
      default=''
   )
]

answers = inquirer.prompt(questions)

if answers['type'] == 'Yes':
   from_text(answers['text'], answers['filename'], answers['output'])