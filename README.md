# Sistema Central de Consultas Jurídicas C2 - D.L. 1137 🎖️

## 1. Nombre del Proyecto
**Bot Integrado de Inteligencia y Consultas C2 (C2-IA Bot)**
*Módulo RAG (Retrieval-Augmented Generation) para el Ejército del Perú.*

---

## 2. Objetivo Táctico
El objetivo táctico de esta solución de comando y control (C2) con Inteligencia Artificial es **proporcionar a los operadores y personal militar respuestas jurídicas inmediatas, seguras y contextualizadas sobre el Decreto Legislativo N° 1137 (Ley del Ejército del Perú)**. 

Mediante el uso de un modelo de lenguaje avanzado (`gemini-flash-lite`) y un motor de recuperación de información (RAG) basado en documentos PDF oficiales (`DL1137.pdf`), el bot asiste en la toma de decisiones estratégicas, garantizando el apego irrestricto a la normativa legal militar sin riesgo de alucinaciones o manipulaciones maliciosas.

---

## 3. Instrucciones de Instalación

Siga estos pasos para desplegar el bot en su entorno local o en un servidor dedicado:

### Requisitos Previos
* **Python 3.10 o superior** instalado en el sistema.
* Un token de bot de Telegram (obtenido vía [@BotFather](https://t.me/BotFather)).
* Una clave de API de Google GenAI para interactuar con Gemini.

### Paso 1: Clonar o Descargar el Proyecto
Asegúrese de tener los siguientes archivos en su directorio de trabajo:
```text
bot_integrado_c2_ia/
├── config.py
├── config.py.example
├── database.py
├── generator.py
├── main.py
├── scheduler.py
├── requeriments.txt
└── DL1137.pdf
```

### Paso 2: Instalar las Dependencias
Ejecute el siguiente comando en la terminal para instalar las bibliotecas necesarias:
```bash
pip install -r requeriments.txt
```

### Paso 3: Configurar las Variables de Entorno / Credenciales
1. Renombre el archivo `config.py.example` a `config.py`.
2. Edite `config.py` y complete sus credenciales reales:
   ```python
   TOKEN_API = "TU_TELEGRAM_BOT_TOKEN_AQUI"
   CHAT_ID_MONITOREO = "ID_CHAT_MONITOREO_AQUI"
   GEMINI_API_KEY = "TU_GEMINI_API_KEY_AQUI"
   UMBRAL_SIMILITUD = 0.35
   ```

### Paso 4: Iniciar el Bot
Ejecute el módulo principal para poner el bot en marcha:
```bash
python main.py
```

---

## 4. Guía de Uso del Operador

El bot está diseñado para interactuar de forma intuitiva con el personal militar mediante comandos y lenguaje natural:

1. **Iniciar Interacción (`/start`):**
   Al enviar el comando `/start`, el sistema inicializa el motor cognitivo e informa que el bot está listo para recibir consultas.
   
2. **Consultas en Lenguaje Natural:**
   El operador escribe preguntas directas relacionadas con el Decreto Legislativo N° 1137.
   * *Ejemplo:* "¿Cuáles son las funciones del Alto Mando?" o "¿Cómo se estructura la organización del Ejército?".
   
3. **Flujo de Procesamiento Interno:**
   * **Búsqueda Semántica/Vectorial:** El sistema busca en el documento `DL1137.pdf` el artículo que mejor responde a la consulta.
   * **Validación de Umbral:** Si la similitud semántica es inferior al límite configurado (`UMBRAL_SIMILITUD = 0.35`), el bot emitirá una advertencia táctica informando que la consulta está fuera del marco de la ley analizada.
   * **Generación de Respuesta:** Si supera el umbral, el motor Gemini sintetiza la respuesta con un estricto tono castrense.

4. **Filtro de Seguridad (Guardrails):**
   Si el operador intenta forzar al bot a "olvidar" sus directivas o actuar en un rol no autorizado (ataques de prompt injection), el bot bloqueará el procesamiento y responderá con un error táctico estandarizado.

---

## 5. Funcionamiento Simultáneo (Multihilo)

Para garantizar un rendimiento óptimo bajo condiciones de alta demanda o en operaciones en tiempo real, el bot implementa un **diseño multihilo en Python**:

* **Módulo `scheduler.py`:** Define la inicialización de tareas programadas (como reportes automáticos o limpiezas periódicas) sin bloquear el flujo principal del bot.
* **Hilo de Escucha (Telegram Polling):** El bot de Telegram corre de forma independiente recibiendo y respondiendo consultas de múltiples usuarios.
* **Hilos de Segundo Plano:** Al llamar a `scheduler.iniciar_hilo_planificador()`, se levanta un hilo de tipo *Daemon* (`threading.Thread`) que ejecuta continuamente el bucle de verificación de `schedule.run_pending()` cada segundo. Esto evita que los temporizadores de monitoreo congelen la UI de chat o retrasen las respuestas a los operadores.

---

## 6. Políticas de Cero Exposición de Tokens (Seguridad de Credenciales)

En entornos militares y de alta seguridad, la protección de credenciales es crítica. Se establecen las siguientes directivas obligatorias para este proyecto:

1. **Prohibición de Hardcoding:** Bajo ninguna circunstancia se deben escribir tokens de Telegram (`TOKEN_API`) o claves de API de Gemini (`GEMINI_API_KEY`) directamente en los archivos de código fuente (`main.py`, `generator.py`, etc.).
2. **Uso del archivo `.gitignore`:** El archivo `config.py` (que contiene las credenciales reales) **debe estar listado en el archivo `.gitignore`** para evitar que sea subido accidentalmente a repositorios públicos o compartidos (como GitHub/GitLab).
3. **Distribución Segura:** Solo se distribuirá el archivo plantilla `config.py.example`. Los operadores encargados del despliegue deberán rellenar el archivo localmente en el servidor de destino con las claves autorizadas para ese nodo táctico.
4. **Rotación Periódica:** Los tokens deben renovarse periódicamente a través de los canales oficiales de administración de servicios de mensajería e inteligencia artificial.