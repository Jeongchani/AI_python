from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', title='학생관리')

if __name__=='__main__':
    app.run(port=5000, debug=True)