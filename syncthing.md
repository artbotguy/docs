==MAC==

Полная переустановка Syncthing с чистого листа
1. Остановка и удаление текущей версии

# Остановка службы
sudo systemctl stop syncthing@syncthing

# Удаление конфигурации и данных
sudo rm -rf /home/syncthing/.config/syncthing/

# Удаление пакета (если установлен через apt)
sudo apt purge syncthing -y
sudo apt autoremove -y
2. Удаление пользователя (опционально)

sudo userdel -r syncthing
3. Переустановка Syncthing

# Добавление репозитория
curl -s https://syncthing.net/release-key.txt | sudo apt-key add -
echo "deb https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
sudo apt update

# Установка
sudo apt install syncthing -y
4. Создание пользователя и папок

# Создаем пользователя без пароля
sudo adduser --disabled-password --gecos "" syncthing

# Создаем папку для синхронизации
sudo mkdir -p /home/syncthing/Sync
sudo chown -R syncthing:syncthing /home/syncthing
5. Настройка systemd-службы

sudo systemctl edit --full syncthing@syncthing
Вставьте конфигурацию:

[Unit]
Description=Syncthing for %i
After=network.target

[Service]
User=%i
ExecStart=/usr/bin/syncthing serve --no-browser --no-restart --logflags=0
Restart=on-failure
Environment=STNORESTART=1

[Install]
WantedBy=multi-user.target

1. Запуск и генерация конфига (ДОПИСЫВАЛ САМ)
    ; Возможно нужно создать папки вручную и конфиг:
    mkdir -p /home/syncthing/.config/syncthing
    chown -R syncthing:syncthing /home/syncthing/.config

    su - syncthing -c "syncthing -generate=/home/syncthing/.config/syncthing"
    ; 2025/07/17 06:14:01 INFO: Generating ECDSA key and certificate for syncthing...
    ; 2025/07/17 06:14:01 INFO: Device ID: HOK6GUP-NHFQ5WM-5QAA7ZF-UZ4KAWQ-MYVZ3TQ-GYAHNRT-RDT4IMH-RWIKAAD
    ; 2025/07/17 06:14:01 INFO: Default folder created and/or linked to new config

    ; Меняем:
    vim /home/syncthing/.config/syncthing/config.xml
        <gui enabled="true" tls="false">
            <address>0.0.0.0:<PORT></address>
        </gui>

    ; Установите правильные права:
    chown -R syncthing:syncthing /home/syncthing/.config/syncthing

    sudo systemctl restart syncthing@syncthing

2. Открытие портов

sudo ufw allow 8384/tcp
sudo ufw allow 22000/tcp
sudo ufw reload
