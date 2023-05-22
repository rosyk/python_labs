from jokeapi import Jokes
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, InlineQueryHandler
from translate import Translator


async def get_joke():
    jokes = await Jokes()
    joke = await jokes.get_joke(joke_type="twopart")
    return joke["delivery"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Address me from any chat room with an @ and I'll complete your joke")


async def query_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    translator = Translator(to_lang="ru")
    query = update.inline_query.query
    if not query:
        return
    answer = InlineQueryResultArticle(
        id='1',
        title="Шутка",
        description="Добавить шутку",
        input_message_content=InputTextMessageContent(query + ". " + translator.translate(await get_joke()))
    )
    await update.inline_query.answer([answer])


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(InlineQueryHandler(query_text))

    application.run_polling()
