from Picture_taker.picturetaker import return_a_picture
from Facial_Recoqnition.picture_facial_reqoc import facial_reqocnition
from Facial_Recoqnition.video_facial_recoq import video_FR

class doorbell:

    def __init__(self):
        self.img = return_a_picture()

    def someone_at_the_door(self):
        '''in order to take a new picture when someone is at the door:'''
        self.img = return_a_picture()

    def picture_FR(self):
        img = self.img
        facial_reqocnition(img)

    def continuous_stream(self):
        video_FR()

if __name__=="__main__":

    DB = doorbell()

    DB.picture_FR()
    DB.someone_at_the_door()
    print('some shit')
    # DB.picture_FR()
    # DB.continuous_stream()