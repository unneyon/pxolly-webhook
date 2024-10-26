# @pxolly: вебхук
Это — вебхук на Python для [@pxolly: чат-менеджера](https://vk.com/pxolly). Для хотя бы минимального понимания, как он работает, нужно сначала прочитать статью [«Callback API»](https://vk.com/@pxolly-webhook) от [@pxolly](https://vk.com/@pxolly).<br>
Вы также всегда можете установить [готовый вебхук](https://vk.com/roxy2022) ([статья по установке](https://vk.com/@roxy2022-go)).

# Оглавление
1. [Настройка](https://github.com/unneyon/pxolly-webhook#настройка)
2. [Получение токена от VK](https://github.com/unneyon/pxolly-webhook#получение-токена-от-vk)
3. [Получение токена от API @pxolly: чат-менеджера](https://github.com/unneyon/pxolly-webhook#получение-токена-от-api-pxolly-чат-менеджера)
4. [Запуск](https://github.com/unneyon/pxolly-webhook#запуск)

## Настройка
### config.json
**Описание значений:**
| Значение | Описание | Тип |
|:---------:|:---------:|:---------:|
| `port` | Порт, на котором будет запущен вебхук (по умолчанию 6789) | integer |
| `credential` → `vk_token` | Токен от аккаунта VK. Получение: [*тык*](https://github.com/unneyon/pxolly-webhook#получение-токена-от-vk) | string |
| `credential` → `pxolly_token` | Токен от API [@pxolly: чат-менеджера](https://vk.com/pxolly). Получение: [*тык*](https://github.com/unneyon/pxolly-webhook#получение-токена-от-api-pxolly-чат-менеджера) | string |
| `web-check` → `title` | Название веб-страницы (лучше оставить дефолтное значение) | string |
| `web-check` → `text` | Основной текст (это может быть что угодно, что кратко расскажет о том, где находится пользователь) | string |
| `web-check` → `little_text` | Нижний текст (текст с небольшим описанием) | string |

**Структура файла:**
```json
{
    "port": 6789,
    "credential": {
        "vk_token": "",
        "pxolly_token": ""
    },
    "web-check": {
        "title": "@pxolly: вебхук",
        "text": "@pxolly: вебхук",
        "little_text": "Вебхук для <a href=\"https://vk.com/pxolly\">@pxolly [VK]</a> работает!"
    }
}
```

## Получение токена от VK
Токен от VK можно получить по этой ссылке: [vkhost.github.io](https://vkhost.github.io)
> *Позже тут будет подробная инструкция с получением токена…*

## Получение токена от API [@pxolly: чат-менеджера](https://vk.com/pxolly)
Вам необходимо написать в ЛС [@pxolly: чат-менеджера](https://vk.com/pxolly) команду `!токен новый` (бот вам даст ссылку на его мини-приложение, где вы должны будете получить токен).
> *Позже тут будет подробная инструкция с получением токена…*

## Запуск
> **Предполагает, что у вас уже есть свой сервер, на котором вы можете настроить порты**

До первого запуска:
```commandline
git clone https://github.com/unneyon/pxolly-webhook pxwb
cd pxwb
pip3 install -r requirements.txt --force-reinstall
```
После этого вебхук можно запускать этой командой:
```commandline
python3 -B main.py
```