import os
import signal
import fastapi
import uvicorn

app = fastapi.FastAPI()


def hello():
    return fastapi.Response(status_code=200, content='Hello, world!')


def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return fastapi.Response(status_code=200, content='Server shutting down...')


@app.on_event('shutdown')
def on_shutdown():
    print('Server shutting down...')


app.add_api_route('/hello', hello, methods=['GET'])
app.add_api_route('/shutdown', shutdown, methods=['GET'])

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
