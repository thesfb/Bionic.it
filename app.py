from flask import Flask, render_template, request, make_response
import re


app = Flask(__name__)

def bionic_reading(text):
 
    words = re.findall(r'\b\w+\b', text)


    transformed_words = []
    for word in words:
        if len(word) > 4:
            transformed_word = f'<b>{word[0]}</b><b>{word[1]}</b><b>{word[2]}</b>{word[3::]}</b>'
        else:
            transformed_word = word
        transformed_words.append(transformed_word)

 
    transformed_text = ' '.join(transformed_words)

    return transformed_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form.get('input-text')
        output_text = bionic_reading(input_text)
        return render_template('index.html', output_text=output_text)
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
