import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8443))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # https://your-render-domain.onrender.com

IMAGE_URL = "https://i.ibb.co/G3nbpR0L/IMG-20250820-221800-029.webp"

CAPTION = """..."""  # aapka caption yahan

def get_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1. sᴜᴘᴘᴏʀᴛ🍂 👇", url="https://t.me/hehe_heeeeee")],
        [InlineKeyboardButton("2. ʙᴏᴛs🍁 👇", url="https://t.me/Music_promaxbot?start=_tgr_u2T_FTcxODI1")],
        [InlineKeyboardButton("3. ᴍᴏʀᴇ☘️ 👇", url="https://t.me/hartsteeler")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=IMAGE_URL,
        caption=CAPTION,
        parse_mode="HTML",
        has_spoiler=True,
        reply_markup=get_inline_keyboard()
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
        drop_pending_updates=True
    )

if __name__ == "__main__":
    main()
