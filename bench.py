import time, sys, argparse
from chirpsdk import ChirpSDK, CallbackSet

def init(blockname='default'):
    chirp = ChirpSDK(block=blockname)
    chirp.start(send=True, receive=True)
    print("Sending",len(msg),"bytes using",blockname,"configuration.")
    identifier = msg    
    payload = bytearray([ord(ch) for ch in identifier])
    chirp.send(payload, blocking=True)
    
    chirp.stop()