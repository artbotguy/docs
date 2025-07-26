INSTALL
    1. check php info, {ctrl + c}
    2. {ctrl + v} to xdebug.org
    3. Настройка 

    Also:
        xdebug_info();      - show errors

    P.S.
        Xdebug that connects to IDE and NOT other way around

            F5 - start debug, xdebug trying listen 
                Order requests xdebug:
                1. if xdebug.discover_client_host=true 
                    - try connect with address found in the HTTP headers
                2  else 
                    - try to connect xdebug.client_host


TROUBLESHOTTING
  - ошибка подключения, связанная с тем, что php-fpm имеет директиву clear_env,
    которую нужно выключить (я сделал это в .env, главном для wordpress контейнера):
    clear_env=off

    (LINUX) - not connect
        - check Firewall (!), if it not get allow
            $ sudo ufw allow 9003
