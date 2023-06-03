import requests
import json
from typing import Final
from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CallbackContext
from googlesearch import search



# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


print('Arrancando bot...')

TOKEN: Final = '6030876042:AAH7wZXgwU-GlC6Dm0gj16paJcNrXKcYDlA'
BOT_USERNAME: Final = '@Juegosferabot'

bot = Bot(token=TOKEN)

# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bievenido, Soy un Bot Llamado Juegosfera a la Orden! ! !,\n'
                                    ' Haz clic en un boton \n'
                                    '\n  Puede ver nuestro catalogo completo de nuestro producto aqui, tendras un mega aventura con nuestro productos unicos -- > \n '
                                    ' \n /producto')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola te saluda Juegosfera, Como te podemos ayudar?,'
                                   'Por el momento solo reconozco los siguientes comandos : \n'
                                    
                                   ' \n /start ------------ Visualizar el menu de catalogos \n'
                                   '\n /need  -------------Necesitas aun otro tipo de producto? \n'
                                    '\n /Sopport  -------------Necesitas Soporte? \n'
                                    '\n /open_website  -------------Necesitas mas informacion puedes visitarnos en nuestra pagina? \n')




# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Este es un comando realizado a comodadida de usuario, puede agregar el texto que desee aquí.')


def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hola' in processed:
        return '¡Qué onda!'

    if 'como estas' in processed:
        return 'Estoy bien.'

    if 'producto' in processed:
        return 'vea nuestro catalogo brindado al inicio.'

    if 'soporte' in processed:
        return 'se le brindara la ayuda con el comando help.'

    if 'pagina' in processed:
        return 'te daremos nuestra pagina para que puedas visitarla.'

    if 'gracias' in processed:
        return 'De nada, vuelve pronto.'

    return 'No entiendo'



async def back_command(update, context):
    # Lógica para manejar el comando de regresar
    await update.message.reply_text('Has presionado el botón "Regresar".')

async def forward_command(update, context):
    # Lógica para manejar el comando de adelantar
    await update.message.reply_text('Has presionado el botón "Adelantar".')

