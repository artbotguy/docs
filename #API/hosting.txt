{{BEGET}}
    cкрипты на python, на вирт. хостинге возможно запустить только из виртуального окружения Docker, 
    но т.к. для входа в docker требуется ввод пароля, нужно сначала пробросить в него ключ. 
    Подключитесь на аккаунт по ssh. Затем выполните

    $ ssh-keygen -t rsa
    Нажимаем enter, пока ключ не будет сгенерирован. Пробрасываем его в докер командой

    $ ssh-copy-id '-p222 -i ~/.ssh/id_rsa.pub  localhost'
    Вводим свой пароль от аккаунта. Если все сделано верно, теперь вход в докер будет происходить 
    без ввода пароля, проверьте выполнив команду ssh localhost -p222

    В задании для crontab, перед вводом нужной нам команды указываем ssh localhost -p222, например

    $ ssh localhost -p222 node -v
    
    $ npm <cmd> --prefix /path - для запуска npm по пути
    
    $ ssh localhost -p222 npm run generate --prefix ~/amogusxj.beget.tech/public_html/wp-content/themes/logotype-ssg/vue-vite-ssg