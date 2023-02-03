# перевод слов на маленькие буквы
import discord
import sys
import os 
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '*')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("__SDG__"))
    print('Bot online')
    
    
@client.event
async def on_message(message):
    if message.channel.id != 543896208175923200:
        return
    if message.author == client.user:
        return
    async for message in message.channel.history(limit=1):
         print()
    op = str("**[" + message.author.display_name + "**]  -  " + message.content)
    op1 = op.lower()
    m = op1.replace('q','爍');m1 = m.replace(  'w','夾');m2 = m1.replace( 'e','複');m3 = m2.replace( 'r','惟');m4 = m3.replace( 't','丄');m5 = m4.replace( 'y','曼');m6 = m5.replace( 'u','解');m7 = m6.replace( 'i','痣');m8 = m7.replace( 'o','呇');m9 = m8.replace( 'p','卂');q1 = m9.replace( 'a','喜');q2 = q1.replace( 's','寙');q3 = q2.replace( 'd','銣');q4 = q3.replace( 'f','怏');q5 = q4.replace( 'g','了');q6 = q5.replace( 'h','炽');q7 = q6.replace( 'j','圊');q8 = q7.replace( 'k','布');q9 = q8.replace( 'l','累');w1 = q9.replace( 'z','塉');w2 = w1.replace( 'x','飽');w3 = w2.replace( 'c','墾');w4 = w3.replace( 'v','地');w5 = w4.replace( 'b','區');w6 = w5.replace( 'n','刈');w7 = w6.replace( 'm','𤲟');w8 = w7.replace( ' ','燾');w9 = w8.replace( '[','㶭');e1 = w9.replace( ']','㥣');e2 = e1.replace( '.','小');e3 = e2.replace( ',','者');e4 = e3.replace( '*','品');e5 = e4.replace( '²','舦');e6 = e5.replace( '`','較');e7 = e6.replace( '-','承');e8 = e7.replace( '"','袍');e9 = e8.replace( "'",'適');r1 = e9.replace( ':','輕');r2 = r1.replace( ';','銳');r3 = r2.replace( '?','留');r4 = r3.replace( '!','三');r5 = r4.replace( '^','希')
    basa2 = r5
    s1 = basa2.replace( '0','了');s2 = s1.replace( '1','及');s3 = s2.replace( '2','多');s4 = s3.replace( '3','愛');s5 = s4.replace( '4','魘');s6 = s5.replace( '5','筈');s7 = s6.replace( '6','森');s8 = s7.replace( '7','簥');s9 = s8.replace( '8','麪');d1 = s9.replace( '9','爀')
    t1 = d1.replace('й','宅');d2 = d1.replace('ц','鉝');d3 = d2.replace('у','貭');d4 = d3.replace('к','村');d5 = d4.replace('е','動');d6 = d5.replace('н','局');d7 = d6.replace('г','嬙');d8 = d7.replace('ш','𤲟');d9 = d8.replace('щ','懲');g1 = d9.replace('з','卲');g2 = g1.replace('х','胹');g3 = g2.replace('ф','卌');g4 = g3.replace('ы','荒');g5 = g4.replace('в','濃');g6 = g5.replace('%','勞');g7 = g6.replace('а','患');g8 = g7.replace('п','學');g9 = g8.replace('р','乪');h1 = g9.replace('о','炸');h2 = h1.replace('л','惸');h3 = h2.replace('д','恂');h4 = h3.replace('ж','毖');h5 = h4.replace('э','鑠');h6 = h5.replace('я','兇');h7 = h6.replace('ч','卝');h8 = h7.replace('с','臼');h9 = h8.replace('м','簿');k1 = h9.replace('и','妐');k2 = k1.replace('т','當');k3 = k2.replace('ь','起');k4 = k3.replace('б','鄔');k5 = k4.replace('ю','巔')
   # print(k5)
    f = open('message.txt','a+')
    f.write(k5+'\n')
#<______________________>

#pip install -U discord==1.7.3 pip install -U discord.py==1.7.3

client.run("",bot = False)
