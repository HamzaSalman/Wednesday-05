# Created by: Hamza Salman
# Created on: September 2016
# Created for: ICS3U
# This program is used to use buttons to switch through scenes

from scene import *
import ui

from splash_scene import *
from help_scene import *


#  ..use when deploying app for Xcode and the App Store
main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = SplashScene()
main_view.present(hide_title_bar = True, animated = False)
