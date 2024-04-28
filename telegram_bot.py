
from typing import Final
from telegram import Update
import weather
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'YourBotToken'
BOT_NAME: Final = 'YoutBotName'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello! I am a bot {BOT_NAME}, designed to help you find the weather all around the globe. Write /help to learn how to use me.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You can use the following commands:\n'
                                    '/weather <city> - to get the weather in a specific city\n'
                                    '/custom - to get a custom response\n')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You entered the command /custom')

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = ' '.join(context.args)
    response = weather.get_weather(city)
    print(f'Bot: "{response}"')
    await update.message.reply_text(response)

def process_text(text: str) -> str:
    text = text.lower()
    if 'hello' in text:
        return 'Hello! How can I help you?'
    if 'bye' in text:
        return 'Goodbye!'
    if 'thank you' in text:
        return 'You are welcome!'
    if 'how are you' in text:
        return 'I am fine, thank you!'
    if 'what is your name' in text:
        return 'I am a bot, no name, only weather!'
    if 'weather' in text:
        return 'Please use the command /weather <city> to get the weather in a specific city'
    return 'I do not understand you'

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(f'User ({update.message.chat_id}) in {update.message.chat.type}: "{text}"')

    if update.message.chat.type == 'group' and BOT_NAME in text:
        text = text.replace(BOT_NAME, '').strip()

    response = process_text(text)
    print(f'Bot: "{response}"')
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Error: {context.error}')
    await update.message.reply_text('An error occurred')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('weather', weather_command))

    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    # Add error handler
    app.add_error_handler(error_handler)

    app.run_polling()
