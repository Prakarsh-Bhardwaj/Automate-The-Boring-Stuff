import os
import zipfile
import shelve

def zipdir(path, ziph):
    for root, _ , files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile('zipfile_1.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('../../../Projects', zipf)
zipf.close()
        