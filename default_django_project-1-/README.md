# default_django_project-1-

В .gitignore не забыть добавить (удостовериться в наличии) файл базы данных, папку виртульаного окружения (если она в папке проекта) и папку настроект среды разработки



Создать requirements.txt (или Pipfile + Pipfile.lock в зависимости от используемого)



Создать django приложение catalog (python manage.py startapp <app_name>) и добавить его в INSTALLED_APPS



Убедиться что SECRET_KEY будет взят из переменных окружения и НЕ будет храниться в репозитории (os.environ.get("SECRET_KEY", "<def value>"))

