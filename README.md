# Minecraft Server Manager

Консольный менеджер серверов Minecraft. Позволяет создавать, настраивать и запускать сервера
в локальной файловой системе или Google Drive.

## Структура проекта

```
mcmanager/
  mcmanager.py
  loaders/
    __init__.py
    vanilla.py
    paper.py
    purpur.py
    fabric.py
    forge.py
    neoforge.py
  utils/
    __init__.py
    downloader.py
    java.py
    config.py
    gdrive.py
README.md
```

## Установка зависимостей

Создайте виртуальное окружение и установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Настройка rclone

Установите rclone:

```bash
sudo apt update && sudo apt install rclone
```

Настройте удалённый `gdrive`:

```bash
rclone config
```

Следуйте инструкциям для создания конфигурации Google Drive (обычно remote name: `gdrive`).

## Монтирование Google Drive

```bash
rclone mount gdrive: ~/gdrive
```

## Запуск менеджера

Простой способ:

```bash
./start.py
```

Или вручную:

```bash
source venv/bin/activate
python -m mcmanager.mcmanager
```

или

```bash
source venv/bin/activate
cd mcmanager && python mcmanager.py
```

## Настройка playit.gg для онлайн-доступа

1. **Зарегистрируйтесь на [playit.gg](https://playit.gg)** и создайте агент.
2. **Получите claim код** с сайта.
3. **Запустите claim**:
   ```bash
   ./playit claim <CLAIM_CODE>
   ```
   Замените `<CLAIM_CODE>` на код с сайта.
4. **Включите туннель в настройках менеджера**:
   - Выберите `3) Настройки` → `4) Использовать playit.gg туннель`.
5. **При запуске сервера** туннель автоматически запустится, и адрес будет доступен на playit.gg панели.

## Создание сервера

1. В главном меню выберите `Создать сервер`.
2. Выберите загрузчик и версию Minecraft.
   - Для **Forge** и **NeoForge**: введите версию Minecraft (например `1.20.1`), менеджер автоматически найдёт последнюю версию загрузчика.
   - Для других: введите версию Minecraft.
3. Укажите имя, RAM, порт (по умолчанию 25565) и место хранения (локально или Google Drive).
4. Сервер будет автоматически скачан и настроен.

## Добавление новых загрузчиков

1. Создайте новый модуль в `mcmanager/loaders/`.
2. Определите функцию `install(version: str, path: str)`.
3. Добавьте опцию в словарь `LOADERS` в `mcmanager/mcmanager.py`.
