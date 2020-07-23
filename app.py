from flask
import Flask,render_template,request,dateutil

app = Flask(__name__)

@app.route('/')
def index():
    msg = request.form.get('msg')
    return render_template('index.html')

if __name__=='__main__':
    app.debug = True
    app.run()