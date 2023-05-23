    redirect (301 from cache)
        {{CROME}}
                Редирект происходит из-за кеширования.
                Лечится "~Очисткой файлов и изображения" в 
                chrome://settings/clearBrowserData

    {CORS}
        Отключение CORS в Хроме - использование Attach с флагом в ярлыке Хрома: --disable-web-security
        "C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default" --remote-debugging-port=9222 --user-data-dir=remote-debug-profile --disable-web-security
        ||
        Установить расширение CORS Unblock

        прим: попытка получить на клиенте некоторых заголовков (Nonce) может не сработать из-за CORS защиты - оги отображаются
            в chrome devtools/network, но к ним нет доступа. Для обеспечения доступа нужно поставить флажок в CORS Unblock
            или настроить сервер:
                file:///home/artbot/Documents/aboutHeaders.txt || https://stackoverflow.com/questions/37897523/axios-get-access-to-response-header-fields
    
    Некорректное отображение в Chrome при режиме Device Toolbar - необходимо установить верные атрибуты во viewport:
        <head>
	        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0" />
        </head>
                