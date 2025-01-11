from telethon.sync import TelegramClient
from telethon import events, types
from main_func import *


print('''
 ____   ___    ____    __    ____  ___  ____  ____
(_  _) / __)  (  _ \  /__\  (  _ \/ __)( ___)(  _ \\
  )(  ( (_-.   )___/ /(__)\  )   /\__ \ )__)  )   /
 (__)  \___/  (__)  (__)(__)(_)\_)(___/(____)(_)\_)
             ''')
phone_number = phone_number_right(input('Введите ваш номер телефона:'))
print('Для Начала работы с Парсером войдите в https://my.telegram.org/auth')
print('Переходим в API development tools и Заполняем поля App title и Short name, \n'
      'и нажимаем «Create application» напишите свои api_id и ')
api_id = int(input('Введите api_id: '))
api_hash = input('Введите api_hash: ')
password = input("если у вас есть пароль напишите его если нет поставьте '-' :")
phrase = input('Введите фразу по которой будут парсится каналы: ')
client = TelegramClient(session=f'{phone_number[1:]}.session', api_id=api_id, api_hash=api_hash,
                        system_version='4.16.30-vxCUSTOM', )
print('Сейчас придет код авторизации его нужно будет ввести ниже')
if password == "-":
    client.start(phone=phone_number)
else:
    client.start(phone=phone_number, password=password)

print(f'Начал парсить все каналы где будет попадаться фраза - "{phrase}"\n'
      f'Вся информация будет в файле parcing.txt')


@client.on(events.NewMessage(incoming=True))
async def channel_parcer(event):
    async for dialog in client.iter_dialogs():
        if isinstance(event.peer_id, types.PeerChannel):
            if phrase.upper() in str(event.message.message).upper():
                if event.message.message == dialog.message.message:
                    if dialog.entity.broadcast:
                        if dialog.entity.username is None:
                            link_to_message = f'https://t.me/c/{dialog.message.peer_id.channel_id}/{dialog.message.id}'
                        else:
                            link_to_message = f'https://t.me/{dialog.entity.username}/{dialog.message.id}'
                        def_phrace = f'{dialog.name};{dialog.message.date};' \
                                     f'{link_to_message};{dialog.message.message}'
                        print(def_phrace)
                        write_in_file(def_phrace)


client.run_until_disconnected()
