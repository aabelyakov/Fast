# Запустить сервер GUVICORN, получить сообщение {"detail":"Not Found"},
# так как маршрут "/" (конечная точка или endpoint) не обрабатывается.
# Отправить запрос по маршруту /shutdown и остановить сервер GUVICORN.


import uvicorn
import os
import signal
from fastapi import FastAPI

app = FastAPI()


@app.get('/shutdown')
def shutdown():
    # Получить идентификатор текущего процесса сервера и отправить этому
    # процессу сигнал останова TERMINATE
    os.kill(os.getpid(), signal.SIGTERM)
    return {"Прощание": "Процесс сервера GUVICORN остановлен"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
