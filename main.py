import discord
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import requests

gamesInProgress = {}

print('setting up NLP')
model_name = "deepset/roberta-base-squad2"
print('starting pipeline')
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question':'',
    'context':''
}
print('loading model')
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
print('loading tokenizer')
tokenizer = AutoTokenizer.from_pretrained(model_name)
print('DONE! Moving to bot setup...')
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
@client.event
async def on_message(msg):
    if msg.author == client.user: return
    if msg.content.startswith('20q'):
        args = msg.content.split() # make argument list, should only respond to "start" or "quit"
        # TODO: if game is in progress for author id, respond to any message containing a question mark
        # TODO: basically everything
        args.pop(0) # remove invocation statement probably
        if args[0] == 'start':
            # TODO: steal my own wikipedia query code from wikibot
            gamesInProgress[msg.author.id] = next(iter(requests.get('https://en.wikipedia.org/w/api.php', {
                'action':'query',
                'generator':'random',
                'rnnamespace':'0',
                'prop':'extracts',
                'format':'json',
                'explaintext':1
            }).json()['query']['pages'].values()))
            print(str(gamesInProgress))
            await msg.channel.send(str(gamesInProgress))


client.run(open('token.txt', 'r').read())