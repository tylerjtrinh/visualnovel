image bg living_room = "bg/living-room.png"
image bg starry_sky = "bg/sky.png"
image bg grass = "bg/grass.png"
image bg white = "#FFFFFF"
image bg wife_grass = "bg/cutscene_extrarender.png"
image bg garden dead = "bg/garden-dead.PNG"
image bg grass_cutscene = "bg/grass-cutscene.png"
image bg truckkun = "sprites/truck.png"
image staircase = "bg/staircase.PNG"

image loadingscreen = Solid("#38125c")
#transitions
define in_eye = ImageDissolve("transitions/eye.png", 2.0)
define out_eye = ImageDissolve("transitions/eye.png", 6.0, reverse=True)

define in_shatter = ImageDissolve("transitions/shatter.png", 1.0)

define in_confused = ImageDissolve("transitions/039.jpg", 3.0)

define in_spiral = ImageDissolve("transitions/spiral2.png", 0.5)
define out_spiral = ImageDissolve("transitions/spiral2.png", 0.5, reverse=True)

define in_spiral2 = ImageDissolve("transitions/039.jpg", 0.5)

define in_glitch = ImageDissolve("transitions/glitch.jpg", 0.25)