from cleverwrap import CleverWrap
import constants as keys

cw = CleverWrap(keys.CLEVER_API)

def text(text):
    reply = cw.say(text)
    return reply
