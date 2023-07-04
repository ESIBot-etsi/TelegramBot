# TelegramBot
Bot de esibot de Telegram 

# Instalación
**Es imperativo que se instale en linux, no por nada sino porque todos lo estamos desarrollando en Linux**

- Arch
  ```
  sudo pacman -S python python-pip python-virtualenv
  ```
- Debian
  ```
  sudo apt install python3 python-is-python3 python3-pip
  ```
- Para desarrollar:
  El editor ya es cosa tuya, yo uso tanto neovim (usando NvChad) como vscode. Para neovim te recomiendo que veas el siguiente [video](https://www.youtube.com/watch?v=4BnVeOUeZxc).
  Una vez apañado el editor, debemos establecer el entorno virtual:
  ```
  virtualenv telebot
  ```
  Creamos el entorno virtual llamado telebot donde vamos a instalar las dependencias pertinentes, para ello haremos lo siguiente, entro del directorio de trabajo:
  ```
  source telebot/bin/activate
  pip install -r requirements.txt
  ```
Ya podriamos hacer lo que quisieramos aqui y para terminar solo tenemos que escribir:
```
  deactivate
```

Para volver a desarrollar sin instalar todo solo necesitas: 
```
source telebot/bin/activate
deactivate
```
