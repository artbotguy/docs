	Ошибка с циклическими зависимостями:
		https://github.com/vitejs/vite/issues/3033#issuecomment-1360691044
		
		defineConfig.plugins: [      
		{
			name: "singleHMR",
			handleHotUpdate({ modules }) {
			  modules.map((m) => {
			    m.importedModules = new Set();
			    m.importers = new Set();
			  });
			  return modules;
        		},
      		},]
          
---------------------------------------------------------------------------------------


{{ESLint (для Vite)}}
  - установить расширения vscode:
                                                                  (х - отказался)- Prettier
                                                              (?) установить плагин (мб не надо)
                                                          $ npm install eslint-config-prettier --save-dev
      - ESLint
      - Vetur 
          конфиг, чтобы не конфликтовал и передал управление шаблоном: 
              "vetur.validation.template": false,

  - установить с сайта https://eslint.org/
      $ npm init @eslint/config

  Настройка .eslintrc.
      - ошибка разрешения пути (Unable to resolve path to module) https://github.com/kriasoft/react-starter-kit/issues/1180
          - пофиксил(убил) 
              rules: {"import/no-unresolved": "off",}
          - есть вариант решения с помощью установки плагинов, который не получилось реализовать
      - не работает конфиг - проверить output
    - для форматирования стилей в SFC можно воспользоваться @vue/eslint-config-prettier
      https://stackoverflow.com/questions/67191678/is-it-possible-to-use-eslint-to-format-the-style-in-a-vue-component
      https://stackoverflow.com/questions/71207427/syntax-error-error-failed-to-load-config-vue-prettier-to-extend-from
