import os
import psutil
from matplotlib import pyplot as plt
from time import sleep
from base64 import b64encode

i=0

# def rw_file():
#     global i
#     i += 1
#     iocnt = psutil.disk_io_counters()
#     print(iocnt.read_count)
#     with open("aaaa" + str(i % 100), "w") as f:
#         f.write("b" * i)
#         f.flush()
#         os.fsync(f.fileno())
        
#     with open("aaaa" + str(i % 100), "r+") as f:
#         test = f.read()
#         f.seek(0)
#         f.write(b64encode(test.encode('utf-8')).decode('utf-8'))
#         f.flush()
#         os.fsync(f.fileno())

#     sleep(0.5)



# t = 60
reads = []
writes = []
iocnt0 = psutil.disk_io_counters(perdisk=True)['PhysicalDrive1']
iread = iocnt0.read_count
iwrite = iocnt0.write_count
for _ in range(60):
    # rw_file()
    sleep(1)
    iocnt1 = psutil.disk_io_counters(perdisk=True)['PhysicalDrive1']

    reads.append( iocnt1.read_count - iread)
    writes.append(iocnt1.write_count - iwrite)    
    
print(reads)
print(writes)
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].scatter(range(len(reads)), reads,color='red')
axs[0].plot(range(len(reads)), reads)
axs[0].set_title("read")
axs[1].scatter(range(len(writes)), writes,color='blue')
axs[1].plot(range(len(writes)), writes)
axs[1].set_title("write")

plt.show()

max_read = 1
max_write = 1

if (all(item < max_read for item in reads)) and (all(item < max_write for item in writes)):
    print("This is a completely legitimate program. No malware round this way.")
else:
    print("AYO PAUSE. THIS SOFTWARE IS SUSPICIOUS AF!!!")




