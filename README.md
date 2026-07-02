# CoAP Time Server & Client

A minimal CoAP (Constrained Application Protocol) demo using [`aiocoap`](https://aiocoap.readthedocs.io/): an observable time resource that clients can subscribe to and receive live updates from, without repolling.

## What it does

- **`CoAPTimeServer.py`** — runs a CoAP server exposing an observable `/time` resource. Every 2 seconds it pushes the current time (`HH:MM:SS`) to any subscribed clients.
- **`CoAPClientObserveRequest.py`** — subscribes ("observes") the `/time` resource and prints each notification as it arrives.

This demonstrates CoAP's `Observe` option, which lets a client register interest in a resource once and then receive push updates, similar to a lightweight pub/sub pattern for constrained IoT devices.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install aiocoap
```

## Usage

In one terminal, start the server:

```bash
python3 CoAPTimeServer.py
```

In a second terminal, run the client:

```bash
python3 CoAPClientObserveRequest.py
```

### Example output

Server:

```
CoAP server is running at coap://127.0.0.1:5683/time (observable)
```

Client:

```
Client subscribed to coap://127.0.0.1:5683/time
Notification: 11:17:28
Notification: 11:17:30
```

## License

MIT
