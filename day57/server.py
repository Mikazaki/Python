from flask import Flask, render_template
import requests

app = Flask(__name__)

G_URL = 'https://api.genderize.io?'
A_URL = 'https://api.agify.io?'



@app.route('/guess/<names>')
def guess(names):
    param = {
    'name': names
    }

    g_response = requests.get(G_URL, params=param)
    a_response = requests.get(A_URL, params=param)

    genderio = g_response.json()
    ageio = a_response.json()
    
    name = genderio['name']
    age = ageio['age']
    gender = genderio['gender']
 

    return render_template('index.html', n = name, a = age, g = gender)


if __name__ == '__main__':
    
    app.run(debug=True)