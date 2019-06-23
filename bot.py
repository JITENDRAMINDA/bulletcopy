from pyrogram import Client, Filters,Emoji
app = Client('my_aount',715451,"d2cba6f7bf5d1a45682da5bb9071a307")

u = '-1001378725482'

@app.on_message(Filters.command("clear"))
def forward(client, message):
  file = open("sure.txt" , "w")
  file.write("001 002")
  file.close()
 
         
   
@app.on_message(Filters.command("set"))
def forward(client, message):
  with open("source.txt" , "w") as file:
   file.write(message.text.split(' ')[1])
   file.close()

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
        if '🖲' in message.text:
            mes = client.send_message(int(u),"**" + message.text.replace('🖲' , '💘') + "**")
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
        elif '📟' in message.text :
            mes = client.send_message(int(u),"**" + message.text.replace('📟' , '🏝') + "**")
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
        elif message.text == 'WD' :
            client.send_message(int(u),'🤦‍♂️ **WIDE BALL** 🤦‍♂️')
        elif message.text.casefold() == 'WKT'.casefold() :
            client.send_message(int(u),'🚾** Wicket Wicket Wicket** 🚾 ') 
        elif 'NO BALL' in message.text:
            client.send_message(int(u),'🔛** NO BALL **🔛' )
        elif 'DRINKS BREAK' in message.text:
            client.send_message(int(u), '🍻** DRINKS BREAK **🍻') 
        elif 'DEAD BALL' in message.text:
            client.send_message(int(u), '🔁** DEAD BALL **🔄') 
        elif message.text.casefold() == 'RUKA'.casefold():
            client.send_message(int(u), '🛑** BOWLER RUKA **🛑')
        elif message.text.casefold() == '🚾WICKET WICKET🚾'.casefold():
            client.send_message(int(u),'🚾** Wicket Wicket Wicket **🚾')
        else:
            mes = client.send_message(int(u), "**" + message.text.replace('🎾' , '🥎') + "**")
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
         

@app.on_message(Filters.sticker)
def forawrd(client, message):
  if message.sticker.file_id == 'CAADBQADkgIAAlTquhpPMfzjWNqQagI' :
    client.send_message(int(u),'🍾 **INNINIGS BREAK** 🍾' )
    
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
     if '🖲' in message.text:
        client.edit_message_text(int(u),int(x[x.index(id)+1]), "**" + message.text.replace('🖲' , '💘') + "**" )
     elif '📟' in message.text :
        client.edit_message_text(int(u),int(x[x.index(id)+1]),"**" + message.text.replace('📟' , '🏝') + "**")
     else:
        client.edit_message_text(int(u),int(x[x.index(id)+1]),"**" + message.text.replace('🎾' , '🥎')+ "**")
 
   

        
app.run()
