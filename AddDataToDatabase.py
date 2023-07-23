import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://realtime-facebasedattendance-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "963852":
        {
            "name": "Elon Musk",
            "major": "Software",
            "starting_year": 2020,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Machine Learning",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "D",
            "year": 4,
            "last_attendance_time": "2022-12-14 00:4:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
