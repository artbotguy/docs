Отключил встроенную обработку статики во flask

добавил новый формат заголовков




TODO
location / {
    valid_referers none blocked server_names ~.abotkin.space;
    if ($invalid_referer) {
        return 403;
    }
}