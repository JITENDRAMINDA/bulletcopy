from pyrogram import Client, Filters,Emoji
app = Client("mcc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
k = -1001453099412
@app.on_message(Filters.command("clearf"))
def forward(client, message):
  with open("ids.txt" , "w") as file:
   file.write("0001")
   file.close() 
   message.reply("kk")
@app.on_message(Filters.command("setf"))
def forward(client, message):
  with open("source.txt" , "w") as file:
   file.write(message.text.split(' ')[1])
   file.close()
   message.reply("done bro ₹₹₹₹ ")
@app.on_message( Filters.text & ~Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
    f = False
    words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
    for word in words:
     if word.casefold() in message.text.casefold():
      f = True
    if not f:
      mes = client.send_message(k,message.text)
      fie = open("ids.txt","a")
      fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
      fie.close()   
@app.on_message( Filters.text & Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   file = open("ids.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(k,int(x[x.index(id)+1]),message.text)
     except FloodWait as e:
      time.sleep(e.x)
@app.on_deleted_messages(Filters.channel)
def main(client, messages):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   for v in messages:
    file = open("sure.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     x = line.split()
     id = str(v.message_id )
     if id in x:
      try:
       client.edit_message_text(k,int(x[x.index(id)+1]),".")
      except FloodWait as e:
       time.sleep(e.x)
app.run()
