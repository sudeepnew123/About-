import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get environment variables
TOKEN = os.environ.get("BOT_TOKEN")  # Set your BotFather token in Render env
PORT = int(os.environ.get("PORT", 8443))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # Your Render URL, e.g., https://about-mh6l.onrender.com

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
    if not TOKEN or not WEBHOOK_URL:
        raise RuntimeError("Set BOT_TOKEN and WEBHOOK_URL env vars in Render!")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # PTB v20.6 webhook runner
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,  # secret webhook path
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
        drop_pending_updates=True
    )

if __name__ == "__main__":
    main()
