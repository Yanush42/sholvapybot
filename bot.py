import telebot
import pyowm

owm = pyowm.OWM('a92104f546e2839989b7855b333e6b4d', language = 'ru')
bot = telebot.TeleBot("988944065:AAGy0Lh4G5ShDdQxmrYMIHaFRs7Hz_hzZ7Q")

@bot.message_handler(content_types=['text'])
def send_weather(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('kelvin')["temp"]
	tempC = temp - 273.15

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура: " + str(tempC) + "°C" + "\n\n"

	if tempC < -5: 
		answer += "Жесть, вот это холодрыга! Одевай шубу и валенки!"
	elif tempC < 10:
		answer += "Сейчас довольно холодно, одевайся тепло!"
	elif tempC < 16: 
		answer += "Сейчас холодновато, накинь куртку."
	elif tempC < 20: 
		answer += "Прохладенько однако, лучше накинь кофточку."
	else:
		answer += "На улице тепло, можешь гулять в лёгкой, удобной одежде."

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop= True, interval = 0 ) 