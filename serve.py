from app.server import app


if __name__ == "__main__":
    print('starting server...')
    app.run(host='0.0.0.0', port=8000)
