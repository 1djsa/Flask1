from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route("/ALAMAT")
def FUNCTION_NAME():
    return "<hi> whats up !"

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return "<h1>Hello, World!</h1><br><p>Nice to see you</p><p>please check</p><a href='/random_fact'>View a random fact!</a><br><a href='/modern_fact'>View a modern fact!</a>"
    
# 2nd page
@app.route("/random_fact")

def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'
# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')#folder templates
app.run(debug=True)
