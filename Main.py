# Importing modules
import json, requests, sys
import vk_api
import DLib

# Importing modules parts
from pyowm.exceptions import api_response_error
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# Creating variables with API-Keys
vk_api_key = 'c57e1e664859dd4a2e564b4262bd841bce289cbd88b1743425cdcebebc1ee295d3660f7b71088eae54736'
owm_api_key = '77f486a0b806529eb556220947c3689e'

# Initializing vk_api: longpoll-bot
vk_session = vk_api.VkApi(token = vk_api_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

# Printing: Bot has been started!
print('Cистема: Бот запущен!\n==================================================')

# Infinite cycle
while True:

	# Checking for new events cycle
	for event in longpoll.listen():

		# Initializing vkBot in DLib
		VkDLib = DLib.vkBot(vk, event)

		# Verifing for new text messages
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

			# Printing: System: User(id...) write: Message
			print('Система: (id%s) написал: %s' % (event.user_id, event.text))

			# Verifing for hello command
			if event.text == '!hello' or event.text == '!привет' or event.text == 'Начать' or event.text == 'Приветствие ✌':

				# Sending message with hello
				VkDLib.send_msg('Привет, я "Обозреватель погоды" 😀!\n⚠ Если хочешь узнать как я работаю, напиши - "!help"\nСоздатель бота: Губин Даниил')
				# Printing: System: New command: !hello, result: Run: 'Hello'
				print('Система: Обнаружена команда: "!hello"\nРезультат: Выполнить функцию: "Приветствие"\n==================================================')

				# Exit from cycle
				break

			if event.text == '!help' or event.text == '!помощь' or event.text == 'Помощь 💊':

				# Sending message with help
				VkDLib.send_msg('Мои команды 🚑:\n 1. "!hello" или "!привет" - Приветствие ✌,\n 2. "!help" или "!помощь" - Помощь 💊\n 3. "!weathy" или "!погода" - Погода ☁\n 4. "!meme" или "!мем" - Мем 🤣')
				# Printing: System: New command: !help, result: Run: 'Help'
				print('Система: Обнаружена команда: "!help"\nРезультат: Выполнить функцию: "Список команд"\n==================================================')

				# Exit from cycle
				break

			if event.text == '!weathy' or event.text == '!погода' or event.text == 'Погода ☁':

				# Sending message with choosing city
				VkDLib.send_msg('Снова привет 🖐, для какого города хочешь посмотреть погоду?\n⚠ Пример: Москва, Moscow')
				# Printing: System: New command: !weathy, result: Run: 'Choosing city'
				print('Система: Обнаружена команда: "!weathy"\nРезультат: Выполнить функцию: "Выбор города"\n==================================================')
				
				# Checking for new events cycle
				for event in longpoll.listen():

					# Initializing vkBot in DLib
					VkDLib = DLib.vkBot(vk, event)

					# Verifing for new text messages
					if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

						# Trying for:
						try:

							# Initializing getWeather in DLib
							OwmDLib = DLib.getWeather(owm_api_key, 'ru', event.text)

							# Printing: System: User(id...) choose city - "city": Cyty has been detected! Result: Run: 'Information about weather'
							print('Система: Пользователь (id%s) выбрал город - "%s": Город обнаружен!\nРезультат: Выполнить функцию: "Информация о погоде"\n==================================================' % (event.user_id, event.text))

							# Sending message with detail weather
							VkDLib.send_msg('☁ В городе - %s (Сейчас  %s)' % (OwmDLib.place, OwmDLib.w_get_detail()))
							# Printing: System (Information about weather): Sending information about detail weather in the city
							print('Система (Информация о погоде): Отправка информации о обстановке на улице')

							# Sending message with temperature
							VkDLib.send_msg('🌡 Температура в районе: %s °C' % str(OwmDLib.w_get_temp()))
							# Printing: System (Information about weather): Sending information about temperature in the city
							print('Система (Информация о погоде): Отправка информации о температуре на улице')

							# Printing: System (Information about weather): Couting and choosing a tip
							print('Система (Информация о погоде): Обсчет и выбор совета')
							# Counting temperature, choosing and sending a tip
							VkDLib.send_msg(OwmDLib.count_tip())

						# Search exeption: api_response_error.NotFoundError (Not found city)
						except api_response_error.NotFoundError:

							# Sending message with error
							VkDLib.send_msg('Сорян, я сломался 😢,\nПовтори попытку позднее.')
							# Printing: System (Information about weather): Error! Result: Sending error
							print('Система (Информация о погоде): Ошибка!\nРезультат: Вывод ошибки\n==================================================')

							# Exit from cycle
							break

				# Exit from cycle
				break

			if event.text == '!meme' or event.text == '!мем' or event.text == 'Мем 🤣':

				# Sending message with meme
				VkDLib.send_msg('Вот твой мем, наслаждайся ✨:\n(https://gfycat.com/assets/23968fa52b57e25c0a8e35bebc324202.gif)')
				# Printing: System: New command: !meme, result: Run: 'Meme'
				print('Система: Обнаружена команда: "!meme"\nРезультат: Выполнить функцию: "Вывод мема"\n==================================================')

				# Exit from cycle
				break

			else:

				# System: The unknowm command! Result: Run: 'Skipping'
				print('Система: Обнаружена неизвестная команда!\nРезультат: Выполнить функцию: "Пропуск"\n==================================================')

				# Exit from cycle
				break