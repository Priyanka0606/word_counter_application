from flask import Flask, render_template, request
import nltk
import string
from nltk.corpus import stopwords
from nltk import FreqDist

nltk.download('punkt')


# initialize the app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods =['post']) 
def predict():
    text = request.form.get('fname')
    print(text)
    
    char = len(text)

    sentences = len(nltk.sent_tokenize(text))

    wordsnum = len(nltk.word_tokenize(text))
   
    freq = FreqDist(nltk.word_tokenize(text))

    char = len(text)
    


    return render_template('predict.html', predict = { 'Sentences': sentences , 'Words': wordsnum ,'Characters': char,
                                                    'frequencyof words': freq})


# Run the app
if __name__ == '__main__':
    app.run()
