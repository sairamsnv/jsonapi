from flask import Flask,render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello():
    df = pd.read_excel("C:/Users/laxmi/jonathanY.Xlsx")
    dj = df.to_json()
    return render_template('hello.html',si='{}'.format(dj))
if __name__ == "__main__":
    app.run()

