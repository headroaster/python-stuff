
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/horror')
def horror():
    return render_template('horror.html')

@app.route('/comedy')
def comedy():
    return render_template('comedy.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/heroic')
def heroic():
    return render_template('heroic.html')

@app.route('/scifi')
def scifi():
    return render_template('scifi.html')

    
if __name__=='__main__':
    app.run(debug=True)
