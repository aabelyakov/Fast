import uvicorn
import os
import signal
from fastapi import FastAPI


app = FastAPI()


@app.get('/hello')
def hello():
    return {"Приветствие": "Здравствуй, МИР"}
# enddef


@app.get('/shutdown')
def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return {"Прощание": "Процесс сервера GUVICORN остановлен"}
# enddef
print(dir(uvicorn.run))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
# endif
