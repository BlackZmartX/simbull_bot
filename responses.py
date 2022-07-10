from datetime import datetime
# import gizoogle
# import cleverbotty
import cleverwrapapi

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey", "yo", "whatsup", "sup"):
        return "Hi Seksi, How you doing!?"

    if user_message in ("who are you", "who are you?"):
        return "I'm Mr. Simbull, bitch."

    if user_message in ("time", "time?", "date", "date?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    # reply = None
    # if input_text is not None:
    #     reply = cleverbotty.text(input_text)
    # return reply


    reply = None
    if input_text is not None:
        reply = cleverwrapapi.text(input_text)
    return reply


    # return ('"' + str(input_text) + '"'+ " is not a valid command. What the fuck are you tryna say?")

    # reply = None
    # if input_text is not None:
    #     reply = gizoogle.text(input_text)
    # return reply
