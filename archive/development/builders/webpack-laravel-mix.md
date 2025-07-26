Для того, чтобы пути к изображениям (изображения также перестают копироваться при установке в FALSE) и шрифтам не переписывались в обсолютный путь
необходимо добавить
    options({processCssUrls: false})

	mix.sass('assets/src/sass/style.scss', 'assets/dist/css').options({
		processCssUrls: false
	});

Source: https://stackoverflow.com/questions/48048004/how-to-keep-relative-paths-in-css-for-images-and-fonts-in-laravel-mix/48048049#48048049