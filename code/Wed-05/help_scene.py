# Created by: Hamza Salman
# Created on: September 2016
# Created for: ICS3U
# This scene is the help scene for the program.

from scene import *
import ui

from main_menu_scene import *


class HelpScene(Scene):
    def setup(self):
        
        center_of_screen = self.size/2
        
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
        self.start_button = LabelNode('Designed by: Hamza Salman',
                                      font = ('helvetica', 20),
                                      parent = self,
                                      position = self.size/2)
    
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_button_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    