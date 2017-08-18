from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login()

phoneNumber = cell
text = messagetext

voice.send_sms(phoneNumber, text)