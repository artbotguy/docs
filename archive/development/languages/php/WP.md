
Невозможность загружать изображения больших размеров:
    Установить в .htaccess
        php_value upload_max_filesize 50M
        php_value post_max_size 50M
        php_value max_execution_time 300
        php_value max_input_time 300

???

    Ошибка подключения к db вордпресса после установки новой версии.
    Вместо установки констант в .env установил в wp-config.php (примечание: из коробки
    докер-вордпресс имеет wp-config-example.php стандартную настройку, я поставил ту, в которойпроисходит переопределение docker_env
    но и это не помогло. Поэтому поставил мои данные как дефолтные) 




Причниы НЕ подключения скриптов/стилей:
    - отсутствуют зависимости
    - wp_deregister_script() из-за невыясненных несоответствий - например, с jquery





{{Перенос на хостинг}}:
    - установка правильной версии PHP

    - установка в wp-config.php:
        - DB_HOST - localhost
        - убедиться в том, что в wp-config.php установлены WP_HOME и WP_SITEURL
        
    - почистить Cache images and files

    (ОПЦИОНАЛЬНО)
    - заменить ссылки с помощью плагина Update URL (актуально для Logotype SSG)


    ***

    - критическая ошибка:
        - отключить плагины, ТЕМУ

    - ошибки импорта бд:
        - убедиться, что экспортируется правильная бд (база, а не таблица)

    - 
        https://stackoverflow.com/questions/58931144/enqueue-javascript-with-type-module


TROUBLESHOOTING

    Error include styles (admin panel)
        db/options/siteurl: http://<siteurl>/
        
	[cURL] 
		В wordpress docker вызов php curl из пакета automattic/woocommerce приводил
		к ошибкам. Connection refused, timeout etc. 
		Ошибки возникали в файле functions.php. Вызов в клиентском классе решил проблему

    Ошибка с подключение скриптов - скрипты регистрируются и подключаются, но не включаются
        - отключить wp_deregister_script('jquery');



    {{WOOCOMMERCE}}
        401 error woocomerce:
        ошибка из-за неправильного хоста в админке wordpress - изменил с //localhost на http://localhost 
        usr/local/etc/php-fpm.d/www.conf

        подключение стилей и скриптов:
            пути, которые использутся при навигации в каталоге файлов и для подключения файло разные
            - для фалового дерева (например для поиска и подклюючения файлов) используются такие функции как 
            get_stylesheet_directory() (путь получится: http://example.com/var/wwww/html/wp-content/themes/my-theme/my-theme-script.js.) и ей подобные
            - для подключения файлов - get_template_directory_uri() (путь получится: http://example.com/wp-content/themes/my-theme/my-theme-script.js.)

