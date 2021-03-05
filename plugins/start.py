from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("قناة البوت", url="https://t.me/zwamlallaith")],
        [InlineKeyboardButton(
            "مطور البوت😊", url="https://t.me/haidarkrar")]
    ])
    welcomed = f"مرحبا  <b>{message.from_user.first_name}</b>\n اضغط/help للمساعدة"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
