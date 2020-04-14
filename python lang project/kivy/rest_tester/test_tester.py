# Perform http requests and print responses

# URL
# Dropdown menu: GET, Post, PATCH, DELETE
# Response Body:

from requests import Request, Session
from kivy.app import App
from kivy.uix.widget import Widget


class BaseWindow(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def perform_http_request(self, method):
        # TODO predefine the request, update the mothod accordingly
            
        request = Request(method, url=self.url.text)
        response = Session().send(request.prepare())

        #response.status_code
        self.response_body.text= response.text



    # def perform http_request
    # Get the URL from the textfield
    # perform request
    # put output in a result field


class WebtesterApp(App):
    
    def build(self):
        
        Base_Window = BaseWindow()
        return Base_Window

if __name__=='__main__':
    WebtesterApp().run()
