# впн без GUI на убунту

# базовая жизнеспособность

sudo bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install

sudo vim /usr/local/etc/xray/config.json


далее сляпано дипсиком из: 
vless://ed3d55f3-3abb-4d71-a69a-5773c1b259a1@77.105.140.246:443?security=reality&type=tcp&flow=xtls-rprx-vision&sni=moktana.digital&fp=chrome&pbk=fzGsSpDuugv69pczDu9yoOktMKSHwehoinV42va8lUk&sid=284ed4ac975d2114#🇳🇱 Нидерланды — CacaoVPN

{
  "inbounds": [
    {
      "port": 1080,
      "listen": "127.0.0.1",
      "protocol": "socks",
      "settings": {
        "udp": true
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vless",
      "settings": {
        "vnext": [
          {
            "address": "77.105.140.246",
            "port": 443,
            "users": [
              {
                "id": "ed3d55f3-3abb-4d71-a69a-5773c1b259a1",
                "flow": "xtls-rprx-vision",
                "encryption": "none"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "serverName": "moktana.digital",
          "fingerprint": "chrome",
          "publicKey": "fzGsSpDuugv69pczDu9yoOktMKSHwehoinV42va8lUk",
          "shortId": "284ed4ac975d2114"
        }
      }
    }
  ]
}

sudo systemctl restart xray
sudo systemctl status xray
