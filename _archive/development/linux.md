


## при установке


#### NODE 
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
    (if error install)
curl -fsSL <link>
sudo dpkg -i --force-overwrite /var/cache/apt/archives/<archive-name>
sudo apt -f install
sudo apt update
sudo apt dist-upgrade

#### NODE устанавливаем на виртуалку
(!!! - может возникать ошибка несовместимости хостинга - исплользовать 16 node))
(!) - работает (ОДИН РАЗ - если установить сразу, затем после переустановки находит и запускает - мб зависит от настройки .bashrc), но установка node_modules не происходит по команде

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash

    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    
    nvm install 16

        ***если bin/node which другой путь***
        ~/.bashrc
            PATH=/home/a/amogusxj/.nvm/versions/node/v16.19.1/bin/node:$PATH

#### NODE -ИСПОЛЬЗЕТСЯ- Passanger... (попытки использования с CronTab не увенчались успехом) (по туториалу beget)
    Переходим в окружение docker
    cd ~/.local 
    wget https://nodejs.org/dist/v17.9.1/node-v17.9.1-linux-x64.tar.xz 
    tar xJf node-v17.9.1-linux-x64.tar.xz --strip 1


PATH=/home/a/anyaaa6t/.local/bin/node:$PATH
PATH=/home/a/anyaaa6t/.local/bin/npm:$PATH


#### NODE dockerfile
    (1)
        RUN apt-get update && apt-get install -y \
            software-properties-common \    
            npm
        RUN npm install npm@latest -g && \
            npm install n -g && \   
            n latest   

    (2) 
        ENV NODE_VERSION=16.13.0
        RUN apt install -y curl
        RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        ENV NVM_DIR=/root/.nvm
        RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
        RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
        RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
        ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
        RUN node --version
        RUN npm --version 


## NODE UTILITES
BASH SCRIPT COMMAND

Only you - $HOME/.local/bin (As per the XDG Base Directory Specification)
You and other local users - /usr/local/bin
root only - /usr/local/sbin

example:
    #!/usr/bin/expect

    set timeout 20

    set cmd [lrange $argv 1 end]
    set password [lindex $argv 0]

    eval spawn $cmd
    expect "password:"
    send "$password\r";
    interact
    Put it to /usr/bin/exp, So you can use:

    exp <password> ssh <anything>
    exp <password> scp <anysrc> <anydst>



*****************************
AFTER INTSALL
*****************************

1. install:
    nettools
2. settings:
    - disable password root: 
        $ sudo visudo
        # add in end file
            $USER ALL=(ALL) NOPASSWD: ALL 

3. {{Chrome}}
    - set debug flag
    - disable "Use hardware acceleration when available"


***********************************************************************


{{OS}}
    Не показывает boot loader (load Windows)
    fix: 
        in Linux terminal (installed Linux system)

        $ sudo efibootmgr
        // showing boot order
        $ sudo efibootmgr -o <NUMBER_BOOT_OPT_0,NUMBER_BOOT_OPT_1,...>
        //
        restart