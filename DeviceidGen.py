from time import time
from requests import get
from pyfiglet import figlet_format
from concurrent.futures import ThreadPoolExecutor
import os
import threading
import hmac
from hashlib import sha1

device_Ids = open("deviceids.txt", "a")

def device_Id_generator():
    try:
        identifier = os.urandom(20)
        x= ("19" + identifier.hex() + hmac.new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"), b"\x19" + identifier, sha1).hexdigest()).upper()

        print(f"device_Id: {x}")
        device_Ids.write(f"{x}\n")
    except BaseException:
        return

while True:
    with ThreadPoolExecutor(max_workers=100) as executor:
        _ = [executor.submit(device_Id_generator) for _ in range(50)]
