from flask import Flask, render_template, request
app = Flask(__name__)


def saveDocument ():
    with open("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "r") as notes:
            lines = notes.readlines()
            with open ("ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as finalNotes:
                finalNotes.writelines(lines)
                notes.close()
                finalNotes.close()
            return


def documentThis ():
    prompts = [{{ customerName }}, {{ TID }}, {{ callDriver }}, {{ caller }}, {{ callBack }}, {{ serial }}, {{ address }}, {{ ZpCode }}, {{ callNotes }}]
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
        def border():
            notes.write("\n*********************************************************\n")
            return
        border()
        for item in prompts:
            notes.write(item + " " + prompts[item] + "\n")
        border()
    saveDocument()
    return


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ticketMaker', methods=['GET', 'POST'])
def ticketMaker():
    return render_template('test_form.html', methods=['GET', 'POST'])


@app.route('/input', methods=['GET', 'POST'])
def input():
    return render_template('tfr.html',\
                           customerName=request.form['customerName'],\
                           terminalID=request.form['terminalID'],\
                           serial=request.form['serial'],\
                           caller=request.form['caller'],\
                           phoneNumber=request.form['phoneNumber'],\
                           address=request.form['address'],\
                           ZpCode=request.form['ZpCode'],\
                           callNotes=request.form['message'])


@app.route('/inputb', methods=['GET', 'POST'])
def inputb():
    customerName=request.form['customerName'],\
    terminalID=request.form['terminalID'],\
    serial=request.form['serial'],\
    caller=request.form['caller'],\
    phoneNumber=request.form['phoneNumber'],\
    address=request.form['address'],\
    ZpCode=request.form['ZpCode'],\
    callNotes=request.form['message']
    return documentThis()



@app.route('/tidelClaimer')
def tidelClaimer():
    return '<link rel="stylesheet" type="text/css" href="static/theme.css">'\
    '<h1>Coming SOON!!</h1>'


@app.route('/tidelUnClaimer')
def tidelUnClaimer():
    return '<link rel="stylesheet" type="text/css" href="static/theme.css">'\
    '<h1>Coming SOON!!</h1>'


@app.route('/partsCalc')
def partsCalc():
    return '<link rel="stylesheet" type="text/css" href="static/theme.css">'\
    '<h1>Coming SOON!!</h1>'


if __name__=='__main__':
    app.run(debug=True)
