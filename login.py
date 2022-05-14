from flask import Flask,render_template,request
import dbstore
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index1.html')


@app.route("/Login",methods=["POST","GET"])
def login():
    try:
        data=request.form
        print(data)
        Name=data["Name_of_Student"]
        Address=data["address"]
        Mobile_Number=data["mobile_no"]
        E_mail=data["e_mail"]
        
        dict1={"Name of Student":Name,"Address":Address,"Mobile Number":Mobile_Number,"E-Mail":E_mail}
        print(dict1)
        result=dbstore.Stdent_data(Name,Address,Mobile_Number,E_mail)
        if result=="Details Enter Successfully":
            return render_template('index1.html',Prediction2=result)
        else:
            return render_template('index1.html',Prediction2=result)
    except:
        result="Please Enter valid Result"
        return render_template('index1.html',Prediction2=result)
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)