from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    fw=open("Sample2.json","r")
    data_str=fw.read().replace('\n','')
    print(type(data_str))
    print(data_str)
    return render_template('index.html',jstr=data_str)

if __name__ == '__main__':
    app.run(debug=True)
