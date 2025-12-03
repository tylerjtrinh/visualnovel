define base_char = Character(color="#FFFFFF", ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
define narrator = Character(kind=base_char)

transform side_left_base:
    xalign 0.12
    yalign 1.0
    anchor (0.5, 1.0)

#Main Characters
image alex normal = "sprites/alex/alex_normal.png"
image valerie normal = "sprites/valerie/val_normal.png"
image ryan normal = "sprites/ryan/ryan_default.png"
image valerie ghost = Transform(im.Scale("sprites/valerie/val_ghost.png", 900, 1000))

image side valerie normal = Transform(im.Scale("sprites/valerie/val_normal.png", 450, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), xoffset=-45, yoffset=-25)
image side valerie happy = Transform(im.Scale("sprites/valerie/val_happy.png", 390, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), xoffset=-45, yoffset=-25)
image side valerie mad   = Transform(im.Scale("sprites/valerie/val_angry.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), yoffset=-25)
image side valerie sad   = Transform(im.Scale("sprites/valerie/val_sad.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), yoffset=-25)
image side valerie maimeng   = Transform(im.Scale("sprites/valerie/val_maimeng.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), yoffset=-25)

image side alex normal = Transform(im.Scale("sprites/alex/alex_normal.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0))
image side alex sad = Transform(im.Scale("sprites/alex/alex_sad.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0))
image side alex awksmile = Transform(im.Scale("sprites/alex/alex_awksmile.png",   450, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0))
image side alex slightsmile = Transform(im.Scale("sprites/alex/alex_smileslight.png",   500, 480), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), xoffset=-45)
image side alex angry = Transform(im.Scale("sprites/alex/alex_angry.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0))
image side alex shocked = Transform(im.Scale("sprites/alex/alex_shocked.png",   400, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0))

image side ryan normal = Transform(im.Scale("sprites/ryan/ryan_default.png", 450, 500), xalign=0.12, yalign=1.0, anchor=(0.5, 1.0), xoffset=-45, yoffset=-25)

image truck = "sprites/truck.png"
define a = Character("Alex", color="#0000FF", image="alex")
define v = Character("Valerie", color="#E37BD0", image="valerie")
define r = Character("Ryan", color="#C89D7C", image = "ryan")
transform side_left:
    xalign 0.12   # horizontal position (0.0 = left, 1.0 = right)
    yalign 1.0    # put the anchor at the bottom of the screen
    anchor (0.5, 1.0)   # anchor point: (x, y) of the image; bottom center