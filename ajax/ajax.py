from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fname = request.form.get('fname')
        bday = request.form.get('bday')
        age = request.form.get('age')  

        age = int(age) if age else None
        
        response = f"Name: {fname}<br><br>Age: {age}"
        
        return response

if __name__ == '__main__':
    app.run(debug=True)
