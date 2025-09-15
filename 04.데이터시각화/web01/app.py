from flask import Flask, render_template, send_file
from io import BytesIO

import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv', index_col='지원번호')

import matplotlib.pyplot as plt
#한글설정
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size = 10)
plt.rc('axes', unicode_minus = False)

app = Flask(__name__, template_folder='templates')

@app.route('/graph1') #학생별키 막대그래프
def graph1():
    name = df['이름']
    height = df['키']
    plt.figure(figsize=(10, 5))
    plt.ylim(150, 210)
    plt.bar(name, height, color='orange', hatch='/', ec='yellow')
    plt.xticks(name, rotation=45, size=8, color='g')
    for idx, h in enumerate(height):
        plt.text(idx, h+1, h, ha='center', color='g', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')
@app.route('/')
def index():
    return render_template('index.html', title='학생관리')

if __name__=='__main__':
    app.run(port=5000, debug=True)