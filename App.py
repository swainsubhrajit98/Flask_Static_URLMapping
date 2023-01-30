from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/Hi')
def Hai():
    return render_template('Hai.html')

@FAI.route('/Image')
def Image_Insert():
    return render_template('Image_Insert.html')

@FAI.route('/MSD')
def Dhoni():
    return render_template('Dhoni.html')

if __name__=='__main__':
    FAI.run(debug=True)