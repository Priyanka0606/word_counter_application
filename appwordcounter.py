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


    punct = string.punctuation
    stop_words = stopwords.words('english')
    
    char = len(text)

    sentences = nltk.sent_tokenize(text)
    sent = len(sentences)

    words_token = nltk.word_tokenize(text)
    wordnum = len(words_token)

    char = len(text)
    
    clean_word = [word for word in nltk.word_tokenize(text.lower()) if word not in punct]
    without_stopwords = [word for word in clean_word if word not in stop_words]
    words = len(without_stopwords)

    freq = FreqDist(without_stopwords)

    return render_template('predict.html' , predict = f'No of sentences is : {sent}')


# Run the app
if __name__ == '__main__':
    app.run()
