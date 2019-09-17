import time, sys, argparse
from chirpsdk import ChirpConnect, CallbackSet

class Callbacks(CallbackSet):
    def on_received(self, payload, channel):
        if payload is not None:
            identifier = payload.decode('utf-8')
            print('Received: ' + identifier)
        else:
            print('Decode failed')

def main(blockname='default'):
    chirp = ChirpConnect(block=blockname)
    chirp.start(send=False, receive=True)
    chirp.set_callbacks(Callbacks())

    try:
        print("SDK initialized successfully. Using",blockname,"configuration.")
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Exiting')

    chirp.stop()

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Listen for chirps.')
    parser.add_argument('-u', action='store_true', default=False, dest='ultrasonic',help='use ultrasonic protocol')
    results = parser.parse_args()
    if results.ultrasonic: 
        main(blockname='ultrasonic')
    else: 
        main()