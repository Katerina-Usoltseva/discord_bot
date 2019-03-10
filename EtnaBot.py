from discord.ext import commands
from Server.Server import Server
import bot_settings as bot_settings

bot = commands.Bot(bot_settings.command_prefix)


@bot.event
async def on_ready():
    print('Bot is ready to connect.\nUse bot commands {}'.format(server.controller.bot_routs))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    query = message.content
    splited_query = query.rsplit(' ')
    command = splited_query[0]
    if server.controller.check_routs(command):
        response = server.execute_query(query, command)
        await bot.send_message(message.channel, response)


if __name__ == '__main__':
    server = Server()
    if server.connect_db():
        bot.run(bot_settings.token)