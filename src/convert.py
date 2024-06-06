import os
import sys
from generate_markdown import generate_markdown

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
   text_questions = [
      inquirer.Text('text', 
         message='The markdown text',
         default=''
      )
   ]
   text_answer = inquirer.prompt(text_questions)
   generate_markdown(text_answer['text'], answers['filename'], answers['output'])
else:
   file_questions = [
      inquirer.Path('file',
         message='Enter the path to the .txt file',
         path_type=inquirer.Path.FILE
      )
   ]
   file_answer = inquirer.prompt(file_questions)
   if file_answer['file'].endswith('.txt'):
      user_file = open(file_answer['file'], 'r')
      file_text = user_file.read()
      generate_markdown(file_text, answers['filename'], answers['output'])
   else:
      print('Only txt files are excepted')