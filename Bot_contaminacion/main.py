import discord
from discord.ext import commands
import random

# Intenciones necesarias
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Crear el bot
bot = commands.Bot(command_prefix='$', intents=intents)

# Lista de contaminaciones y sus soluciones
contaminaciones = [
    {
        "tipo": " Contaminación del aire",
        "causa": "Producida por los carros, fábricas y quema de basura.",
        "solucion": "Usar bicicleta, caminar o compartir carro para reducir gases."
    },
    {
        "tipo": " Contaminación del agua",
        "causa": "Químicos y basura tirados en ríos o playas.",
        "solucion": "No tires basura en la calle y usa menos productos tóxicos."
    },
    {
        "tipo": " Contaminación del suelo",
        "causa": "Por tirar basura fuera de los zafacones o verter químicos.",
        "solucion": "Separar la basura, reciclar y no tirar aceite ni pintura en el piso."
    },
    {
        "tipo": " Contaminación sonora",
        "causa": "Ruido excesivo de bocinas, motores y construcciones.",
        "solucion": "Bajar el volumen, usar audífonos y respetar zonas tranquilas."
    },
    {
        "tipo": " Contaminación lumínica",
        "causa": "Demasiadas luces encendidas toda la noche.",
        "solucion": "Apagar luces que no se usan y usar bombillas eficientes."
    }
]

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} está en línea')

# Comando para mostrar una contaminación y su solución
@bot.command()
async def contaminacion(ctx):
    dato = random.choice(contaminaciones)
    mensaje = (
        f"**{dato['tipo']}**\n"
        f" *Causa:* {dato['causa']}\n"
        f" *Solución:* {dato['solucion']}"
    )
    await ctx.send(mensaje)

# Iniciar el bot (reemplaza por tu token real)
bot.run('')
