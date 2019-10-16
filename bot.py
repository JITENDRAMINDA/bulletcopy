from pyrogram import Client, Filters,Emoji
app = Client("session",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")
k = -1001378725482
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
    words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND',"?","LU"]
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
