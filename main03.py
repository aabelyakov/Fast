# ВНИМАНИЕ
# Использование FastAPI для создания веб-API Python
# https://realpython.com/fastapi-python-web-apis/

import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World!'}
# enddef

# В терминале ввести:
# uvicorn main:app --reload
# uvicorn app.app:app --host 0.0.0.0 --port 8080
# uvicorn app.app:app --reload

# или добавить в текст программы эту конструкцию
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
    # Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# endif

# Запустите браузер по адресу http://127.0.0.1:8000/docs
# FastAPI автоматически создаст полностью интерактивную документацию по API,
# которую вы можете использовать для взаимодействия с вашим новым API.
#

# Запустите браузер по адресу http://127.0.0.1:8000/redoc