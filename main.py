from functions import *

""" Todas as funções utilizadas no programa estão no arquivo functions.py.
As variáveis abaixo definem os caminhos para os diretórios onde serão lidos e salvos os dados.
Os caminhos utilizados no código se referem à máquina onde o código foi desenvolvido, bastando alterar a variável
onde o caminho está salvo para se adequar à necessidade do momento """

from_folder = '/Users/fabiolopes/Documents/estagio/home/valcann/backupsFrom'
to_folder = '/Users/fabiolopes/Documents/estagio/home/valcann/backupsTo'
path_to_log_from = '/Users/fabiolopes/Documents/estagio/home/valcann/backupsFrom.log'
path_to_log_to = '/Users/fabiolopes/Documents/estagio/home/valcann/backupsTo.log'

""" As funções abaixo realizam as ações requisitadas
list_files_in_path_and_log lista os arquivos no caminho determinado e já escreve no log as informações
delete_files_older_than_3_days remove arquivos com tempo de criação superior a 3 dias
copy_files_from_backup realiza a cópia solicitada
log_copy_to salva em log as informações dos arquivos copiados """

list_files_in_path_and_log(from_folder, path_to_log_from)
delete_files_older_than_3_days(from_folder)
copy_files_from_backup(from_folder, to_folder)
log_copy_to(to_folder, path_to_log_to)
