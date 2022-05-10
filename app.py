from crypt import methods
from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template')

@app.route('/')
@app.route('/home')
def home():
    companies =["Advanced Micro Devices,Inc","Apple","Palantir Technologies Inc","Ford Motor Company","NVIDIA Corporation","NIO Inc"]
    return render_template('index.html', companies = companies)


@app.route('/viewresult', methods=['GET', 'POST'])
def scrapDataResult():
    if request.method == 'POST':
        
    
    return render_template('index.html')




if __name__=="__main__" :
    app.run(debug=True)