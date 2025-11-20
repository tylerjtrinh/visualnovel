
define in_d = ImageDissolve("transitions/dragon-skien.jpg", 2.0)
define out_d = ImageDissolve("transitions/dragon-skien.jpg", 2.0, reverse=True)

'''
label splashscreen:
    scene black
    with Pause(0.4)
    
    show bg living_room with in_d
    alt "Yadadada presents Pass On"
    with Pause(0.75)

    scene black
    with Pause(0.25)

    # End the label, which will return to the main menu
    return
'''
# The game starts here.
label start:
    call a0
    return

#Minigame screens
