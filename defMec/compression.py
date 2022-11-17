import os
import zipfile

directory = "../../testing/cosc469-testing-data"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with zipfile.ZipFile(f[:len(f)-3]+"zip", 'w') as jungle_zip:
            jungle_zip.write(f, compress_type=zipfile.ZIP_DEFLATED)
    