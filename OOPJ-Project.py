from flask import Flask, render_template, request

import MainProcess


app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/rebates')
def rebates():
    userlist=[]
    userlists=[]
    userlist=MainProcess.processAccounts()
    userlists=MainProcess.processAccountss() #secondcard
    totalCiti = 0
    totalOcbc = 0
    totalCiti = MainProcess.rebatesTransaction
    totalOcbc = MainProcess.rebatesTransaction

    return render_template('rebates.html', citiAmount = totalCiti, ocbcAmount = totalOcbc,users=userlist, user=userlists)

@app.route('/compare')
def compare():
    return render_template('compare.html')

@app.route('/citibank')
def citibank():
    return render_template('citibank.html')

@app.route('/Mayciti')
def Mayciti():
    return render_template('Mayciti.html')

@app.route('/AugOcbc')
def AugOcbc():
    return render_template('AugOcbc.html')

@app.route('/NovOcbc')
def NovOcbc():
    return render_template('NovOcbc.html')

@app.route('/JunCiti')
def JunCiti():
    return render_template('JunCiti.html')

@app.route('/Augciti')
def Augciti():
    return render_template('Augciti.html')

@app.route('/NovCiti')
def NovCiti():
    return render_template('NovCiti.html')

if __name__ == '__main__':
    app.run()






