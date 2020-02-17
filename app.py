from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/about_us')
def about():
    return render_template("about_us.html")

@app.route('/contact_us')
def contact():
    return render_template("contact_us.html")

@app.route('/Egypt')
def country():
    return render_template("Egypt.html")

if __name__ == '__main__':
	app.run( debug=True)
