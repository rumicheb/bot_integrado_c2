# main.py
import telebot
import schedule
# Importamos nuestros propios módulos locales
import config
import database
import scheduler

bot = telebot.TeleBot(config.TOKEN_API)

# 1. Configuración de Tareas Proactivas (Scheduler)
def alerta_automatica_combustible():
    df = database.simular_inventario()
    # Filtramos artículos críticos
    criticos = df[df['Cantidad'] < df['Umbral_Minimo']]
    
    if not criticos.empty:
        for _, fila in criticos.iterrows():
            mensaje = (
                f"🚨 *[ALERTA LOGÍSTICA PROACTIVA]*\n"
                f"⚠️ El artículo *{fila['Articulo']}* está en nivel crítico.\n"
                f"📦 Stock actual: {fila['Cantidad']} (Mínimo requerido: {fila['Umbral_Minimo']})"
            )
            bot.send_message(config.CHAT_ID_MONITOREO, mensaje, parse_mode="Markdown")

# Programamos la revisión cada 30 segundos
schedule.every(30).seconds.do(alerta_automatica_combustible)

# 2. Manejadores de Comandos Reactivos
@bot.message_handler(commands=['start', 'estado'])
def comando_estado(message):
    df = database.simular_inventario()
    reporte = "📋 *ESTADO ACTUAL DE RECURSOS (PVF CONCORDIA)*\n\n"
    for _, fila in df.iterrows():
        estado = "🟢 OK" if fila['Cantidad'] >= fila['Umbral_Minimo'] else "🚨 CRÍTICO"
        reporte += f"• *{fila['Articulo']}:* {fila['Cantidad']} units [{estado}]\n"
        
    bot.reply_to(message, reporte, parse_mode="Markdown")

# 3. Encendido del Sistema
if __name__ == "__main__":
    print("🛰️ Iniciando sistema de comunicaciones 'HÉROE'...")
    scheduler.iniciar_hilo_planificador()
    print("🟢 Bot a la escucha de comandos (infinity_polling)...")
    bot.infinity_polling()


