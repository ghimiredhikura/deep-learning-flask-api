import os
from flask import Flask, request, render_template
import label_image

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
       return render_template('index.html')
    if request.method == 'POST':
        if 'file' not in request.files:
            print('file not uploaded')
            return
        file = request.files['file']
        image = file.read()
        result = label_image.get_predictions(image)
        filename = file.filename
        top1 = '1. %s, %.4f'%(result[0][0], result[0][1])
        top2 = '2. %s, %.4f'%(result[1][0], result[1][1])
        top3 = '3. %s, %.4f'%(result[2][0], result[2][1])        

        return render_template('result.html', output_top1=top1, output_top2=top2, output_top3=top3, image=filename)

if __name__ == '__main__':
    app.run(debug=True)

