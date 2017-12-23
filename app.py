from flask import Flask, flash, redirect, render_template, request, session, abort
import driver
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('test.html')

@app.route("/ngram_viewer", methods = ['POST'])
def ngram_viewer():
    print('In ngram viewer')
    input_terms = request.form['search_terms']
    labels, all_term_freq = driver.find_ngram_freq_multiple(input_terms)
    terms = input_terms.split(',')
    print('n : {}'.format(len(terms)))
    print('labels : {}'.format(labels))
    for i in range(len(terms)):
        print('{} : {}'.format(terms[i], all_term_freq[i]))
    return render_template('chart3.html', all_data=list(zip(terms,all_term_freq)), labels=labels)

if __name__ == "__main__":
    app.run(port=80, debug=True)