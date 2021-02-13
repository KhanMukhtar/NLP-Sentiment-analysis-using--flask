from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap 


# NLP Packages
from textblob import TextBlob,Word 
import random 
import time

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyse',methods=['POST'])
def analyse():
	start = time.time()      # to print the start time just to check processing time
	if request.method == 'POST':
		rawtext = request.form['rawtext'] #this will be our input text
		#NLP Stuff
		blob = TextBlob(rawtext) #text will preprocess
		received_text2 = blob #store or copy preprocess text in other variable
		blob_sentiment,blob_subjectivity = blob.sentiment.polarity ,blob.sentiment.subjectivity #creating polarity & subjectivity
		number_of_tokens = len(list(blob.words)) #checking len of words & convet into list & tokenize it
		# Extracting Main Points
		nouns = list()
		for word, tag in blob.tags: #creting part of speech(POS)
		    if tag == 'NN':  #(checking if words are noun or not
		        nouns.append(word.lemmatize()) #lemmatize the words
		        len_of_words = len(nouns)
		        rand_words = random.sample(nouns,len(nouns)) #checking random words lihe "is","a","the" etc
		        final_word = list()
		        for item in rand_words:
		        	word = Word(item).pluralize() #creating plural words which are singular
		        	final_word.append(word)
		        	summary = final_word
		        	end = time.time()
		        	final_time = end-start #from print final time 


	return render_template('index.html',received_text = received_text2,number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,summary=summary,final_time=final_time)






if __name__ == '__main__':
	app.run(debug=True)