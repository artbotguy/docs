devServer
    для работы нужен html файл, который должен лежать по пути, указаному в devServer.static

TROUBLESHOOTING

  Ошибка полифилов Cannot read properties of undefined (reading 'call')
  https://stackoverflow.com/questions/70398678/i-tried-to-polyfill-modules-in-webpack-5-but-not-working-reactjs

  Необходимо установить в вебпак fallback:
          fallback: {
              stream: require.resolve('stream-browserify'),
          },


  Если не подключается что-то, мб некорректный путь. Это связано с тем, что в webpack
  указан publicPath. Установил путь /. Таким образом главный js и html файлы лежат в папке,
  относительно которой должны располагаться другие папки

--------------------------------------------------------

    [0]
        Ошибка связанная с путями файлов во vue
        ! настройка webpack:

            output: {
                path: path.resolve(__dirname, 'assets/all'),
                filename: 'index.bundle.js',
                publicPath: '/',
            },
            devServer : {
                static: path.join(__dirname, "./assets/all"),
                historyApiFallback: {
                    // index: 'assets/all/index.html'
                    rewrites: [
                    { from: /^\/.*/, to: 'index.html' },
                    ],
                },
            }

        пояснение:
            используемый файл index.html, подключаемый к нему index.bundle.js 
            в разработке также используются, при этом не записываясь на диск

            использование путей возможно благодаря настройке вебпака,
            в которой любые пути перенаправляются на главный файл index.html

    [1]
        {{prerender-spa-plugin}} 
            [0]
                ошибка:     [prerender-spa-plugin] Unable to prerender all routes!
                            
                причина:    оффициальная версия плагина пепрестала поддерживаться

                решение:    использовать @dreysolano/prerender-spa-plugin || prerender-spa-plugin-next

            [1]
                наличие плагина определяет, каким будет index.html, который возвращает
                HTMLWebpackPlugin - если сабж присутсвует, то содержимое узла #app
                будет заполненным содержимым страницы с путём '/'

            [2] ошибка, связанная с НЕзаполнением содержимого mount-элемента vue.
                получалось вывести все необходимые пути-файлы, но содержимое #app
                оказывалось пустым
                createWebHistory()

            [3] неразрешенная ошибка: 
                плагин не работает если в компоненте присутвуют некоторые import,
                например, импорт компонента, такая же ошибка возникает при импорте routes 


--------------------------------------------------------

Проблема с Неотображением стилей в dev сборке. Конечным и КЛЮЧЕВЫМ решением было изменение sideEffect
    ***
    Возможные решения (ответ https://stackoverflow.com/questions/63770142/webpack-not-loading-vues-single-file-components-css)
    в webpack.config.js
    1) Добавить esModule: false к css-loader варианту. 
    2) Изменить vue-style-loaderна style-loader в webpack.config.js. (как ответ @seiluv)
    в пакете.json
    3) Добавить "*.vue"в{sideEffects: []}
    См.: https://github.com/vuejs/vuepress/issues/718#issuecomment-412345448 и https://stackoverflow.com/a/53737250/493168.
    ***
    1 и 2 решение не оказываеют особого влияния

    SideEffect в false ВЫЗЫВАЕТ ЭТУ ПРОБЛЕМУ

(.) - а так же - я убрал   "sideEffects": [
                                "**/*.css"
                            ],
