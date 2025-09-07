import os
from datetime import datetime

# path = os.path.curdir
# print(path)
# print(os.path.commonpath(path))
# print(os.listdir(path))


# print(datetime.now().time())


current_path = os.path.curdir
list_of_files = os.listdir(current_path)
string1 = f'Все файлы: {"\n".join(list_of_files)}'
print(string1)