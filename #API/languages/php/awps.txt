1. Заполнить wp-config.php константами из окружения docker. Он должен находиться в /var/www/html - так DotEnv(__DIR__) получит к нему доступ в wpconfig

2. Перед запуском composer
	$ sudo apt install php-xmlwriter (если не установлен)

***

При нерабочем HotReplacement необходимо проверить, везде ли есть соответсвие между
подлючаемым файлом из webpack.mix.js и функцией mix()
Так обновление стилей может не работать, если app.js используется в mix(), но не подкючен в 
webpack.mix.js
