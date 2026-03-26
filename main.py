import telebot

# Initialize the bot with your token
API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Greeting handler
@bot.message_handler(commands=['start', 'help'])
def greet_user(message):    
    bot.reply_to(message, "Hello! I am your intelligent chatbot. How can I assist you today?")

# Capital cities lookup
cities = {
    'USA': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'UK': 'London',
    'Germany': 'Berlin',
    'France': 'Paris'
}

@bot.message_handler(commands=['capital'])
def send_capital(message):
    country = message.text.split('/capital ')[1].strip()  # Get the country name
    capital = cities.get(country, "I'm sorry, I don't have information about that country.")
    bot.reply_to(message, f'The capital of {country} is {capital}.')

# Presidential information
presidents = {
    'USA': 'Joe Biden',
    'Canada': 'Justin Trudeau',
    'France': 'Emmanuel Macron'
}

@bot.message_handler(commands=['president'])
def send_president(message):
    country = message.text.split('/president ')[1].strip()  # Get the country name
    president = presidents.get(country, "I'm sorry, I don't have information about that country.")
    bot.reply_to(message, f'The president of {country} is {president}.')

# FAQ system
faq_data = {
    'What is your name?': 'I am an intelligent chatbot created to assist you.',
    'How can you help me?': 'I can provide information on various topics, including capitals, presidents, and answer FAQs.'
}

@bot.message_handler(commands=['faq'])
def send_faq(message):
    faq_response = '\n'.join([f'Q: {q}\nA: {a}' for q, a in faq_data.items()])
    bot.reply_to(message, faq_response)

# Start the bot
if __name__ == '__main__':
    bot.polling()