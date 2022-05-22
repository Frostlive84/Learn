import time
import zipfile
import os

target = r'F:\Рисунки'
back_up = r'G:\Python\Backup'
def zip_files(target):
    time_name = time.strftime('%Y%m%d%H%M%S' + '.zip')
    zip_file = zipfile.ZipFile(f'{time_name}', 'w')
    for path, dirs, files, in os.walk(target):
        for file in files:
            rady_file = os.path.join(path, file)
            zip_file.write(rady_file)
    zip_file.close()
    remove_old(back_up)


def remove_old(back_up):
    print('принял')
    days = 3
    time_now = time.time()
    file_old = time_now - 60*60*24*days
    for path, dirs, files in os.walk(back_up):
        for file in files:
            rady_file = os.path.join(path, file)
            file_time = os.path.getctime(rady_file)
            if file_time < file_old:
                print('удаление старых файлов', rady_file)
                #os.remove(rady_file)


zip_files(target)
