import time, sys, argparse
from chirpsdk import ChirpConnect, CallbackSet


def main(msg, blockname='default'):
    chirp = ChirpConnect(block=blockname)
    chirp.start(send=True, receive=False)
    print("Sending",len(msg),"bytes using",blockname,"configuration.")
    identifier = msg    
    payload = bytearray([ord(ch) for ch in identifier])
    chirp.send(payload, blocking=True)
    
    chirp.stop()

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Send a chirp.')
    parser.add_argument('msg', action='store', type=str,help='string to send') 
    parser.add_argument('-u', action='store_true', default=False, dest='ultrasonic',help='use ultrasonic protocol')
    results = parser.parse_args()
    if results.ultrasonic: 
        main(results.msg, blockname='ultrasonic')
    else: 
        main(results.msg)