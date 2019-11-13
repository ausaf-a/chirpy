import time, sys, argparse
from chirpsdk import ChirpSDK, CallbackSet, CHIRP_SDK_STATE
import chirpsdk
import time

timeSent = -1

class Callbacks(CallbackSet):

    def on_state_changed(self, previous_state, current_state):
        if current_state == chirpsdk.CHIRP_SDK_STATE_STOPPED:
            print("ChirpSDK has stopped")

    def on_sending(self, payload, channel):
        print('Sending data...')

    def on_sent(self, payload, channel):
        print('Sent data')

    def on_receiving(self, channel):
        print(time.time() - timeSent, 'seconds')
        print('Receiving data...')

    def on_received(self, payload, channel):
        print(time.time() - timeSent, 'seconds')
        if payload is None:
            print('Decode failed')
        else:
            print('Received data')

def init(blockname='default'):
    global timeSent 
    
    chirp = ChirpSDK(block=blockname)
    chirp.start(send=True)

    chirp2 = ChirpSDK(block=blockname)
    chirp2.input_sample_rate = 48000 #USB mic requires 48Khz to function
    chirp2.start(send=False, receive=True)
    chirp2.set_callbacks(Callbacks())

    msg = 'hello darkness'
    payload = bytearray([ord(ch) for ch in msg])
    print("Sending",len(msg),"bytes using",blockname,"configuration.")    
    
    timeSent = time.time()
    chirp.send(payload, blocking=False)
    
    while True: 
        time.sleep(0.1)
    chirp.stop()
    chirp2.stop()
init()