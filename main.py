from flask import Flask,request

import fit
strval = 0
app = Flask(__name__)
@app.route('/',methods = ['GET'])
def main():
    m = fit.walk()
    
    
    return (str(strval) + "|" + str(m))
@app.route('/str',methods = ['POST','GET'])
def a():
    if(request.method == 'POST'):
        data = request.get_data()
        
        print "recevied request data"
        if(str(data) =='1'):
            print "recvied str"
            print strval
            global strval
            strval +=5

        return "received"
    else:
        return str(strval)
if __name__ == "__main__":
    app.debug = True
    app.run()
