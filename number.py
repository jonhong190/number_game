from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'shh'
import random


@app.route('/')
def game():
    return render_template('index.html')

@app.route('/random', methods=['POST'])
def randomize():
    if 'random' not in session:
        session['random'] = random.randrange(0,101)
 
    if 'attempt' not in session:
        session['attempt'] = 0
    session['attempt'] = int(request.form['guess'])
   
    if session['attempt'] > session['random']:
        session['answer'] = 'higher'
        return redirect('/')
    elif session['attempt'] < session['random']:
        session['answer'] = 'lower'
        return redirect('/')
    elif session['attempt'] == session['random']:
        session['answer'] = 'correct'
        return redirect('/')
        
@app.route('/reset', methods=['POST'])
def replay():
    session.clear()
    return redirect('/')
    

app.run(debug=True)