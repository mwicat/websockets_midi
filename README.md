# websockets_midi

This is my example project that shows how can you join websockets
functionality with local MIDI communication, thus creating remote
MIDI controller through web browser.

## Components

### Server

- Python interpreter
- Flask web framework
- Flask-SocketIO extension

### Client

- Socket.IO client library
- jQuery

## Running

1. Install dependencies

```shell script
pip3 install --user pipenv
pipenv install
```

2. Start server

```shell script
./serve.sh
```

3. Open [http://localhost:5000/]() in web browser.

## TODO

- Implement audio/video transfer like https://github.com/paranerd/simplecam
