git config 
git config  --list                                - конфиг лист
git config  --list  --show-origin --show-scope    - показать где установлен конфиг
git config  --global --edit                       - редактировать конфиг
git config  --global --unset <PROP_NAME>          - удалить свойство

git status                                        - проверка staging area (index) (измененных, добавленных фалйлов)

git add <. | FILENAME>                            - подготовить к добавлению в index все файлы | файл
git commit                                        - коммит
git checkout                                      - перейти к определённой ветке/коммиту
              -b  <BRANCHNAME>                    - создать новую ветку и перейти в неё
git log                                           - все коммиты ветки

git branch                                        - все ветки
git branch -a                                     - все ветки (включая удаленные)

            <BRANCHNAME>                          - новая ветка
            -m <NEWBRANCHNAME>                    - переименовать ветку
            -d <BRANCHNAME>                       - удалить ветку (текущую ветку удалить нельзя)
git branch -vv                                    - показывает как связаны ветки (удаленная и локальная)
git merge <FEATUREBRANCHNAME>                     - объединить текущую (receiving) ветку с другой (feature)
git clone <URL>                                   - клонирование удаленного репо в локальный
git pull                                          - из удалённой ветки в локальную
git push                                          - из локальной ветки в удаленную (выполняется когда ветки связаны\/)
  git remote add origin <LINK>                    - подключение удаленного репо
  //после подключения удаленного репо 
  //к локальному, находясь на локальной ветке
  //нужно выполнить команду (после внесения изменений)
  git push -u origin <BRANCHNAME>      

git remote -v                                     - функции удаленного репо        