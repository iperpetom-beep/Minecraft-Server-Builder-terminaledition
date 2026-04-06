# Minecraft Server Manager

Консольный менеджер серверов Minecraft. Позволяет создавать, настраивать и запускать сервера в локальной файловой системе или Google Drive, с поддержкой двойного туннелирования playit.gg для сервера и VoiceChat.

## ✨ Возможности

- ✅ Поддержка 6 типов серверов: Vanilla, Paper, Purpur, Fabric, Forge, NeoForge
- ✅ Хранение на локальном диске или Google Drive (синхронизация через rclone)
- ✅ Двойное туннелирование playit.gg (сервер + VoiceChat с разными аккаунтами)
- ✅ Автоматический выбор Java версии (17 для <1.20, 21 для ≥1.20)
- ✅ Управление RAM и портами
- ✅ Автоматическая установка Java если нужно
- ✅ Отдельная логирование и конфигурация для каждого туннеля

## 📦 Установка зависимостей

Создайте виртуальное окружение и установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 📥 Скачивание playit

Загрузите playit с [playit.gg](https://playit.gg) и подготовьте две копии:

```bash
# Скачайте playit в корень проекта
cp ~/playit .

# Дублируйте для сервера и VoiceChat
cp playit playit-server
cp playit playit-voice

# Убедитесь что файлы исполняемые
chmod +x playit playit-server playit-voice
```

## 🔧 Настройка rclone (опционально, для Google Drive)

Если хотите использовать Google Drive для хранения серверов:

```bash
sudo apt update && sudo apt install rclone
rclone config
```

Создайте конфиг для remote `gdrive` (или используйте существующий).

## 🚀 Монтирование Google Drive

```bash
rclone mount gdrive: ~/gdrive
```

## ▶️ Запуск менеджера

Простой способ:

```bash
./start.py
```

Или вручную:

```bash
source venv/bin/activate
python -m mcmanager.mcmanager
```

## ⚙️ Настройка playit.gg

### Для сервера

1. Зарегистрируйтесь на [playit.gg](https://playit.gg)
2. Создайте агент и получите claim code
3. В менеджере: `3) Настройки` → `7) Настройки playit.gg для сервера`
4. Введите:
   - `Secret key` — claim code или secret
   - `Playit binary path` — `./playit-server` (или путь к нему)
5. Вернитесь в главное меню и включите: `4) Использовать playit.gg для сервера`

### Для VoiceChat

1. Получите отдельный claim code (можно использовать другой аккаунт)
2. В менеджере: `3) Настройки`
3. Включите: `5) VoiceChat включён`
4. Перейдите в: `8) Настройки playit.gg для VoiceChat`
5. Введите:
   - `Secret key` — отдельный claim code
   - `Playit binary path` — `./playit-voice`
6. Включите: `6) Использовать playit.gg для VoiceChat`

## 🎮 Создание сервера

1. Главное меню → `1) Создать сервер`
2. Выберите загрузчик (1-6)
3. Введите версию Minecraft
4. Укажите имя сервера
5. Выберите объём RAM
6. Выберите порт (по умолчанию 25565)
7. Выберите хранилище (локально или Google Drive)

## ▶️ Запуск сервера

1. Главное меню → `2) Выбрать сервер`
2. Выберите сервер из списка
3. Укажите RAM
4. Сервер запустится, playit туннели (если включены) запустятся автоматически
5. При остановке сервера (Ctrl+C) туннели также остановятся

## 📁 Структура проекта

```
mcmanager/
  mcmanager.py          # Основной менеджер и интерфейс
  __main__.py
  loaders/              # Загрузчики серверов
    vanilla.py
    paper.py
    purpur.py
    fabric.py
    forge.py
    neoforge.py
  utils/                # Утилиты
    config.py           # Конфигурация
    downloader.py       # Загрузчик файлов
    java.py            # Поиск Java
    gdrive.py          # Работа с Google Drive
playit                  # Бинарник playit (скачайте сами)
playit-server           # Копия для сервера (скопируйте из playit)
playit-voice            # Копия для VoiceChat (скопируйте из playit)
start.py               # Точка входа
README.md              # Этот файл
requirements.txt       # Зависимости Python
```

## 📝 Конфигурация

Все параметры сохраняются в `~/.mcmanager/config.json`:

```json
{
  "servers_path": "~/mcservers",
  "gdrive_mount": "~/gdrive",
  "gdrive_remote": "gdrive",
  "use_playit_server": false,
  "playit_server_secret": "",
  "playit_server_bin_path": "./playit-server",
  "playit_server_log_path": "~/.mcmanager/playit_server.log",
  "voicechat_enabled": false,
  "use_playit_voice": false,
  "playit_voice_secret": "",
  "playit_voice_bin_path": "./playit-voice",
  "playit_voice_log_path": "~/.mcmanager/playit_voice.log"
}
```

## 📋 Требования

- Python 3.7+
- requests
- psutil
- rclone (если используется Google Drive)
- Java 17/21

## 🐛 Известные ограничения

- Hard-coded пути к Java для Ubuntu/Debian (нужна поддержка других ОС)
- Поддерживается только playit.gg как туннель (в планах: ngrok, другие)
- Требуется rclone для работы с Google Drive

## 📄 Лицензия

MIT
