import os
import psutil
from time import sleep
from base64 import b64encode
i = 0
while True:
    i += 1
    iocnt = psutil.disk_io_counters()
    print(iocnt.write_count)
    with open("aaaa" + str(i % 100), "w") as f:
        f.write("b" * 30)
        f.flush()
        os.fsync(f.fileno())
        
    with open("aaaa" + str(i % 100), "r+") as f:
        test = f.read()
        f.seek(0)
        f.write(b64encode(test.encode('utf-8')).decode('utf-8'))
        f.flush()
        os.fsync(f.fileno())

    sleep(0.5)
