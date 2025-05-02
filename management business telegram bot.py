#bot.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🛒 ثبت سفارش", callback_data='order')],
        [InlineKeyboardButton("💳 پرداخت", callback_data='payment')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('به بات خوش آمدید:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'order':
        query.edit_message_text(text="لطفا محصول مورد نظر را وارد کنید:")
    elif query.data == 'payment':
        query.edit_message_text(text="مبلغ را به شماره کارت ۶۰۳۷-****-****-۱۲۳۴ واریز کنید.")

updater = Updater("YOUR_BOT_TOKEN")
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()