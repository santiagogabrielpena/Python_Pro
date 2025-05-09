import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.members = True  # Necesario para acceder a los miembros del servidor

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} está en línea')


@bot.command()
async def henry(ctx, *, mensaje: str = ""):
    mensaje = mensaje.lower().strip()

    if mensaje == "saludar todos":
        # Obtener todos los miembros del canal
        members = ctx.channel.members
        sent = 0
        for member in members:
            if not member.bot:  # Ignorar bots
                try:
                    await member.send(
                        f"¡Hola {member.name}! Soy un bot que puede saludarte. "
                        "Escríbeme 'hola' o usa el comando `$henry hola` para probar. (No le digas pero, es un poco inutil y esta en progreso)"
                    )
                    sent += 1
                except:
                    print(f"No pude enviarle mensaje a {member.name}")

        await ctx.send(f"Saludé por privado a {member.name} ")
    
    elif mensaje == 'hola':
        await ctx.send('Hola, ¿cómo estás?')
    elif mensaje == 'buenas':
        await ctx.send('Buenas, ¿qué tal?')
    elif mensaje == "eres inutil":
        await ctx.send("COMO TE ATREVES SI SOY EL GRADIOSO HENRY, DISCULPATE O TE BOTARE DEL GRUPO (No le digan pero no puede hacer esto ni contestarte mas despues cuando te disculpes, realmente es inutil)")
    elif mensaje == "miembros":
        for member in ctx.guild.members:
            await ctx.send(member.name)
    else:
        await ctx.send('comando invalido')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower().strip()

    if content in ['hola', 'buenas']:
        try:
            await message.author.send(
                f"¡Hola {message.author.name}! Soy un bot que puede saludarte. "
                "Escríbeme 'hola' o usa `$saludar hola`."
            )
        except:
            print(f"No pude mandar mensaje privado a {message.author.name}")
    
    await bot.process_commands(message)

token = ""
bot.run(token)
