from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/play')

@app.route('/play')
def play():
    return render_template("index.html", count=3, color="lightblue")

@app.route('/play/<int:count>')
def additup(count):
    return render_template("index.html", count=count, color="lightblue")

@app.route('/play/<int:count>/<color>')
def addcolor(count, color):
    return render_template("index.html", count=count, color=color)


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    

#  TODAY I LEARNED HOW TO USE FLASK TO CREATE A SERVER AND CONNECT(RENDER) MY HTML WITH SOME FUNCTIONALITY ALONG WITH REDIRECTING URLS