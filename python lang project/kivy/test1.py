import os, time
os.environ['KIVY_TEXT'] = 'pil'
import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        # to schedual a repeating event, do not use while true or time.sleep
        # if you do that kivy won't be able to do others thing so u will have a black screen
        # instead use Clock.schedule
        '''
        #********** Scheduling an event *************
        def my_callback(dt):
            print('My callback is called')
        event = kivy.clock.Clock.schedule_interval(my_callback, 1 / 30.)
        
        # to unschedule use, do this everytime to unschedule event
        event.cancel() or Clock.unschedule(event)

        # you call call a function once in the next frame or n seconds
        #If n is greater than 0, the callback will be called in X seconds
        #If n is 0, the callback will be called after the next frame
        #If n is -1, the callback will be called before the next frame
        def my_callback(dt):
            print 'My callback is called !'
        Clock.schedule_once(my_callback, n)

        #********** Trigger events *************
        # or a better way is to use trigger, wich unschedule it self
        trigger = Clock.create_trigger(my_callback)
        # later
        trigger()

        #********** Widget events *************
        # it has 2 types of events
        Property event: if your widget changes its position or size, an event is fired.
        Widget-defined event: e.g. an event will be fired for a Button when it’s pressed or released.


        

        '''


class MyApp(App):

    def build(self):
        return LoginScreen()



if __name__ == '__main__':
    MyApp().run()
