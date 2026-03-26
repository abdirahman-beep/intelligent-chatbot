# Chatbot Configuration Settings

DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'db_name': 'chatbot_db'
}

NLP_MODEL_PATHS = {
    'default': 'path/to/default/model',
    'sentiment_analysis': 'path/to/sentiment/model',
    'intent_recognition': 'path/to/intent/model'
}

API_ENDPOINTS = {
    'chat': 'https://api.yourservice.com/chat',
    'user_data': 'https://api.yourservice.com/user/data'
}