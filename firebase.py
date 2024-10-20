import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import storage
import datetime
from firebase import firebase
import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..."
firebase = firebase.FirebaseApplication('...')
cred = credentials.Certificate("...")
firebase_admin.initialize_app(cred)
db = firestore.client()
client = storage.Client()
bucket = client.get_bucket('...')
collection = db.collection('users')  #database

blobs = bucket.list_blobs()
num_blobs = sum(1 for _ in blobs)


def detection():
    return 'aa'


user='MB15C'
while True:
    if firebase.get("/disponibility",'nombre de place disponibles') == 5 :
        palette = 2
        pin=['1245','5698','4893','6213','2121','6591','1207','4962','4682','1021','7958','1197','3019','7784','9882','2210','3481','4030','9981','3784']
    if firebase.get("/disponibility",'nombre de place disponibles') == 4 :
        palette = 10
        pin=['1345','5678','4493','6413','2421','3591','1407','5962','4182','1001','7959','1197','3074','7084','9822','2010','3881','4010','9381','3384']

    blobs = bucket.list_blobs()

    if sum(1 for _ in blobs) > num_blobs :
        num_blobs=sum(1 for _ in bucket.list_blobs())
        blobs = bucket.list_blobs()
        sorted_blobs = sorted(blobs, key=lambda x: x.updated)
        image_a_traiter = sorted_blobs[-1]
        image_path = f'images/{image_a_traiter.name}'
        image_a_traiter.download_to_filename(image_path)


        whattime = datetime.datetime.now()
        res = collection.document(user).update({ # insert document
            'matricule'  : user,
            'Palette': str(palette),
            'code':pin,
            'datePassage': whattime,
        })
    blobs = bucket.list_blobs()