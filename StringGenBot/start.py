from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention}🍷,

ι αм {me2},​тяυѕтє∂ ѕтяιηg ѕєѕѕιση gєηєяαтσя вσт. ƒυℓℓу ѕє¢υяє & ησ αηу єяяσя.
.

𝐌𝐚𝐝𝐞 𝐁𝐲  : [​🇲​​🇦​​🇲​​🇧​​🇦​_​🇭​​🇺​_​🇻​​🇦​​🇮​ ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ ꜱᴜᴘᴘᴏʀᴛ ❣️", url="https://t.me/MAMBA_UPDATES_CHAT"),
                    InlineKeyboardButton("🥀 ᴏꜰꜰɪᴄᴇ 🥀", url="https://t.me/MAMBA_UPDATES")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
