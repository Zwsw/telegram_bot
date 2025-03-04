from telethon import TelegramClient, errors
import asyncio  
from telethon.tl.functions.channels import JoinChannelRequest  # 📌 Добавлено для подписки на каналы

# ⚠️ ВАЖНО: НЕ публикуйте свои API-ключи публично!
api_id = 24586867   
api_hash = "c74a1a9426f345c05ef9ac223f4e15ed"  

client = TelegramClient("/root/telegram_bot/my_session", api_id, api_hash)

# 📌 Функция для проверки сессии перед запуском
async def check_session():
    if not await client.is_user_authorized():
        print("⚠️ Бот не авторизован! Проверьте Telegram-сессию.")
        await client.start()  # Попытка подключения к аккаунту
        if not await client.is_user_authorized():
            print("❌ Ошибка: не удалось войти в аккаунт.")
            return False
    return True

async def send_message():
    await client.start()  # 📌 Подключаемся перед отправкой

    messages = [
        (-1002155201582, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1002120460328, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1002037221561, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001632685691, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001554811744, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001305009781, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001618705872, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74 (гарант: @Legion_Guarantor_Bot)"),
        (-1001996032429, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74 гарант @Freedom_Garant_Bot"),
        (-1001855792924, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1002374585006, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001894640231, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001425395464, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74 Гарант @atlantis_grntbot"),
    ]

    for channel_id, message_text in messages:
        try:
            entity = await client.get_entity(channel_id)  # Проверяем доступность канала
            await client.send_message(entity, message_text)
            print(f"✅ Сообщение отправлено в канал {channel_id}")

            # ⏳ Пауза между сообщениями (15 сек)
            await asyncio.sleep(15)

        except errors.FloodWaitError as e:
            print(f"⏳ Telegram требует подождать {e.seconds} секунд! Ждем...")
            await asyncio.sleep(e.seconds)

        except errors.ChatWriteForbiddenError:
            print(f"❌ Нет прав на отправку сообщений в {channel_id}. Возможно, бот не является администратором.")

        except errors.ChannelPrivateError:
            print(f"⚠️ Бот не подписан на канал {channel_id}. Подписываемся...")
            try:
                await client(JoinChannelRequest(channel_id))
                print(f"✅ Подписка на {channel_id} успешна.")
            except Exception as e:
                print(f"❌ Ошибка подписки на {channel_id}: {e}")

        except Exception as e:
            print(f"❌ Ошибка в {channel_id}: {e}")

async def main():
    await client.start()

    # 📌 Проверяем, есть ли активная сессия
    if not await check_session():
        return

    while True:
        await send_message()
        print("⏳ Ждем 1,5 часа перед следующей рассылкой...")
        await asyncio.sleep(5400)  # 1,5 часа (5400 секунд)

with client:
    client.loop.run_until_complete(main())
