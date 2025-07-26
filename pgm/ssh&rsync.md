ssh -tt                         - fix...

scp -r /path/to/local/dir user@remotehost:/path/to/remote/dir         		- очень долго

rsync -avz -e 'ssh' /src/* user@remotehost:/dest     
	- важно указать конечную папку - копирует директорию src в dest,
		поэтому, если нужно скопировать содержимое папки, то необходимо указывать /src/*

		Пример:
			rsync -avz -e 'ssh' /home/artbot/dev/wp-docker-apache/html/* abobus5j@abobus5j.beget.tech:/home/a/abobus5j/abobus5j.beget.tech/public_html 

https://askubuntu.com/questions/446724/copy-folders-not-one-file-using-ssh-ubuntu

