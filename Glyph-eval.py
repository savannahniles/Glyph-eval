from flask import Flask, render_template, request, redirect, url_for     # for running the Flask server
import sys                                                               # for obtaining command line arguments
import json
import csv
import time


app = Flask(__name__)
app.debug=True

#ultimately how we'll input a URL and be forewarded to that page
@app.route('/')
def home():
    data = "news"
    return render_template('Glyph-eval.html')

@app.route('/endStudy/', methods=['POST'])
def endStudy():
    results = request.data
    target = open('evalResults/' + str(int(time.time())) + '.json', 'w')
    target.write(results)
    target.close()
    return results


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "USAGE: python Glyph-eval.py [port #]"
    else:
        # app.run(port = int(sys.argv[1])) # run on the specified port number
        app.run(host = "0.0.0.0", port = int(sys.argv[1]))

