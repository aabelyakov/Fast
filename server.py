import os
import signal
import fastapi
import uvicorn

# print(dir(fastapi))

app = fastapi.FastAPI()

# print(dir(app))

def hello():
    return fastapi.Response(status_code=200, content='Hello, world!')


def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return fastapi.Response(status_code=200, content='Application shutdown complete')


app.add_api_route('/hello', hello, methods=['GET'])
app.add_api_route('/shutdown', shutdown, methods=['GET'])

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
