from picamera import PiCamera
from time import sleep
#list for effects
#sketch
#posterise
#gpen
#colorbalance
#film
#pastel
#emboss
#denoise
#negative
#blur
#colorswap
#colorpoint
#saturation
#hatch
#watercolor
#cartoon
#none
#deinterlace1
#deinterlace2
#washedout
#solarize
#oilpaint
i =0
camera = PiCamera()
def takepict():
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
def takevideo():
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
def diffEffects(effect):
    camera.start_preview()
    camera.image_effect = effect #"film"#camera.IMAGE_EFFECTS[effect]
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % effect)
    camera.stop_preview()

