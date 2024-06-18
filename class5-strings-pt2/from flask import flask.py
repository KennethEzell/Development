from flask import flask
app = Flask(__name__) # lask Construcktor

@app.route('/') # Decorator, that will take in another functios
def hello():
    return 'HELLO'

@app.route('/resume')
def my_resume():
    return 'This would be my resume'

if __name__ =='__main__':
    app.run()
    