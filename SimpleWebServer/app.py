# import the Flask class from the flask module
from time import sleep
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

secretPassword = "we just need a very long string, that shows that a difference comes in time!"

# use decorators to link the function to a url

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))

    #if len(request.form["password"] == 10):
    #  print 10


    if ( len(request.form["password"]) == len(secretPassword)):
      for i in range(len(request.form["password"])):
        if request.form["password"][i] == secretPassword[i]:
          continue
        else:
          break

    return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
