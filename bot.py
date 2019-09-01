from pyrogram import Client, Filters
app = Client("baaz",869912,"a7b049e08df35464047d57e5134327e5")
d = -1001378725482
@app.on_message( Filters.text & ~Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
    text = message.text
    f = False
    words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND',"?","LU"]
    for word in words:
        if word.casefold() in text.casefold():
            f = True
    if not f:
     mes = client.send_message(d, "<b>" + message.text + "</b>", parse_mode="html" )
     files = open("sure.txt" , "a")
     files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
     files.close()  
@app.on_message( Filters.text & Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + message.text.replace("🇩🇪","🇳🇮").replace("🎾","🥎").replace("🖲","🧤").replace("📟","🛑").replace("WD","🔷 WIDE BALL 🔷").replace("/","~").replace("CHALU RAKHO","GAME STARTED, PLAYERS ON THE STEDIUM ").replace("NB","🔷 NO BALL 🔷") + "</b>", parse_mode="html" )
     except FloodWait as e:
      time.sleep(e.x)
@app.on_message(Filters.command("clear"))
def forward(client, message):
 with open("sure.txt" , "w") as file:
  file.write("001 002")
  file.close()
@app.on_message(Filters.command("set"))
def forward(client, message):
  with open("source.txt" , "w") as file:
   file.write(message.text.split(' ')[1])
   file.close()
app.run()
