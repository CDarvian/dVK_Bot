# Importing modules
import vk_api
import pyowm

# Initializing class: vkBot
class vkBot():

	# Initializing init_class function
	def __init__(self, vk, event):

		# Initializing variables
		self.vk = vk
		self.event = event

	# Initializing send_message function
	def send_msg(self, message):

		# Verifing from user
		if self.event.from_user:
			self.vk.messages.send(
				user_id = self.event.user_id,
				message = message,
				random_id = self.event.random_id,
				keyboard = open('keyboard.json',"r",encoding="UTF-8").read()
				)

		# Verifing from chat
		elif self.event.from_chat:
			self.vk.messages.send(
				chat_id = self.event.chat_id,
				message = message,
				random_id = self.event.random_id,
				keyboard = open('keyboard.json',"r",encoding="UTF-8").read()
				)

# Initializing class: getWeather
class getWeather():

	# Initializing init_class function
	def __init__(self, api_key, lang, place):

		self.api_key = api_key
		self.lang = lang
		self.place = place

		self.weather_api = pyowm.OWM(self.api_key, language = self.lang)
		self.obsi = self.weather_api.weather_at_place(self.place)
		self.weather = self.obsi.get_weather()
		
	# Initializing get_weather_details function
	def w_get_detail(self):

		# Initializing variable with weather_details
		w_detail = self.weather.get_detailed_status()

		# Returning variable
		return w_detail

	# Initializing get_temperature function
	def w_get_temp(self):

		# Initializing variable with temperature
		w_temp = self.weather.get_temperature('celsius')['temp']

		# Returning variable
		return w_temp

	# Initializing counting_tip function
	def count_tip(self):

		# Initializing variable with temperature
		temp = self.w_get_temp()

		# Counting temperature and returning result
		if temp < 10:
			print('Система (Информация о погоде): Температура меньше 10\nРезультат: Отправка совета N1\n==================================================')
			return '🦉 Совет:\n\nСейчас на улице очень холодно, одевайся как танк! ❄'

		elif temp < 20:
			print('Система (Информация о погоде): Температура меньше 20\nРезультат: Отправка совета N2\n==================================================')
			return '🦉 Совет:\n\nСейчас на улице холодно, оденься потеплее. 🧣'

		else:
			print('Система (Информация о погоде): Температура больше 20\nРезультат: Отправка совета N3\n==================================================')
			return '🦉 Совет:\n\nТемпература нормальная, одевай что угодно. 👓'