from flask import Flask, render_template
import pandas as pd

app =Flask(__name__, template_folder='temp')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/score/data')
def score_data():
    df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv')
    #df = pd.read_csv('/staitc/score.csv')
    table = df.to_html(classes='table table-striped table-hover', index=False)
    return table

if __name__=='__main__':
    app.run(port=5000, debug=True)