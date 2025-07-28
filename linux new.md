
# VIM
{ echo 'export SYSTEMD_EDITOR=vim'; cat ~/.bashrc; } > ~/.bashrc.tmp && mv ~/.bashrc.tmp ~/.bashrc

И затем **sudo visudo** добавьте эту строку:
Defaults  env_keep += "SYSTEMD_EDITOR"
или
echo 'Defaults env_keep += "SYSTEMD_EDITOR"' | sudo tee /etc/sudoers.d/env_keep_systemd_editor