import cleverbot
import constants as keys

def text(text):
    cb = cleverbot.Cleverbot(keys.CLEVER_API, cs='76nxdxIJ02AAA', timeout=60, tweak1=0, tweak2=100, tweak3=100)
    try:
        reply = cb.say(text)
    except cleverbot.CleverbotError as error:
        return error
    else:
        return reply
    finally:
        cb.close()