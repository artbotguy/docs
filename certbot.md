
sudo nginx -t && sudo systemctl reload nginx

чек сертов
sudo certbot certificates

выпуск
sudo certbot certonly --webroot -w /var/www/html -d sub.sub.abotkin.space

проверка доступа
curl -v http://to-ip.abotkin.space/.well-known/acme-challenge/



права
sudo chown -R www-data:www-data /var/www/html/.well-known
sudo chmod -R 755 /var/www/html/.well-known
`

server {
    listen 443 ssl;
    server_name to-ip.abotkin.space;
    ssl_certificate /etc/letsencrypt/live/to-ip.abotkin.space/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/to-ip.abotkin.space/privkey.pem;
}
server {
    listen 80;
    server_name to-ip.abotkin.space;
	return 301 https://$host$request_uri;  # Редирект с HTTP на HTTPS
    root /var/www/to-ip.abotkin.space/html;
    index index.html;
    location ^~ /.well-known/acme-challenge/ {
        root /var/www/html;
        allow all;
        default_type text/plain;
    }
    location / {
        try_files $uri $uri/ /index.html;
    }
}