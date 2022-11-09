import datetime
import os
import sys

import frida

def on_message(message, data):
    if 'payload' in message:
        payload = message['payload']
        if isinstance(payload, dict):
            if payload['type'] == 'httpx':
                print (datetime.datetime.now(), 'http', payload['source'], payload['method'], payload['url'].split('?')[0])
            else:
                print (datetime.datetime.now(), payload)
        else:
            print (datetime.datetime.now(), payload)

    else:
        print (datetime.datetime.now(), 'on_message', message, data)

def run():
    # clear_app()
    # os.system('adb shell killall com.oppo.market\'"')
    device = frida.get_usb_device(100)
    pid = device.spawn(['com.taobao.taobao'])
    process = device.attach(pid)
    # process = frida.get_usb_device(100).attach('com.taobao.taobao')
    with open(os.path.join('trace.js'), 'r') as f:
        code = f.read()
    script = process.create_script(code)
    script.on('message', on_message)
    script.load()
    device.resume(pid)
    sys.stdin.read()


if __name__ == '__main__':
    print (datetime.datetime.now())
    run()
