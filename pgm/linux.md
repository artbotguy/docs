cat <F>                         - show file (work in shell by docker)

cat > <F>                - create file with content
    (input text)
"CTRL"+"D"


ls --inode <F>
ls -la                          - all files
ls -R                           - option flag lists directory tree recursively
ls -r                           - option flag lists files/directories in reverse order
ls -l                           - show folder permissions

ps                              - processes

lsof -i tcp:<PORT>              - show process with port
kill -9 <PID>                   - kill ps (note: everybody working)
pkill -f <PROCESSNAME>          - kill ps (note: not always working)




ps -aux                         - all processes
ps aux | grep <PROCESSNAME>     - info about process

netstat -ntlp              - ports
ifconfig                        - show list net interfaces 


hostname -I                     - local IP's


bash -c <CMD>              - execute cmd (work in folders with permisssions (cat cmd permission denied))
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
rm -rf <FOLDERNAME>
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

apt list --installed
apt show <PACKAGENAME>                      Информация о пакете
---------------------------------------------------------------------------------------------------------------
----------------------------------------------------SUDO-------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

chown <USER?:GROUP> -R  <path>                      - recursive change owner directory     

dpkg -i --force-overwrite <F>   принудительная перезапись, при ошибках совместимости
rm <DIR> -r                             - delete folder with content


---------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
----------------------------------------folder-----------------------------------------------------------------------
mkdir <dir-name>                            - create directory
mkdir -p <dir-name/sub-dir-name>            - create directory with nested directories

mv <from-path/> <to-path/>                    - move (if folder <from-path> - folder name)
(!)    -n                                      - (перемещает, если такого же файла не существует) - работает не так как я думал. Для совмещения папок используется 
                                                                                                    rsync -a src dest
     
                            -i              - not replace
find <WHERE> -type d -name 'httpdocs'       - find dir; WHERE, default / - all system; -name could be -iname to ignore case; also -type is not mandatory; 
du -sh <PATH>                               - disk usage (size folder)
find . -maxdepth 1 -exec mv {} .. \;	    - перепестить содержимое текущей папки на уровень выше

--------------------------------------file-------------------------------------------------------------------
source ~/.bash_profile                      - Execution shell

source <F> [arguments]                      - read and execute file
touch                                       - new file (set last time edit)
chmod <-|+>x <F>                                 - сделать файл (не)исполняемым
chmod <PERM> <PATH>
mv <F> <F>                                  - rename file
nano <F>					                - edit file
---------------------------------------archive------------------------------------------------------------------
tar                                         - archive manager
tar xJf <archive-name> --strip 1            - unarchive (flg === to current directory)
tar xf <archive-name>                       - unarchive .tar.gz

tar -czvf file.tar.gz <DIR1> <optional-DIR2>         - make archive

---------------------------------------------------------------------------------------------------------------
-i                                     Сменить пользователя
cat /etc/passwd                             Список всех пользователей

su -l <USER> -s /bin/bash                   - open shell another user
su -l <USER>                                - swith user

ln -s [OPTIONS] FILE LINK                   символическая ссылка

which <LIB?>                                 - path to

env                                         - env

ufw <CMD>                                   - firewall
ufw allow <PORT>                       - open port 

--------------------------------------------------------atp-get-------------------------------------------------------
-f          fix

sudo apt-get update                         Обновить информацию о том, какие пакеты доступны и откуда
sudo apt-get upgrade                        Обновить пакеты (т. е. «обновить вашу систему»)
sudo apt-get dist-upgrade                   Обновить пакеты, включая пакеты, которые требуют установки неустановленных пакетов или удаления установленных пакетов, запустите это
sudo apt-get install <PACKAGENAME>          Установить пакет
                        --reinstall             -- переустановить пакет, запустите
                        --purge --reinstall     -- переустановить пакет и при этом удалить его общесистемные файлы конфигурации
sudo apt-get remove <PACKAGENAME>           Удалить пакет
sudo apt-get purge <PACKAGENAME>            Удалить пакет, а также удалить его общесистемные файлы конфигурации (но не его файлы конфигурации для каждого пользователя, которые находятся в домашних каталогах пользователей)
sudo apt-get autoremove                     Удалить пакеты, которые были установлены автоматически, потому что они были нужны другим пакетам, но которые теперь больше не нужны
                        --purge                  -- также удалить их глобальные файлы конфигурации
sudo apt-get clean                          Удалить кэшированные .debфайлы установщика пакетов ( ) (которые не удаляют никакие пакеты, но заставляют их снова получать по сети для переустановки)
sudo apt-get autoclean                      Удалить кешированные файлы установщика пакетов, но только для пакетов, которые вряд ли потребуются снова (т. е. те, которые настолько старые, что были удалены с серверов на момент последнего sudo apt-get updateзапуска)


service --status-all
apt --only-upgrade install         - upgrade one package

---

cat /etc/os-release                             - info about os


***

Очистка пространства - https://askubuntu.com/questions/100004/how-can-i-free-space-from-a-massive-39-5gb-var-log-folder

find /var/log -type f -name "*.gz" -exec rm -f {} \;                    - снести старые журналы

journalctl --vacuum-size=100M
journalctl --vacuum-time=10d                                            - доп. очистка

#!/bin/sh
LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' |
while read pkg revision; do
  sudo snap remove "$pkg" --revision="$revision"
done
                                                                        - удалить все неиспользуемые версии пакетов моментальных снимков
