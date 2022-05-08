import sys
import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import O9937
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
LOGS = logging.getLogger(
"مستقبل العرب"
)
print(
userbot.__copyright__)
print(
"المرخصة بموجب شروط " + userbot.__license__)
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info(
"بدء تنزيل مستقبل العرب"
)
    O9937.loop.run_until_complete(
setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(
f"{str(e)}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await load_plugins("MusicTelethon")
    print(
f"<b> ⌔︙ اهلا بك لقد نصبت مستقبل العرب بنجاح 🥁 اذهب الى قناتنا لمعرفة المزيـد ⤵️. </b>\n CH : https://t.me/O9937 "
)
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return
O9937.loop.run_until_complete(startup_process())
def start_bot():
  try:
      List = ["O9937","uruur","tttuu","TelethonMusic"]
      for id in List :
          O9937.loop.run_until_complete(O9937(functions.channels.JoinChannelRequest(id)))
  except Exception as e:
    print(e)
    return False
Checker = start_bot()
if Checker == False:
    print(
"عذرا لديك حظر مؤقت حاول التنصيب غدا او بعد 24 ساعة"
)
    O9937.disconnect()
    sys.exit()
if len(sys.argv) not in (1, 3, 4):
    O9937.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        O9937.run_until_disconnected()
    except ConnectionError:
        pass
