from Picture_taker.picturetaker import return_a_picture
from Facial_Recoqnition.picture_facial_reqoc import facial_recognition, save_face_from_picure
from Facial_Recoqnition.video_facial_recoq import video_FR

class doorbell:

    def __init__(self):
        self.img = return_a_picture()

    def someone_at_the_door(self):
        '''in order to take a new picture when someone is at the door:'''
        self.img = return_a_picture()  # this saves a picture to Pictures/current picture.jpg
        current_face = save_face_from_picure(self.img)  # gets the current face of the person at the door, also saves it


    def picture_FR(self):
        img = self.img
        facial_recognition(img)

    def continuous_stream(self):
        video_FR()

if __name__=="__main__":

    DB = doorbell()

    # DB.picture_FR()
    DB.someone_at_the_door()
