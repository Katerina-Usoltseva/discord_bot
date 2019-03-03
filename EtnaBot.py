from discord.ext import commands
from Server.Server import Server

bot = commands.Bot(command_prefix='$')
token = ''


@bot.event
async def on_ready():
    print('Bot is ready to connect')


@bot.event
async def on_message(message):
    if message.content.startswith("$select"):
        status, response = server.do_query_db(message.content)
        await bot.send_message(message.channel, response)


if __name__ == '__main__':
    server = Server()
    if server.connect_db():
        bot.run(token)