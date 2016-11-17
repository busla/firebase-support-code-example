import pyrebase
import time

config = {

}



firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(post):

    print(post["event"]) # put
    print(post["path"]) # /-K7yGTTEp7O549EzTYtI
    print(post["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    
    

my_stream = db.child("example").stream(stream_handler)

while True:

    data = {
      "title1" : "Táknmálsfréttir",
      "title2" : "Kastljós",
      "title3" : "Með vottorð í leikfimi",
      "title4": "Það er ekkert ætilegt úti"

    }

    db.child("example").push(data)

    time.sleep(3)