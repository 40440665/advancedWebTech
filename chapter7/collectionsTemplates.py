from flask import Flask, render_template
app= Flask(__name__)

@app.route('/users/')
def users():
 names =['simon', 'thomas', 'lee', 'james', 'pauline']
 return render_template('loops.html', names=names)

