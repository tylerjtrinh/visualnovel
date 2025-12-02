# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



label a0s1:
    window hide
    scene black
    pause 1.0
    play music "Garden_Scene_1.mp3"
    scene bg starry_sky with in_confused
    v mad "Hey… Hey! Did you fall asleep again?"

    menu:
        "No… I was just resting my eyes, I swear.":
            pass
    a awksmile "No… I was just resting my eyes, I swear."

    v normal "Sure you were..."
    
    a slightsmile "If my snoring bugs you that much, you can always leave."

    v "Tch… Nice try, Alex. You’re not getting rid of me any time soon~"
    
    v "...Come on, don't you love this view?"

    a normal "The stars are quite nice tonight."

    v "Mm-hm."

    #background change here
    scene bg grass_cutscene with fade
    v "You know..."

    a "Yea?"
    
    v "You spend too much time looking at the ground."
    
    v "You gotta look upwards sometimes~!"
    
    menu:
        "Maybe I should.":
            a "It’s not good for me to have such bad posture when I’m gardening, anyway."
            a "Looking at the stars seems like a good excuse for a break."
            v "Exactly!"
            v "Gotta do something other than the usual...  ya know?"
            pass
        "Hmm... maybe not.":
            a "I mean like my garden's got everything I need."
            a "It's hard work keeping the garden healthy, but its rewarding."
            v "Yeah, but you gotta stop working long enough to enjoy the reward."
            v "Live a little!"
            pass

    v "Oh, look!"
    #background change here Short pause. Maybe transition back to the starry sky 
    scene bg starry_sky with fade
    v happy "You can see Venus so clearly tonight!"

    a normal "Really?"
    
    v "And… oh, I think I see Mars up there as well!"
    #zoom into mars?

    #continue from here
    v normal "What’re the odds of that?"
    a "Well, I imagine…"
    v "Like, Venus and Mars have very different orbits, so it is quite curious that they’re both visible on this night."
    v "Maybe it means something really special’s gonna happen!"
    a "Or, maybe… They’re two big space rocks just floating around… and they just so happen to be floating a little closer together than usual."
    v "Space rocks?"
    v "Oh, Alex, they’re so much more than that!"
    v "They’re mystery, they’re beauty, they’re our lights in the unfathomable darkness, they’re the sources of myths and tales and all sorts of stories and–"
    a "…"
    v "Well, they’re just really cool…!"
    a "Yeah, so I’ve heard."
    a slightsmile "Anyway… Mind if I continue enjoying your lecture, dear~?"
    v maimeng "{i}Oh, you shouldn’t have~{/i}"


    #scene change

