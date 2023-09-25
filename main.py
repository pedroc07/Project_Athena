import os
import discord
import random
import time
from keep_alive import keep_alive
from discord.ext import commands
import threads
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
  print("A machine made to assist human being.")

@client.event
async def om_message(message):
  if message.content.startswith('<@883730637096378459>'):
    await message.channel.send('Oi, ' + message.author.mention)

@client.command(
  help="Cumprimenta Aigis",
  brief="!oi"
)
async def oi(ctx):
  await ctx.channel.send('Oi, ' + ctx.author.mention)

@client.command(help="Escolhe entre duas opções dadas",
  brief="!escolha <escolha1> <escolha2>")
async def escolha(ctx, x, y):
  escolhido = random.choice([x, y])
  await ctx.channel.send(escolhido)

@client.command(help="Diz algo",
  brief="!diga")
async def diga(ctx, x, y='', z='', a='', b='', c='', d='', e='', f=''):
  await ctx.channel.send(x + " "+ y + " "+ z + " "+ a + " "+ b + " "+ c+ " "+ d+" "+ e + " " + f)

@client.command(hidden=True)
async def palhacos(ctx):
  await ctx.channel.send(
        "ATAQUE DOS PALHACO LOKO:clown::clown::clown:\nAGORA EH NOIS QUE MANDA NESSA POHA:clown::clown:\nSAIAM DO SERVER:clown::clown:\nCOMECOU O ATAQUE:clown::clown:\nHÁ! HÁ! HÁ! HÁ! HÁ! HÁ!\nVOCES FORAM HACKEADOS PELOS PALHACO LOKO:clown::clown:\nOS COMEDORES DE ADMINISTRADO:clown::eggplant::clown:\nTa-_Em-_Shok kk?!:zap::zap:"
    )

@client.command(help="Te lembra de algo em uma data acertada",
  brief="!lembrete <hora> <minuto> <mensagem>")
async def lembrete(ctx, hor, min, msg=''):
  tempo = time.time()
  sair = False
  await ctx.channel.send(f"Lembrete marcado para {hor}:{min}")
  while sair == False:
    tempo_format = time.localtime()
    if int(hor) <= tempo_format.tm_hour and int(min) <= tempo_format.tm_min:
        await ctx.channel.send(ctx.author.mention, msg)
        sair = True
    else:
      tempo = time.time()

@client.command(help="Cita um verso de poesia",
  brief="!quote")
async def quote(ctx):
  escolha = random.randint(0, 5)
  if escolha == 0:
    await ctx.channel.send(
          "Vês! Ninguém assistiu ao formidável\nEnterro de sua última quimera.\nSomente a Ingratidão – esta pantera –\nFoi tua companheira inseparável!\nAcostuma-te à lama que te espera!\nO homem, que, nesta terra miserável,\nMora, entre feras, sente inevitável\nNecessidade de também ser fera.\nToma um fósforo. Acende teu cigarro!\nO beijo, amigo, é a véspera do escarro,\nA mão que afaga é a mesma que apedreja.\nSe alguém causa inda pena a tua chaga,\nApedreja essa mão vil que te afaga,\nEscarra nessa boca que te beija!\n- Augusto dos Anjos"
      )
  elif escolha == 1:
    await ctx.channel.send(
          "Volta o cão arrependido\nCom suas orelhas tão fartas\nCom seu osso roído\nE com o rabo entre as patas"
      )
  elif escolha == 2:
    await ctx.channel.send(
          "Escutem bem, bandidos. Vocês podem jogar comida ou cerveja em mim, ou mesmo cuspir. Eu até vou rir disso. Mas, não me interessa as razões que tenham, não vou perdoar ninguém que se meta com meus amigos!\n- Shanks, o ruivo."
      )
  elif escolha == 3:
      await ctx.channel.send(
          "Quando, por uma lei das supremas potências,\nO Poeta se apresenta à plateia entediada,\nSua mãe estarrecida e prenhe de insolências\nPragueja contra Deus, que dela então se apieda.\n- Charles Baudelaire"
      )
  elif escolha == 4:
      await ctx.channel.send(
    "\nCedo à sofreguidão do estômago. É a hora\nDe comer. Coisa hedionda! Corro. E agora,\nAntegozando a ensangüentada presa,\nRodeado pelas moscas repugnantes,\nPara comer meus próprios semelhantes\nEis-me sentado à mesa!\nComo porções de carne morta... Ai! Como\nOs que, como eu, têm carne, com este assomo\nQue a espécie humana em comer carne tem!...\nComo! E pois que a Razão me não reprime,\nPossa a terra vingar-se do meu crime\nComendo-me também.\n- Augusto dos Anjos")
  elif escolha == 5:
      await ctx.channel.send(
    'Madrugada de Treze de Janeiro.\nRezo, sonhando, o ofício da agonia.\nMeu Pai nessa hora junto a mim morria\nSem um gemido, assim como um cordeiro!\nE eu nem lhe ouvi o alento derradeiro!\nQuando acordei, cuidei que ele dormia,\nE disse à minha Mãe que me dizia:\n"Acorda-o!" deixa-o, Mãe, dormir primeiro!\nE saí para ver a Natureza!\nEm tudo o mesmo abismo de beleza,\nNem uma névoa no estrelado véu...\nMas pareceu-me, entre as estrelas flóreas,\nComo Elias, num carro azul de glórias\nVer a alma de meu Pai subindo ao Céu!\n- Augusto dos Anjos')

