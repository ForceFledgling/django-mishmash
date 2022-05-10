# 1. Цель проекта

Цель проекта — разработать систему для автоматизации разных рутинных задач (далее Система).
Пользователь сможет создавать в Системе разные типы скриптов, управлять ими,
а также выкладывать контент в локальную википедию.


# 2. Описание системы

Система состоит из следующих основных функциональных блоков:

1. Регистрация, аутентификация и авторизация (интеграция с LDAP)
2. Функционал википедии
5. Функционал интеграции с Telegram
6. Уведомления о новых постах и изменениях системы


## 2.1. Типы пользователей

Система предусматривает два типа пользователей системы: автор и подписчик.
Модератор создаёт скрипты и и публикует их, пользователи в соответствии
со своим уровнем получают доступ к разрешённому для них контенту.


## 2.2. Регистрация 

Система, как минимум в своей первой версии, не предполагается как SaaS для
разных Держателей. Одна конкретная инсталляция Системы привязана к одному
конкретному автору/проекту. При этом за счёт открытого исходного кода
Систему может скачать и развернуть любой желающий.

Таким образом, ведение разных авторов в рамках одной инсталляции
Системы пока не подразумевается.


## 2.3. Аутентификация

Аутентификация автора и подписчиков осуществляется по логину и паролю.


## 2.4. Функционал википедии

Модератор после аутентификации и присвоении группы получает доступ к 
своему автороскому функционалу в Системе. Этот функционал состоит из
следующих блоков:

1. ...


### 2.4.1. Редактирование профиля

В этом разделе у пользователей есть возможность редактирования данных
своего профиля — email, соц сети.
Возможные соц сети:

* YouTube
* Instagram
* Facebook
* VK
* Linkedin
* Twitch

Должна быть возможность сменить пароль, подтвердив свой старый пароль.

Если дизайн Системы будет подразумевать какие-то изображения для кастомизации
страницы Системы, то эти изображения тоже должны редактироваться из профиля
пользователя.


### 2.4.2. Заведение и редактирование контента википедии

Контент, публикуемый автором, может представлять собой форматированный текст
с возможность, как миниум, выделения текста жирным, курсивом, подчеркнутым,
перечеркнутым. Возможно стоит добавить возможность создания заголовков разного
размера для структурирования длинного текстового контента.

Должна быть возможность добавления списков и изображений в контент поста,
а также возможность прикрепления файлов.

У каждого поста должен быть заголовок.

Должна быть возможность создать тизер поста — обложку и текст описания
о том, что находится в этому посте.

Также для каждого поста должен быть задан уровень пользователя, при которой
этот пост можно читать. Помимо закрытых уровней, должен быть виден
уровень «открыт для всех» — такие открытые для всех посты будут видны
всем пользователям Системы.

В сам контент может вставляться: текст с форматированием (заголовки,
жирный, курсивный, перечеркнутый текст), изображения (загружаются с компьютера),
видео с YouTube (показываются в стандартном встроенном YouTube плеере),
аудио (загружаются с компьютера, проигрываются во строенном в Систему
аудио плеере, поддерживается только MP3 формат). Также должна быть возможность
прикрепить произвольный загруженный с компьютера файл — для пользователей
он будет отображаться как ссылка на загрузку этого файла.


### 2.4.5. Рассылки

Модератор может осуществлять Telegram рассылки из Системы. Задаётся текст сообщения,
редактор аналогичен тому, что используется при создании постов, выбирается,
кому отправить письмо.

### 2.4.6. Аналитика просмотра статей

...


## 2.5. Функционал интеграции с Telegram

Система должна управлять пользователями в одном конкретном чате. После того, 
как у пользователя сменился логин или заблокировали УЗ, у него должен пропасть доступ и к чату.


# 3. Требования к дизайну

Минимализм, лаконичность, акцент на контент. Белый фон. Должен присутствовать
логотип Системы где-то на странице. Логотип надо разработать в рамках
этого проекта.

В нижней части страницы (в подвале) должно быть написано:

«Работает на Open Source» со ссылкой на GitHub проекта.