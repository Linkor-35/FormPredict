from forms import IsValidForm
from fastapi import FastAPI
import uvicorn
from config import BASE_URL

app = FastAPI()


@app.get("/")
def get_data():
    return "qwdqw"



@app.post("/", status_code=200)
def post_data(data):
    result = IsValidForm.parse_obj(data)
    print(repr(result.date))
    return result.json


if __name__ == "__main__":
    if BASE_URL == "":
        uvicorn.run(app, host="127.0.0.1", port=8000)
    else:
        uvicorn.run(app, host=BASE_URL, port=8000)