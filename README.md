# PP_laba
на macos -
відкриваємо термінал та пишемо наступні команди через enter :
  brew install pyenv
  
  pyenv install 3.8.0
  
  python install pip
  
  pip install --user pipenv
  
що відбулось :
скачалась pyenv
pyenv — утилита, яка позволяє легко переключатися між версіями Python.
скачалсь потрібна версія путона,
скачався пакунок pip,
pip is the package installer for Python.
скачався pipenv,
Pipenv — це набираючий популярність пакет управління віртуальним середовищем для Python, який вирішує деякі проблеми, связані з типовим робочим процесом.
  python3 --version
  pip3 --version
ці дві команди в терміналі покажуть версію путона та піп.
  py -m site --user-site
команда повертає шлях до каталогу користуватських пакетів сайту
  ~ / .bashrc
строка відкриває потрібний нам файл в який ми прописуємо 
  export PATH="$PATH:/home/[YOUR_USER_NAME]/.local/bin"

переходимо в каталог нашого проекта та запускаємо :
  pipenv --python 3.8.5
як альтернатива може бути 
  pipenv --three //версія путона 3
  

активуємо віртуальне середовище
  pipenv shell
  
