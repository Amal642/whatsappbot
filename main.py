import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller,Button
from time import sleep
from whatsapp_responses import response

mouse = Controller()

class whatsapp:
    def __init__(self,speed=0.5,click_speed=0.3):
        self.speed=speed
        self.click_speed=click_speed
        self.message=''
        self.lastmessage=''

    #navigate to the green dot or new message
    def nav_green_dot(self):
        try:
            position=pt.locateOnScreen('green_dot.png',confidence=0.8)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Error in green dot",e)

    #navigate to chat box
    def nav_input_box(self):
        try:
            position=pt.locateOnScreen('paperclip.png',confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(100,10,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Error in input box",e)
    #navigate to message
    def nav_message(self):
        try:
            position=pt.locateOnScreen('paperclip.png',confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(40,-50,duration=self.speed)
        except Exception as e:
            print("Error in input message",e)

    #copy the message
    def get_message(self):
        mouse.click(Button.left,3)
        sleep(self.speed)
        mouse.click(Button.right,1)
        sleep(self.speed)
        pt.moveRel(15,-100,duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.message=pc.paste
        print("user says:",self.message)

    def send_message(self):
        try:
            if self.message != self.lastmessage:
                bot_response=response(self.message)
                print("You said:",bot_response)
                pt.typewrite(bot_response,interval=0.1)
                pt.typewrite('\n') #sends the message

                self.lastmessage=self.message
            else:
                print("nothing new")

        except Exception as e:
            print("Error in message sending", e)

    def nav_cross(self):
        try:
            position=pt.locateOnScreen('cross.png',confidence=0.8)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(10,10,duration=self.speed)
            mouse.click(Button.left,1)
        except Exception as e:
            print("Error in green dot",e)




wabot=whatsapp(speed=0.5,click_speed=0.4)
sleep(2)

while True:
    wabot.nav_green_dot()
    wabot.nav_cross()
    wabot.nav_message()
    wabot.get_message()
    wabot.nav_input_box()
    wabot.send_message()

    sleep(10)
