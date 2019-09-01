from pyrogram import Client, Filters,Emoji
app = Client("mnnn",768402,"f6420bf67303614279049d48d3e670f6")
d = -1001378725482
@app.on_message( Filters.text & ~Filters.edited)
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
 f = False
 words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND',"?","LU"]
 for word in words:
  if word.casefold() in text.casefold():
   f = True
 if not f:
  mes = client.send_message(d, "<b>" + message.text + "</b>", parse_mode="html")
  files = open("sure.txt" , "a")
  files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
  files.close()  
  
@app.on_message( Filters.text & Filters.edited)
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(message.message_id)
  if id in x:
    try:
     client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + message.text + "</b>",parse_mode = "html")
    except FloodWait as e:
     time.sleep(e.x)     
app.run()
