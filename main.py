from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    return """<h1>Hello, World!</h1><br>
              <p>Nice to see you</p>
              <p>please check</p>
              <a href='/random_fact'>View a random fact!</a><br>
              <a href='/modern_fact'>View a modern fact!</a><br>
              <a href='/my_self'>Fun Fact about myself!</a>"""

# 2nd page
@app.route("/random_fact")
def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'

# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')  # folder templates

@app.route('/my_self')
def ketiga():
    text_name = (os.listdir("myself"))
    with open(f'myself/{text_name}', 'r') as f:
        midocument = f.read()
    return f'{midocument}'


if __name__ == "__main__":
    app.run(debug=True)