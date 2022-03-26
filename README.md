# alexsashka_main_rep
1. первым делом при начале работы перейти в проект : $ сd *название проекта* (без звездочек)

2. затем конфигурировать имя пользователя и адрес электронки: 
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

3. для того чтобы git начал отслеживать изменения в файле надо добавить его:
$ git add file_name.md

4. для того чтобы зафиксировать изменения в проекте надо создать коммит, а флаг -m позволяет добавить комментарий:
git commit -m "комментарий к коммиту"

5. команда $ git push отправляет локальные изменения на сервер

6. функция $ git log позволяет просмотреть список коммитов
