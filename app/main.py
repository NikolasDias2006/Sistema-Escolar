from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def testapi():
    return{'message': 'Welcome to school system'}