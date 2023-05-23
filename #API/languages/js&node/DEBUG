    ОШИБКИ:

        - Бесконечная инициализация в VSCODE

    НАСТРОЙКА:

        Подключение attach debug в Chrome
            Метод 1 (attach):
                [Windows]
                - Необходимо добавить флаги для Chrome открыть свойства и в Target (Объект) добавить флаги: 
                    chrome.exe --remote-debugging-port=9222 --user-data-dir=remote-profile
                - Дописать свойство webRoot - в случае с Docker, когда корневой папкой является не тема, то прописывается путь "${workspaceFolder}/mounts/wp-content/themes/CustomTheme"
                - Запустить Хром из этого ярлыка, открыть localhost:8080, включить отладку

                [Linux]:
                    1 способ (ручной):
                        /usr/share/applications/google-chrome.desktop
                            set (в первом и втором упомянании) 
                                Exec=/some/path/ --remote-debugging-port=9222 --user-data-dir=remote-profile
                    2 способ (приложение):
                        Установить:
                            $ sudo apt-get install menulibre
                        Установить флаг

            Метод 2 (launch):
                - В файл launch.json для конфигурации launch добавить свойство "userDataDir": false
                - Запустить новый экземпляр Chrome
