import telebot
import schedule

import config
import database
import generator
import scheduler

bot = telebot.TeleBot(config.TOKEN_API)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bienvenida = (
        "🎖️ *SISTEMA CENTRAL DE CONSULTAS JURÍDICAS C2 - D.L. 1137*\n"
        "Dirección de Telemática - Ejército del Perú\n\n"
        "El motor cognitivo y el módulo RAG están activos.\n"
        "Escriba su consulta jurídica en lenguaje natural (ej. _¿Cuáles son las funciones del Alto Mando?_)."
    )
    bot.send_message(message.chat.id, bienvenida, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def procesar_consulta_operador(message):
    consulta = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    articulo_recuperado,similitud = \
        database.buscar_articulo_vectorial(consulta)
    if similitud < config.UMBRAL_SIMILITUD:
        respuesta = (
            "⚠️ *ADVERTENCIA:* La consulta "
            "no tiene relación con el fragmento de ley "
            "provisto.\n"
            "El D.L. N° 1137 no detalla ese aspecto."
        )
    else:
        respuesta = \
            generator.generar_respuesta_militar(
                consulta, articulo_recuperado
            )
    bot.send_message(
        message.chat.id, respuesta, parse_mode="Markdown"
    )
    
if __name__ == "__main__":
    scheduler.iniciar_hilo_planificador()
    print("Bot iniciado. Esperando mensajes...")
    bot.polling()
