import os
from flask import Flask, request
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Dispatcher

TOKEN = os.environ.get("BOT_TOKEN")  # Set your token in Render secret
PORT = int(os.environ.get("PORT", 8443))  # Render default port
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # Set your Render public URL here

IMAGE_URL = "https://i.ibb.co/G3nbpR0L/IMG-20250820-221800-029.webp"

CAPTION = """👉🍂🍃🌿  𝓐𝓫𝓸𝓾𝓽 𝓜𝓮  🌿🍃🍂
<pre>
╔══════════════╗
  ❖ TG Name :-   𝐒𝐮𝐝𝐞𝐞𝐩 🚩
  ❖ Username :-  @HeartStealer_X
╚══════════════╝
       ⧉ COPY CODE ⧉
</pre>
<pre>
╔══════════════╗
 ❖ Real Name :-  Nhi Btana 🤭
  ❖ Age :-  Nhi Btana
</pre>
<pre>
❖ Class :-  11 th 🙂
  ❖ From :-  Sabke Dil Mja
  ❖ Religion :-  Kattar 🚩
  ❖ Hobby :-  Anime – Gaming – 😂
╚══════════════╝
</pre>
<pre>
《════════════》
      ❤️ Complete ❤️
《════════════》
</pre>
<blockquote>
ᯓ𓆰⌯ <i>Thank You for being
a part of my journey ☗
➤ Your support means the world</i>
</blockquote>
"""

def get_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("1. sᴜᴘᴘᴏʀᴛ🍂 👇", url="https://t.me/hehe_heeeeee")],
        [InlineKeyboardButton("2. ʙᴏᴛs🍁 👇", url="https://t.me/Music_promaxbot?start=_tgr_u2T_FTcxODI1")],
        [InlineKeyboardButton("3. ᴍᴏʀᴇ☘️ 👇", url="t.me/hartsteeler")],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=IMAGE_URL,
        caption=CAPTION,
        parse_mode="HTML",
        has_spoiler=True,
        reply_markup=get_inline_keyboard()
    )

# Flask app
app = Flask(__name__)
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

@app.route("/")
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    # Set webhook on start
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=PORT)
