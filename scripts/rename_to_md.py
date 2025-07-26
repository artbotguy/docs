import os

def rename_files_to_md(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            name, ext = os.path.splitext(filename)
            
            # Проверяем, есть ли расширение или это .txt файл
            if not ext or ext.lower() == '.txt':
                new_filename = name + '.md'
                new_file_path = os.path.join(dirpath, new_filename)
                
                # Переименовываем файл
                os.rename(file_path, new_file_path)
                print(f'Переименован: {file_path} -> {new_file_path}')

if __name__ == '__main__':
    directory = input('Введите путь к директории: ')
    if os.path.isdir(directory):
        rename_files_to_md(directory)
        print('Готово!')
    else:
        print('Указанная директория не существует.')