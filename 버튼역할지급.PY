import discord
from discord_components import DiscordComponents, Button, ButtonStyle, interaction

'''
망치#1111
간단하게 소스짜봄 
봇토큰,역할이름 수정
'''

client = discord.Client()

token = '봇토큰'

DiscordComponents(client)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!역할버튼":
        embed = discord.Embed(title='망치토큰커뮤니티', description='배너를 보기위해선 아래버튼을눌러주세요')
        await message.channel.send(embed=embed, components=[[Button(label="역할받기", id="verify", style=ButtonStyle.gray)]])

@client.event
async def on_button_click(interaction: interaction):
    if interaction.component.custom_id == "verify":
        verify_role = '역 할 이 름' #버튼을 누르면 줄 역할이름
        verifyrole = discord.utils.get(interaction.guild.roles, name=verify_role)
        if verifyrole in interaction.user.roles:
            await interaction.respond(content='이미 역할을 갖고계십니다')
            return
        await interaction.user.add_roles(verifyrole)
        await interaction.respond(content="역할이 지급되었습니다")



client.run(token)
