from flask import Flask, flash, redirect, render_template, request, session, abort
import driver

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('test.html')

@app.route("/ngram_viewer", methods = ['POST'])
def ngram_viewer():
    print('In ngram viewer')
    input_terms = request.form['search_terms']
    terms = input_terms.split(',')
    for term in terms:
        frequency = driver.find_ngram_freq(term)
        print('{} : {}%'.format(term,frequency))
    print('Terms {}'.format(terms))
    return render_template('test.html')


if __name__ == "__main__":
    app.run(port=80, debug=True)