label a1s1: 
    scene bg living_room with in_confused
    play music "Garden_Scene_1.mp3"
    a """
    Another nightmare... same as every other...
    {i}"Sigh"{/i}
    I miss you, Val.
    """

    play audio "footsteps-4.mp3"
    a "..."
    
    play audio "cell-phone-vibrate-1.mp3"

    a "Hm...?"
    a "Oh. {i}Him{/i}"
    show ryan_default: 
        blur 16
    r "What's good, bro?"
    a "{cps=3}...{/cps}"
    r "Oh. {cps=20}Riii{/cps}{cps=*.5}iii{/cps}iiiii{cps=*.3}iiii{/cps}ght..{cps=*.1}.....{/cps}"
    r "How's Life?"
    a "B{w=1.0}a{w=1.0}d{w=3.0}."
    a "Still grieving my loss..."
    a "Still don't know how to move forward..."
    r "I see, I see."
    show ryan_default: 
        blur 40
    r "I'ts been a while since ya last called, and I was getting kinda worried"
    show ryan_default: 
        blur 16
    r "Ya practically dropped off the map after {cps=3}...{/cps} {size=*.5}that happened,{/size} {size=*.25}soo...{/size}"
    r "{cps=*2}Well, fair enough honestly. I get it."
    r "I'd be pretty fucked up if I lost someone as {i}{cps=2}fine{/i}{/cps} as Valerie"
    a "Can you... {i}not{/i} speak about my dead wife like that?"
    r "{cps=*2}Oh, my bad bro."
    a "Just give me some space. I {cps=3}don't{/cps} need your company right now."
    r "Oh, my bad bro.{p=0.9} {size=*.5}if you say so...{/size}"
    r "Buuuuuut I'm gonna be back in town soon, so..."
    a "...Sure, I guess."
    hide ryan_default
    play sound "cell-phone-hang-up-100514.mp3"


