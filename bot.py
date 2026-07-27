from telegram import Update
from telegram.ext import Application,MessageHandler,filters,ContextTypes
import json,os
TOKEN="8601433292:AAGmJJaH7tWEoMoqL2v0n7kq5WdErxyuQt0"
DATA_FILE="data.json"
last=[]
def load():
 global last
 if os.path.exists(DATA_FILE):
  try:last=json.load(open(DATA_FILE)).get("last",[])
  except:last=[]
def save():
 json.dump({"last":last},open(DATA_FILE,"w"))
load()
def check():
 if len(last)<3:return False
 if 1.00 in last[-3:]:return False
 if len(last)>=10:
  return sum(1 for x in last[-10:] if x<1.50)<=1
 return True
async def handle(update:Update,context:ContextTypes.DEFAULT_TYPE):
 global last
 try:n=float(update.message.text)
 except:return
 last.append(n);last=last[-10:];save()
 await update.message.reply_text("🟢 ادخل" if check() else "🔴 لا تدخل")
app=Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle))
app.run_polling()
