from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash(f'Thank you, {name}! We’ll reply to {email} soon.', 'success')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)