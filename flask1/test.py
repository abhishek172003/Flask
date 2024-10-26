from flask import Flask
from flask import render_template,request
from flask import jsonify

## create a simple flask app
app=Flask(__name__)
#__name__ is entry point

@app.route('/',methods=["GET"])
def welcome():
    return "<h1>Hello, World!</h1>"

@app.route('/index',methods=['GET'])
def index():
    return"<h2>WElcome to the Index Page</h2>"



##variable 
@app.route('/success/<score>')
def success(score):
    return "the persom has passed and score is:" + score


##variable rule
#means you can assign rules to variables
@app.route('/newsuccess/<int:score>')
def newsuccess(score):
    return "the persom has passed and score is:" + str(score)



##Html Page Rendering And Url Redirection
@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
        #always remember form.html will always be in templates folder


@app.route('/calculate',methods=["GET","POST"])
def calculate():
    if request.method=="GET":
        return render_template('calculate.html')
        #always remember calculate.html will always be in templates folder
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        return render_template('calculate.html',score=average_marks)

        #Jinja2 Web Template


##Flask API Creation
@app.route('/api',methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)
    #send json data by postman api

if __name__=="__main__":
    app.run(debug=True) 
    #by deafult url=localhost and port 5000 