@client.command(help="Te envia o link para adicionar Aigis ao seu servidor",
  brief="!invite")
async def invite(ctx):
  await ctx.channel.send("https://discord.com/api/oauth2/authorize?client_id=883730637096378459&permissions=412787145920&scope=bot")

@client.command(aliases=["j"],help="Joga uma partida de jokenpô com Aigis", brief="!jokenpo <opcao>")
async def jokenpo(ctx, msg):
    rec_existe = False
    dict = {"pedra": ":rock:", "papel": ":newspaper:", "tesoura": ":scissors:"}
    list = ["pedra", "papel", "tesoura"]
    escolha = random.choice(list)
    if escolha == msg:
      await ctx.channel.send(
          f"{dict[msg]}:vs:{dict[escolha]}Escolhi {escolha} também, deu empate :/")
    elif (escolha == "pedra" and msg == "tesoura") or (escolha == "tesoura" and msg == "papel") or (escolha == "papel" and msg == "pedra"):
      await ctx.channel.send(f"{dict[msg]}:vs:{dict[escolha]}Escolhi {escolha}, então venci :)")
    elif (escolha == "tesoura" and msg == "pedra") or (escolha == "papel" and msg == "tesoura") or (escolha == "pedra" and msg == "papel"):
      await ctx.channel.send(f"{dict[msg]}:vs:{dict[escolha]}Escolhi {escolha}, acho que perdi :(")
      recordes = []
      if os.path.exists('recordes.json'):
        with open('recordes.json', 'r') as arq:
          recorde_arq = json.load(arq)
        recordes = recorde_arq
      for i in recordes:
        print(i)
        if i["id"] == str(ctx.author.id):
          i["recorde"] = str(int(i["recorde"]) + 1)
          rec_existe = True
      if not rec_existe:
        novo_recorde = {'id':str(ctx.author.id), 'recorde':1}
        recordes.append(novo_recorde)
        recordes = json.dumps(recordes)
      with open('recordes.json', 'w') as arq:
          json.dump(recordes, arq)

@client.command(aliases=["r"],help="Veja quantas vezes você venceu Aigis no Jokenpô", brief="!recorde")
async def recorde(ctx):
  venceu = False
  with open('recordes.json', 'r') as arq:
    recorde_arq = json.load(arq)
  recordes = recorde_arq
  for i in recordes:
    if i["id"] == str(ctx.author.id):
      await ctx.channel.send(
          f'Você venceu Aigis no Jokenpô {i["recorde"]} vezes.')
      venceu = True
  if not venceu:
    await ctx.channel.send(
          f'Você venceu Aigis no Jokenpô {i["recorde"]} vezes.')


token = os.environ['token']

keep_alive()

client.run(token)
