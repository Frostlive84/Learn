import time
import zipfile
import os


time_name = time.strftime('%Y%m%d%H%M%S' + '.zip')
zip_file = zipfile.ZipFile(f'{time_name}', 'w')
for puts, dirs, files, in os.walk('F:\Рисунки'):
    for file in files:
        rady_file = os.path.join(puts, file)
        zip_file.write(rady_file)
zip_file.close()
