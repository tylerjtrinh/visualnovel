
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

style title_card_text: 
    font "menu.ttf" 
    
    # Set size and color
    size 60
    color "#F5F5F5" 
    bold True
    
    text_align 0.5 

# --- 2. SCREEN DEFINITION (Ensures Centering on Screen) ---

screen title_card_display(content_of_text):
    zorder 10 
    fixed:
        text content_of_text style_prefix "title_card":
            xalign 0.5
            yalign 0.5

# The game starts here.
label start:
    scene black
    
    pause 1.0
    show screen title_card_display("Visual Novel A Presents...") with dissolve
    pause 1.5
    hide screen title_card_display with dissolve
    show screen title_card_display("Pass On") with dissolve
    pause 1.5
    hide screen title_card_display with dissolve
    show screen title_card_display("Act 0") with dissolve
    pause 2.0
    hide screen title_card_display with dissolve
    # 5. Pause for 1 second after the text is hidden.
    pause 1.0

    call a0 from _call_a0

    scene black
    pause 2.0
    show screen title_card_display("Act 1") with dissolve
    pause 2.0
    hide screen title_card_display with dissolve
    pause 1.0
    call a1 from _call_a1
    return
#Minigame screens