async def close_command(update, context):
    # Lógica para manejar el comando de cerrar
    await update.message.reply_text('Has presionado el botón "Cerrar".')

    async def start_command(update, context):
        # Crea los botones
        back_button = InlineKeyboardButton("Regresar", callback_data='back')
        forward_button = InlineKeyboardButton("Adelantar", callback_data='forward')
        close_button = InlineKeyboardButton("Cerrar", callback_data='close')

        # Crea el teclado con los botones
        keyboard = [[back_button, forward_button], [close_button]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Envía el mensaje con el teclado
        await update.message.reply_text('Haz clic en un botón:', reply_markup=reply_markup)

async def button_callback(update, context):
    query = update.callback_query
    button_clicked = query.data

    if button_clicked == 'back':
        await back_command(update, context)
    elif button_clicked == 'forward':
        await forward_command(update, context)
    elif button_clicked == 'close':
        await close_command(update, context)

    # Para eliminar la notificación de "Esperando respuesta" en el botón presionado
    await query.answer()


async def support_command(update, context):
    # Crea un mensaje de soporte con información de contacto
    support_message = "Si necesitas ayuda o soporte, puedes contactarnos a través de:\n\n" \
                      "Email: support@example.com\n" \
                      "Teléfono: +123456789\n" \
                      "Sitio web: https://example.com/support"

    # Envía el mensaje de soporte al usuario
    await context.bot.send_message(chat_id=update.effective_chat.id, text=support_message)
async def open_website_command(update, context):
    # Create a button to open the website
    button = InlineKeyboardButton(text='Open Website; Esta alojado en localhost:3000', url='https://example.com')
    reply_markup = InlineKeyboardMarkup([[button]])

    # Send the message with the button
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Click the button to open the website:', reply_markup=reply_markup)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Función para el comando /producto
async def producto_command(update, context):
    products = [
        {"name": "1", "price": "$100", "image_url": "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-23/shared-assets/images/fifa-23-featured-image.png.adapt.crop191x100.1200w.png"},
        {"name": "2", "price": "$259", "image_url": "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/mobile/mario-kart-tour-mobile/hero"},
        {"name": "3", "price": "$60", "image_url": "https://xombitgames.com/files/2012/12/principal.jpg"},
        {"name": "4", "price": "$100", "image_url": "https://i.ytimg.com/vi/6AwkMVtpydw/maxresdefault.jpg"},
        {"name": "5", "price": "$259", "image_url": "https://i.pinimg.com/originals/d0/4c/7e/d04c7edf59999abb813dd7fd5e12126e.jpg"},
        {"name": "6", "price": "$60", "image_url": "https://www.antevenio.com/wp-content/uploads/2019/06/Videojuegos-con-m%C3%A1s-audiencia.-Fortnite.jpg"},
        {"name": "7", "price": "$100", "image_url": "https://www.hispatecno.net/wp-content/uploads/2020/11/super-smash-bros-ultimate-switch-hero-1024x576.jpg"},
        {"name": "8", "price": "$259", "image_url": "https://plethoranetwork.com/wp-content/uploads/2022/01/1603445369_648285_1603445409_noticia_normal.jpg"},
        {"name": "9", "price": "$60", "image_url": "https://phantom-marca.unidadeditorial.es/a73987284077328b7be4267ca6ae8170/resize/828/f/jpg/assets/multimedia/imagenes/2022/12/31/16724808774520.jpg"},
        {"name": "10", "price": "$259", "image_url": "https://media.revistagq.com/photos/5ca5e992f464882a46f47eb6/master/w_1280,h_868,c_limit/los_100_mejores_videojuegos_de_la_historia_5572.jpg"},
        {"name": "11", "price": "$60", "image_url": "https://cdn.animum3d.com/wp-content/uploads/2023/05/18110524/blog-videojuegos-cabecera-v2.png"},
        {"name": "12", "price": "$100", "image_url": "https://im.ziffdavisinternational.com/ign_es/screenshot/default/mario-and-luigi-super-mario-bros-32564041-1680-105_ht9x.jpg"},
        {"name": "13", "price": "$259", "image_url": "https://www.mallorcaconfidencial.com/asset/thumbnail,992,558,center,center/media/mallorcaconfidencial/images/2020/10/23/2020102315211751022.png"},
        {"name": "14", "price": "$60", "image_url": "https://i0.wp.com/lavidaesunvideojuego.com/wp-content/uploads/2021/10/SuperMarioBros3UnNuevoMundo00-LaVidaEsUnVideojuego.webp?fit=1200%2C675&ssl=1"},
        {"name": "15", "price": "$100", "image_url": "https://imgmedia.larepublica.pe/640x377/larepublica/original/2022/01/21/61eaf135f4cb332c1374e395.webp"},
        {"name": "16", "price": "$259", "image_url": "https://elcomercio.pe/resizer/JT24YSpC5KUepuJXSzZu-WYa900=/580x330/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/QC5ED63A6JGENDSPFRRPEFSP4E.webp"},
        {"name": "17", "price": "$60", "image_url": "https://www.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2021/03/jefe-maestro-cortana-2277919.jpg"},
        {"name": "18", "price": "$100", "image_url": "https://gmedia.playstation.com/is/image/SIEPDC/dualsense-thumbnail-ps5-01-en-17jul20?$native$"},
        {"name": "19", "price": "$259", "image_url": "https://http2.mlstatic.com/D_NQ_NP_858907-MLU69240020176_052023-O.webp"},
        {"name": "20", "price": "$60",  "image_url": "https://media.vandal.net/i/200x249/42942/red-dead-redemption-2-20185218474_1.jpg"},
        {"name": "21", "price": "$100", "image_url": "https://lh4.googleusercontent.com/dh3Pf3Ael5FyoG-RRuJIyhwToKr0XdZYsHDi8B3o3t-1EfE5crrw6RzGFsjbt-vL5CPIiDqkSb6W94OVRsdtga9kSzguwUsiK7-5h-_Q4kbNp_CFygybXO6nqC3oaV8tSes-Hws8"},
        {"name": "22", "price": "$259", "image_url": "https://elcomercio.pe/resizer/6z1plmpMdqE2yJO3-kyDsw1qVYE=/1920x768/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/A6T5P2P7OZBVFOH3A2AJV5G7BI.jpg"},
        {"name": "23", "price": "$60", "image_url": "https://www.zelda.com/breath-of-the-wild/assets/icons/BOTW-Share_icon.jpg"},
        {"name": "24", "price": "$100", "image_url": "https://i.blogs.es/9a60a2/golf1/450_1000.jpg"},
        {"name": "25", "price": "$259", " image_url": "https://www.tonica.la/__export/1649462615433/sites/debate/img/2022/04/08/sonic-popular-videojuego.jpg_1037907269.jpg"},
        {"name": " 26", "price": "$60",  "image_url": "https://tecolotito.elsiglodedurango.com.mx/i/2022/04/1058853.jpeg"},
        {"name": "27", "price": "$100", "image_url": "https://super-ficcion.com/wp-content/uploads/2023/04/Quien-es-Donkey-Kong-1-780x470.webp"},
        {"name": "28", "price": "$259", "image_url": "https://cloudfront-us-east-1.images.arcpublishing.com/infobae/I6Y36MWNRFD2ZCPBKKANURLCXA.jpg"},
        {"name": "29", "price": "$60",  "image_url": "https://img.asmedia.epimg.net/resizer/x-v8JloRGqopPXV0NCZZOSF9tg4=/360x203/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/EPBVE6SG7BJOFOQKE7VZX54HX4.jpg"},
        {"name": "30", "price": "$100", "image_url": "https://culturageek.com.ar/wp-content/uploads/2023/02/Dead-Space_Mejores-Remakes_www.culturageek.com_.ar_.jpg"},

    ]

    bot = Bot(token=context.bot.token)

    buttons = []
    for product in products:
        button = InlineKeyboardButton(text=product['name'], callback_data=product['name'])
        buttons.append([button])

    reply_markup = InlineKeyboardMarkup(buttons)

    await bot.send_message(chat_id=update.effective_chat.id, text='Catálogo de productos:', reply_markup=reply_markup)


async def button_callback(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    product_name = query.data

    products = [
        {"name": "1", "price": "$100", "image_url": "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-23/shared-assets/images/fifa-23-featured-image.png.adapt.crop191x100.1200w.png"},
        {"name": "2", "price": "$259", "image_url": "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/mobile/mario-kart-tour-mobile/hero"},
        {"name": "3", "price": "$60", "image_url": "https://xombitgames.com/files/2012/12/principal.jpg"},
        {"name": "4", "price": "$100", "image_url": "https://i.ytimg.com/vi/6AwkMVtpydw/maxresdefault.jpg"},
        {"name": "5", "price": "$259",  "image_url": "https://i.pinimg.com/originals/d0/4c/7e/d04c7edf59999abb813dd7fd5e12126e.jpg"},
        {"name": "6", "price": "$60", "image_url": "https://www.antevenio.com/wp-content/uploads/2019/06/Videojuegos-con-m%C3%A1s-audiencia.-Fortnite.jpg"},
        {"name": "7", "price": "$100", "image_url": "https://www.hispatecno.net/wp-content/uploads/2020/11/super-smash-bros-ultimate-switch-hero-1024x576.jpg"},
        {"name": "8", "price": "$259", "image_url": "https://plethoranetwork.com/wp-content/uploads/2022/01/1603445369_648285_1603445409_noticia_normal.jpg"},
        {"name": "9", "price": "$60", "image_url": "https://phantom-marca.unidadeditorial.es/a73987284077328b7be4267ca6ae8170/resize/828/f/jpg/assets/multimedia/imagenes/2022/12/31/16724808774520.jpg"},
        {"name": "10", "price": "$259", "image_url": "https://media.revistagq.com/photos/5ca5e992f464882a46f47eb6/master/w_1280,h_868,c_limit/los_100_mejores_videojuegos_de_la_historia_5572.jpg"},
        {"name": "11", "price": "$60", "image_url": "https://cdn.animum3d.com/wp-content/uploads/2023/05/18110524/blog-videojuegos-cabecera-v2.png"},
        {"name": "12", "price": "$100", "image_url": "https://im.ziffdavisinternational.com/ign_es/screenshot/default/mario-and-luigi-super-mario-bros-32564041-1680-105_ht9x.jpg"},
        {"name": "13", "price": "$259", "image_url": "https://www.mallorcaconfidencial.com/asset/thumbnail,992,558,center,center/media/mallorcaconfidencial/images/2020/10/23/2020102315211751022.png"},
        {"name": "14", "price": "$60", "image_url": "https://i0.wp.com/lavidaesunvideojuego.com/wp-content/uploads/2021/10/SuperMarioBros3UnNuevoMundo00-LaVidaEsUnVideojuego.webp?fit=1200%2C675&ssl=1"},
        {"name": "15", "price": "$100", "image_url": "https://imgmedia.larepublica.pe/640x377/larepublica/original/2022/01/21/61eaf135f4cb332c1374e395.webp"},
        {"name": "16", "price": "$259", "image_url": "https://elcomercio.pe/resizer/JT24YSpC5KUepuJXSzZu-WYa900=/580x330/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/QC5ED63A6JGENDSPFRRPEFSP4E.webp"},
        {"name": "17", "price": "$60", "image_url": "https://www.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2021/03/jefe-maestro-cortana-2277919.jpg"},
        {"name": "18", "price": "$100", "image_url": "https://gmedia.playstation.com/is/image/SIEPDC/dualsense-thumbnail-ps5-01-en-17jul20?$native$"},
        {"name": "19", "price": "$259", "image_url": "https://http2.mlstatic.com/D_NQ_NP_858907-MLU69240020176_052023-O.webp"},
        {"name": "20", "price": "$60", "image_url": "https://media.vandal.net/i/200x249/42942/red-dead-redemption-2-20185218474_1.jpg"},
        {"name": "21", "price": "$100", "image_url": "https://lh4.googleusercontent.com/dh3Pf3Ael5FyoG-RRuJIyhwToKr0XdZYsHDi8B3o3t-1EfE5crrw6RzGFsjbt-vL5CPIiDqkSb6W94OVRsdtga9kSzguwUsiK7-5h-_Q4kbNp_CFygybXO6nqC3oaV8tSes-Hws8"},
        {"name": "22", "price": "$259", "image_url": "https://elcomercio.pe/resizer/6z1plmpMdqE2yJO3-kyDsw1qVYE=/1920x768/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/A6T5P2P7OZBVFOH3A2AJV5G7BI.jpg"},
        {"name": "23", "price": "$60", "image_url": "https://www.zelda.com/breath-of-the-wild/assets/icons/BOTW-Share_icon.jpg"},
        {"name": "24", "price": "$100", "image_url": "https://i.blogs.es/9a60a2/golf1/450_1000.jpg"},
        {"name": "25", "price": "$259", " image_url": "https://www.tonica.la/__export/1649462615433/sites/debate/img/2022/04/08/sonic-popular-videojuego.jpg_1037907269.jpg"},
        {"name": " 26", "price": "$60", "image_url": "https://tecolotito.elsiglodedurango.com.mx/i/2022/04/1058853.jpeg"},
        {"name": "27", "price": "$100", "image_url": "https://super-ficcion.com/wp-content/uploads/2023/04/Quien-es-Donkey-Kong-1-780x470.webp"},
        {"name": "28", "price": "$259", "image_url": "https://cloudfront-us-east-1.images.arcpublishing.com/infobae/I6Y36MWNRFD2ZCPBKKANURLCXA.jpg"},
        {"name": "29", "price": "$60", "image_url": "https://img.asmedia.epimg.net/resizer/x-v8JloRGqopPXV0NCZZOSF9tg4=/360x203/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/EPBVE6SG7BJOFOQKE7VZX54HX4.jpg"},
        {"name": "30", "price": "$100", "image_url": "https://culturageek.com.ar/wp-content/uploads/2023/02/Dead-Space_Mejores-Remakes_www.culturageek.com_.ar_.jpg"},


    ]

    selected_product = next((product for product in products if product['name'] == product_name), None)

    if selected_product:
        message = f"Name: {selected_product['name']}\nPrice: {selected_product['price']}"
        await bot.send_message(chat_id=query.message.chat_id, text=message)
        await bot.send_photo(chat_id=query.message.chat_id, photo=selected_product['image_url'])
        # Add the URL search button
        url_button = InlineKeyboardButton(text='Search URL', url=selected_product['image_url'])
        reply_markup = InlineKeyboardMarkup([[url_button]])
        await bot.send_message(chat_id=query.message.chat_id, text='Search the image URL:', reply_markup=reply_markup)

        def get_google_image_search_url(image_url):
            # Realiza la búsqueda en Google y obtén la URL de la primera página de resultados
            query = f"image: {image_url}"
            urls = search(query, num_results=1)

            # Retorna la URL de búsqueda de imágenes de Google
            for url in urls:
                if 'google.com/search' in url:
                    return url

            return ""

        # Configuración del bot
        def main():
            updater = Updater(token=TOKEN, use_context=True)
            dispatcher = updater.dispatcher

            # Comandos
            dispatcher.add_handler(CommandHandler("producto", producto_command))
            dispatcher.add_handler(CallbackQueryHandler(button_callback))

            updater.start_polling()
            updater.idle()

# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('producto', producto_command))
    app.add_handler(CommandHandler('open_website', open_website_command))
    app.add_handler(CommandHandler('support', support_command))
    app.add_handler(CallbackQueryHandler(button_callback))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))



    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)

