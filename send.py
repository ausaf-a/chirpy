import time, sys
from chirpsdk import ChirpConnect, CallbackSet

chirp = ChirpConnect()

chirp.start(send=True, receive=False)


while True: 
    identifier = input('Enter message: ')    
    if identifier == 'q': 
        break
    payload = bytearray([ord(ch) for ch in identifier])
    chirp.send(payload, blocking=True)



chirp.stop()