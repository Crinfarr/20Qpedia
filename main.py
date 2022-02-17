import wikipediaapi as wapi
import discord
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question':'',
    'context':''
}
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

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