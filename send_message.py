from telethon import TelegramClient, errors
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest

# ⚠️ НЕ публикуйте свои API-ключи публично!
api_id = 24586867
api_hash = "c74a1a9426f345c05ef9ac223f4e15ed"

# Явно указываем абсолютный путь к файлу сессии (без расширения)
client = TelegramClient("/root/telegram_bot/my_session", api_id, api_hash)

async def check_session():
    if not await client.is_user_authorized():
        print("⚠️ Бот не авторизован! Попробуйте авторизоваться вручную.")
        await client.start()  # Попытка подключения к аккаунту
        if not await client.is_user_authorized():
            print("❌ Ошибка: не удалось авторизоваться.")
            return False
    return True

async def send_message():
    messages = [
        (-1002155201582, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1002120460328, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1002037221561, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001632685691, "📲Плачу 110₽ за написание отзыва на авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001554811744, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001305009781, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001618705872, "📲Плачу 110₽ за написание отзыва на Авито\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74 (гарант: @Legion_Guarantor_Bot)"),
        (-1001996032429, "📲Плачу 110₽ за написание отзыва на Авитов\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74 гарант @Freedom_Garant_Bot"),
        (-1001855792924, "📲Плачу 110₽ за написание отзыва на Авитов\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1002374585006, "📲Плачу 110₽ за написание отзыва на Авитов\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001894640231, "📲Плачу 110₽ за написание отзыва на Авитов\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74"),
        (-1001425395464, "📲Плачу 110₽ за написание отзыва на Авитов\n📝Заработок в день от 550₽ за 10-15 минут работы\n⚡️писать @zwsw_74 Гарант @atlantis_grntbot"),
    ]

    for channel_id, message_text in messages:
        try:
            entity = await client.get_entity(channel_id)
            await client.send_message(entity, message_text)
            print(f"✅ Сообщение отправлено в канал {channel_id}")
            await asyncio.sleep(15)  # Пауза между сообщениями
        except errors.FloodWaitError as e:
            print(f"⏳ Telegram требует подождать {e.seconds} секунд! Ждем...")
            await asyncio.sleep(e.seconds)
        except errors.ChatWriteForbiddenError:
            print(f"❌ Нет прав на отправку сообщений в {channel_id}.")
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
    # Добавляем задержку перед началом работы, чтобы дать время на инициализацию
    await asyncio.sleep(5)
    await client.start()
    if not await check_session():
        return
    while True:
        await send_message()
        print("⏳ Ждем 1,5 часа перед следующей рассылкой...")
        await asyncio.sleep(5400)  # 1,5 часа

with client:
    client.loop.run_until_complete(main())
