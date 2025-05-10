import os
import logging
from dotenv import load_dotenv
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup,
    ReplyKeyboardMarkup, KeyboardButton,
    Update, InputMediaPhoto
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters,
    CallbackContext
)
from telegram.error import TelegramError

# Load environment variables
load_dotenv()

# Configuration - moved to separate class for better organization
class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
    
    CHANNELS = {
        "1": os.getenv("CHANNEL_1_URL", "https://t.me/+P0g3FjFHmC05MDY1"),
        "2": os.getenv("CHANNEL_2_URL", "https://t.me/+P0g3FjFHmC05MDY1"),
        "3": os.getenv("CHANNEL_3_URL", "https://t.me/+P0g3FjFHmC05MDY1"),
        "4": os.getenv("CHANNEL_4_URL", "https://t.me/+P0g3FjFHmC05MDY1")
    }
    
    IMAGES = [
        os.getenv("IMAGE_1_URL", "https://i.imgur.com/B0xU0Ie.jpg"),
        os.getenv("IMAGE_2_URL", "https://i.imgur.com/KQ7z4FZ.jpg"),
        os.getenv("IMAGE_3_URL", "https://i.imgur.com/rOijZMg.jpg"),

    ]
    
    PROMO_LINK = os.getenv("PROMO_LINK", "https://yonopromocodes.com/")
    JAIHO_LINK = os.getenv("JAIHO_LINK", "https://jaiho777agent2.com/?code=KZM38WKW22G&t=1744515002")
    CLAIM_LINK = os.getenv("CLAIM_LINK", "https://yonopromocodes.com/claim")

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class BotHandlers:
    @staticmethod
    async def send_gallery_and_promo(update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        try:
            # Send media group if multiple images
            if len(Config.IMAGES) > 1:
                media_group = [InputMediaPhoto(media=url) for url in Config.IMAGES[1:]]
                await context.bot.send_media_group(chat_id=chat_id, media=media_group)

            # Prepare message text
            text = (
                "🎰 Yono-777 >> BIGGEST VoucherCode Coming For All User's !! 😱😱\n"
                "👇👇👇👇👇👇👇👇👇👇👇\n\n"
                "👉 6 Free Spin Milegi (💰 ₹5 Bet )\n\n"
                f"✅ App Link >> {Config.PROMO_LINK}\n\n"
                "❤️ Jaldi-Jaldi Claim Karo !! 👇👇"
            )

            # Prepare inline keyboard
            inline_keyboard = [
                [
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["1"]),
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["2"])
                ],
                [
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["3"]),
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["4"])
                ],
                [InlineKeyboardButton("✅ Claim", callback_data="claim")]
            ]
            reply_markup = InlineKeyboardMarkup(inline_keyboard)

            # Send main message with first image
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=Config.IMAGES[3],
                caption=text,
                reply_markup=reply_markup,
                parse_mode="HTML"
            )

            # Send custom keyboard
            custom_keyboard = [
                [KeyboardButton("Yono 777"), KeyboardButton("BIG PromoCode")],
                [KeyboardButton("Jaiho Arcade"), KeyboardButton("Lucky Gullak")]
            ]
            reply_markup_custom = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            await context.bot.send_message(
                chat_id=chat_id,
                text="Select an option below:",
                reply_markup=reply_markup_custom
            )

        except TelegramError as e:
            logger.error(f"Error in send_gallery_and_promo: {e}")
            await context.bot.send_message(
                chat_id=chat_id,
                text="⚠️ An error occurred. Please try again later."
            )

    @staticmethod
    async def start(update: Update, context: CallbackContext):
        await BotHandlers.send_gallery_and_promo(update, context)

    @staticmethod
    async def button_callback(update: Update, context: CallbackContext):
        query = update.callback_query
        data = query.data
        chat_id = query.message.chat_id
        user = query.from_user

        try:
            if data == "claim":
                await query.answer()
                await context.bot.send_message(
                    chat_id=chat_id,
                    text="🎉 Claim Fast Very Limited !! 😍🤞🔥\n"
                         f"Click here to claim: {Config.CLAIM_LINK}\n"
                         "⏳ Offer valid until May 17, 2025, 11:59 PM!",
                    parse_mode="HTML"
                )
            else:
                await query.answer("Invalid action!", show_alert=True)
        except TelegramError as e:
            logger.error(f"Error in button_callback: {e}")
            await query.answer(f"⚠️ An error occurred: {str(e)}", show_alert=True)

    @staticmethod
    async def send_jaiho_promo(update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        try:
            inline_keyboard = [
                [
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["1"]),
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["2"])
                ],
                [
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["3"]),
                    InlineKeyboardButton("🎯 Join ✅", url=Config.CHANNELS["4"])
                ],
                [InlineKeyboardButton("✅ Claim", callback_data="claim")]
            ]
            reply_markup = InlineKeyboardMarkup(inline_keyboard)
            
            await context.bot.send_photo(
                chat_id=chat_id,
                photo="https://i.postimg.cc/brNyhmSx/Flux-Dev-Create-a-highresolution-modern-digital-wallet-backgro-3.jpg",
                caption=(
                    "🟢 Jaiho-777 New PromoCode 👇\n\n"
                    "Claim >> JAIHO777GAMES\n\n"
                    f"❤️ Jaiho-777 Link >> {Config.JAIHO_LINK}\n\n"
                    "💰 SignUp Bonus Upto ₹100 #Verified"
                ),
                parse_mode="HTML",
                reply_markup=reply_markup
            )
        except TelegramError as e:
            logger.error(f"Error in send_jaiho_promo: {e}")
            await context.bot.send_message(
                chat_id=chat_id,
                text="⚠️ An error occurred. Please try again later."
            )

    @staticmethod
    async def custom_keyboard_handler(update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        text = update.message.text
        
        try:
            if text in ["Yono 777", "BIG PromoCode", "Jaiho Arcade", "Lucky Gullak"]:
                await BotHandlers.send_jaiho_promo(update, context)
            else:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text="⚠️ Invalid option. Please select from the menu."
                )
        except TelegramError as e:
            logger.error(f"Error in custom_keyboard_handler: {e}")
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"⚠️ An error occurred: {str(e)}"
            )

    @staticmethod
    async def notify_admin(context: CallbackContext, chat_id: int, user: dict, channel: str):
        if Config.ADMIN_CHAT_ID:
            try:
                await context.bot.send_message(
                    chat_id=int(Config.ADMIN_CHAT_ID),
                    text=(
                        f"🚨 New join request!\n"
                        f"User: {user['first_name']} {user.get('last_name', '')}\n"
                        f"Username: @{user.get('username', 'N/A')}\n"
                        f"User ID: {user['id']}\n"
                        f"Chat ID: {chat_id}\n"
                        f"Channel: {channel}"
                    )
                )
            except TelegramError as e:
                logger.error(f"Error in notify_admin: {e}")

    @staticmethod
    async def handle_url_click(update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        user = update.effective_user.to_dict()
        
        # This is still an approximation - consider using a proper URL tracking service
        await BotHandlers.notify_admin(context, chat_id, user, Config.CHANNELS["1"])
        await context.bot.send_message(
            chat_id=chat_id,
            text="✅ Join request sent! An admin will review it soon."
        )

def main():
    if not Config.BOT_TOKEN:
        logger.error("Error: BOT_TOKEN not found in environment variables")
        exit(1)
        
    if not Config.ADMIN_CHAT_ID:
        logger.warning("ADMIN_CHAT_ID not found. Join request notifications will not be sent.")

    try:
        app = ApplicationBuilder().token(Config.BOT_TOKEN).build()
        
        # Add handlers
        app.add_handler(CommandHandler("start", BotHandlers.start))
        app.add_handler(CallbackQueryHandler(BotHandlers.button_callback))
        app.add_handler(MessageHandler(
            filters.Text(["Yono 777", "BIG PromoCode", "Jaiho Arcade", "Lucky Gullak"]),
            BotHandlers.custom_keyboard_handler
        ))
        app.add_handler(MessageHandler(filters.ALL, BotHandlers.handle_url_click))
        
        logger.info("Bot is starting...")
        app.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        exit(1)

if __name__ == "__main__":
    main()