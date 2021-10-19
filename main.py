from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/')
def loginPage(): 
    return render_template("login.html")

@app.route('/portal')
def portalPage(): 
    return render_template("portal.html")

#write your code here!

if __name__ == '__main__':
	app.run(debug=True)