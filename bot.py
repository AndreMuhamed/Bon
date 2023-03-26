import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

message_threshold = 20
message_counter = 0

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global message_counter

    # Перевірка, що повідомлення не від бота і не знаходиться в приватному повідомленні
    if not message.author.bot and isinstance(message.channel, disnake.TextChannel):
        message_counter += 1
        if message_counter == message_threshold:
            channel = message.channel
            await channel.send('Привіт, не забудьте підписатися на наші сервера!')
            message_counter = 0

    await bot.process_commands(message)

@bot.slash_command()
async def future(interaction: disnake.ApplicationCommandInteraction):
    await interaction.response.send_message('У Зуфарчика большие планы на будущее')

bot.run('MTA1MTE1MDMwMDUwMjgzMTI0NA.G0k5qT.owjCZ2Z2NLF3jqXi44mXSum9CqF_vKgY-V0uto')
