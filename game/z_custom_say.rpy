
init python:
    DIALOG_WIDTH = 1200
    DIALOG_HEIGHT = 250

# Dialog box styles 
style unified_dialog_outer:
    background Solid("#1a1a1ada")
    xpadding 3
    ypadding 3

style unified_dialog_inner:
    background Solid("#2a2a2ada")
    xpadding 30
    ypadding 20

style unified_dialog_top:
    background Solid("#2a2a2ada")
    xpadding 30
    ypadding 20

style unified_name_text:
    size 24
    bold True

style unified_dialogue_text:
    color "#ffffff"
    size 24
    layout "subtitle"
    xmaximum DIALOG_WIDTH - 66
    text_align 0.0
    xalign 0.0
    yalign 0.0

style centered_text:
    color "#ffffff"
    size 28
    text_align 0.5
    xalign 0.5
    yalign 0.5

style unified_choice_button:
    background Solid("#444444")
    hover_background Solid("#555555")
    color "#ffffff"
    xpadding 20
    ypadding 12
    size 22

# SAY screen 
screen say(who, what):
    tag say
    zorder 100

    # Check for centered text
    if who is centered or who == "centered" or str(who).lower() == "centered":
        text what id "what":
            style "centered_text"
            xalign 0.5
            yalign 0.5
            text_align 0.5
    else:
        # Normal dialog box 
        
        # Character side image
        if (who is not None and who != "") and not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

        # Gray box
        frame:
            style "unified_dialog_outer"
            xalign 0.5
            yalign 1.0
            yoffset -40
            xsize DIALOG_WIDTH
            ysize DIALOG_HEIGHT

            frame:
                style "unified_dialog_inner"
                xfill True
                yfill True

                fixed:
                    xfill True
                    yfill True
                    
                    # Name at top 
                    if who is not None:
                        text who id "who" style "unified_name_text" xpos 0 ypos 0

                    # Dialog text positioned under name
                    text what id "what" style "unified_dialogue_text" xpos 0 ypos 35

                    

# CHOICE screen 
screen choice(items):
    tag choice
    zorder 101

    vbox:
        xalign 0.5
        ypos 405
        yanchor 0.5
        spacing 8
        
        for i in items:
            textbutton i.caption action i.action style "unified_choice_button"