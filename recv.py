import time, sys
from chirpsdk import ChirpConnect, CallbackSet

chirp = ChirpConnect()

chirp.start(send=False, receive=True)

# identifier = 'hello'
# payload = bytearray([ord(ch) for ch in identifier])
# chirp.send(payload, blocking=True)

class Callbacks(CallbackSet):
    def on_received(self, payload, channel):
        if payload is not None:
            identifier = payload.decode('utf-8')
            print('Received: ' + identifier)
        else:
            print('Decode failed')

chirp.set_callbacks(Callbacks())

try:
        # Process audio streams
    while True:
        time.sleep(0.1)
        sys.stdout.write('.')
        sys.stdout.flush()
except KeyboardInterrupt:
    print('Exiting')

chirp.stop()