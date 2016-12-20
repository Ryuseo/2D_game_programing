import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"
import game_framework
import start_state
from pico2d import *

open_canvas(960, 640)

game_framework.run(start_state)

close_canvas()