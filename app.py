from flask import Flask, render_template , request 
from textblob import TextBlob


app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('form.html')



@app.route('/submit', methods = ['POST'])
def form_data():
   user_data = request.form.get('user_data')
   blob = TextBlob(user_data)
   language = request.form.get('language')
   if language == 'Gujarati':
        output = blob.translate(to = 'gu')
   elif language == 'Hindi':
        output = blob.translate(to = 'hi')
   elif language == 'Marathi':
        output = blob.translate(to = 'mr')
   elif language == 'German':
        output = blob.translate(to = 'de')   
   elif language == 'Kannada':
        output = blob.translate(to = 'kn')            

   return render_template('predict.html', data = f'{output} ')
   
if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=8080))
