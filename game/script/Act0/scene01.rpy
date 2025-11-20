# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define in_eye = ImageDissolve("transitions/eye.png", 2.0)
define out_eye = ImageDissolve("transitions/eye.png", 6.0, reverse=True)

image bg living_room = "bg/living-room.png"
image bg starry_sky = "bg/sky.png"

label a0s1:
    window hide
    scene black
    pause 1.0

    scene bg starry_sky with in_eye
    v mad "Hey… Hey! Did you fall asleep again?"

    menu:
        "No… I was just resting my eyes, I swear.":
            pass
    a normal "No… I was just resting my eyes, I swear."

    v normal "Sure you were..."
    
    a "If my snorin bugs you that much, you can always leave."

    v "Tch… Nice try, Alex. You’re not getting rid of me any time soon~"
    
    v "...Come on, don't you love this view?"

    a "The stars are quite nice tonight."

    v "Mm-hm."

    #background change here
    v "You know..."

    a "Yea?"
    
    v "You spend too much time looking at the ground."
    
    v happy "You gotta look upwards sometimes~!"
    
    menu:
        "Maybe I should.":
            a "It’s not good for me to have such bad posture when I’m gardening, anyway."
            a "Looking at the stars seems like a good excuse for a break."
            v normal "Exactly!"
            v "Gotta do something other than the usual...  ya know?"
            pass
        "Hmm... maybe not.":
            a "I mean like my garden's got everything I need."
            a "It's hard work keeping the garden healthy, but its rewarding."
            v normal "Yeah, but you gotta stop working long enough to enjoy the reward."
            v "Live a little!"
            pass

    v normal "Oh, look!"
    #background change here Short pause. Maybe transition back to the starry sky b
    v happy "You can see Venus so clearly tonight!"

    a "Really?"
    
    v "And… oh, I think I see Mars up there as well!"
    #zoom into mars?

    #continue from here
    v "What’re the odds of that?"
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
    a "Anyway… Mind if I continue enjoying your lecture, dear~?"
    v "Oh, you shouldn’t have~"


    #scene change

