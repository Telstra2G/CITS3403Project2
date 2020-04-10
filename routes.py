from flask import flash, request, render_template, redirect, url_for
from app import app


@app.route('/')
@app.route('/index')

def index():
    
    limit = 2
    
    questions = [
        {
            'question': 'What holds tags',
            'answers': ['{ }', '[ ]', '< >', '( )']
        },
        {
            'question': 'what controls a websites "style"',
            'answers': ['HTML', 'CSS', 'Javascript', 'Flask']
        }
    ]
    
    correct = ['< >', 'CSS']
    
    num = len(questions)
    
    return render_template('questions.html', questions=questions, num=num, limit=limit)





