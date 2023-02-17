import datetime
import os
import time
import shutil

""" O problema fala especificamente de listagem de arquivos. Dessa forma, essa versão do código que escrevi considera
que no diretorio 'backupsFrom' encontraremos apenas arquivos e não subdiretórios. Entendo que em um cenário real
isso pode trazer problemas, mas algumas alterações na lógica do código já os resolveriam. """


def list_files_in_path_and_log(path_to_folder, path_to_log):
    with open(path_to_log, 'w') as log_file:
        for entry in os.scandir(path_to_folder):
            if os.path.isfile(entry):
                log_file.write('File name: ' + os.path.basename(entry) + ' | ')
                print('File name: ' + os.path.basename(entry) + ' | ')
                log_file.write('Size: ' + str(os.path.getsize(entry)) + 'KB' + ' | ')
                print('Size: ' + str(os.path.getsize(entry)) + 'KB' + ' | ')
                date_creation = os.path.getctime(entry)
                date_converted = time.ctime(date_creation)
                log_file.write('Date of creation: ' + date_converted + ' | ')
                print('Date of creation: ' + date_converted + ' | ')
                date_modified = os.path.getmtime(entry)
                modified_converted = time.ctime(date_modified)
                log_file.write('Last modified: ' + modified_converted + '\n')
                print('Last modified: ' + modified_converted + '\n')


def delete_files_older_than_3_days(folder_path):
    now = datetime.datetime.now()
    days_ago = now - datetime.timedelta(days=3)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_modified_time < days_ago:
                    os.remove(file_path)


def copy_files_from_backup(source, destination):
    for entry in os.scandir(source):
        if os.path.isfile(entry):
            shutil.copy(entry, destination)


def log_copy_to(path_to_folder, path_to_log):
    with open(path_to_log, 'w') as log_file:
        for entry in os.scandir(path_to_folder):
            log_file.write('File name: ' + os.path.basename(entry) + ' | ')
            log_file.write('Size: ' + str(os.path.getsize(entry)) + 'KB' + ' | ')
            date_creation = os.path.getctime(entry)
            date_converted = time.ctime(date_creation)
            log_file.write('Date of creation: ' + date_converted + ' | ')
            date_modified = os.path.getmtime(entry)
            modified_converted = time.ctime(date_modified)
            log_file.write('Last modified: ' + modified_converted + '\n')
