from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler, filters
import rmbgapi


help_text = '''
hi I am a bot i can help you with following

Remove Backgrounds - To remove background of any image just upload the image and i will remove it's background and send it back to you
'''

hi_text = '''
Hi i am a bot!

if you want to know more about me,use this command:  /help
'''

# Basic Commands

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text = "I'm a bot you can talk to me!")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text = "Sorry I can't understand this Command!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text = help_text)



# Greeting The User

async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE):
	msg_text = update.message.text.lower()
	lis = ["hi","hii","hello","hi bro","hello bro"]
	if msg_text in lis:
		await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker="hibramhi.png")
		await context.bot.send_message(chat_id=update.effective_chat.id, text=hi_text)

	else:
		await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)



# Remove Background Of Image

async def remove_background(update: Update, context: ContextTypes.DEFAULT_TYPE):
	file_id = update.message.photo[-1].file_id
	new_file = await context.bot.get_file(file_id)

	print("getting image.....")
	await new_file.download_to_drive('input.png')
	print("got the image")

	rmbgapi.rembg("input.png","output.png")
	await context.bot.send_message(chat_id=update.effective_chat.id,text = "removing background...")
	await context.bot.send_document(chat_id=update.effective_chat.id, document="output.png")
	await context.bot.send_message(chat_id=update.effective_chat.id, text = "here is the final image ☝️☝️☝️")

	print("sent the image")


# Main Code

if __name__ == "__main__":
	application = ApplicationBuilder().token("TELEGRAM_BOT_TOKEN").read_timeout(30).write_timeout(30).build()
	print("starting bot.....")

	application.add_handler(CommandHandler("start",start))
	application.add_handler(CommandHandler("help", help))
	application.add_handler(MessageHandler(filters.PHOTO,remove_background))
	application.add_handler(MessageHandler(filters.COMMAND, unknown))
	application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), greet))

	print("polling...")
	application.run_polling(poll_interval=3)
