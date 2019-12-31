# Deep Leaning Model Deployment using Flask API

This repo contains a sample code to show how to create a Flask API server by deploying our PyTorch model

## Prepare 
```
pip install -r requirements.txt
```

## Run
```
flask run
```

Now go to `http://127.0.0.1:5000/` via chrome browser and upload image. 

<p align="left"><img src="assets/guide.png" width="1246"\></p>

## Result

| GT: goldfish | GT: power drill | GT: tench |
| :-------: |:-------:|:----------:|
| <p align="center"><img src="assets/result1.png" width="320"\></p> |<p align="center"><img src="assets/result2.png" width="320"\></p> |<p align="center"><img src="assets/result3.png" width="320"\></p>|