from flask import Flask,render_template
import pandas as pd



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])



def hello():
    df = pd.read_csv(r'https://raw.githubusercontent.com/sairamsnv/jsonapi/main/jonathanY.csv')
    dj = df.to_json()
    return render_template('hello.html',si='{}'.format(dj))






if __name__ == "__main__":
    app.run()
