from flask import Flask
from flask import jsonify
import os, csv, subprocess


app = Flask(__name__)
macroSimCommand = ['python', '/model/simulate.py']
dataDir = '/rea-data/'
dummyDataInput = 'dummy-data.csv'

@app.route('/test')
def test():
    with open(dataDir + dummyDataInput) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
    return jsonify(message = 'service is available', datasamples = line_count,
                status = 0)

@app.route('/start')
def start():
    # Start a worker processes.
    #-----------------------------------------------
    # Here we will link the real simulation later on
    subprocess.Popen(macroSimCommand)
    #-----------------------------------------------
    return jsonify(message = 'macromodel simulation started',
                status = 0)
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

