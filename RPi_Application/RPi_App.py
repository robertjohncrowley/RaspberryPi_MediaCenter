import firebase_admin as fba
from firebase_admin import db
import json
import libtorrent as lt


def init_firebase(key_path, database_url):
    cred = fba.credentials.Certificate(key_path)
    fba.initialize_app(cred, {'databaseURL': database_url})


def reset_firebase():
    ref = db.reference("/")
    with open("default-firebase.json") as f:
        file_con = json.load(f)
    ref.set(file_con)


def read_from_firebase():
    ref = db.reference("/download-info/")
    print("NAME: " + ref.get()["name"])


def firebase_listener(event):
    if event.event_type == "put":
        read_from_firebase()


def main():
    init_firebase("../firebase-private-key.json", "https://media-center-a297f-default-rtdb.firebaseio.com/")
    ref = db.reference("/download-info")
    my_stream = ref.listen(firebase_listener)


if __name__ == "__main__":
    main()

