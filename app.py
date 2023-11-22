from flask import Flask,render_template,request,redirect,url_for

app = Flask('__name__')

submitted_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save data (in this case, add it to the dummy list)
        submitted_data.append({'name': name, 'email': email, 'message': message})

        # Redirect to success page
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html', submitted_data=submitted_data)

if __name__ == '__main__':
    app.run(debug=True)