from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_, 'explanation': spacy.explain(ent.label_)} for ent in doc.ents]

    return jsonify({'entities': entities})

if __name__ == '__main__':
    app.run(debug=True)

'''
Barack Obama was born in Hawaii and served as the 44th President of the United States.
He graduated from Harvard Law School in 1991.
In 2009, he was awarded the Nobel Peace Prize.
His wife, Michelle Obama, is also a well-known public figure.
'''