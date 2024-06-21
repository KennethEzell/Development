from flask import Flask
app = Flask(__name__) # Flask Constructor

# Decorator, a function we can use on a function
@app.route('/') # Decorator, that will take in another functtion
def hello():
    return'HELLO'

@app.route('/resume')
def my_resume():
    return 'This would be my resume'

if __name__ == '__main__':
    app.run()