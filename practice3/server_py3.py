from flask import Flask
import sys

if len(sys.argv) != 3:
    print('\nUsage: \npython server.py 이름 포트번호\n')
    exit(0)

app = Flask(__name__)

@app.route('/')
def hello():
    return f'<h1>I am {sys.argv[1]}</h1>'

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=sys.argv[2])
