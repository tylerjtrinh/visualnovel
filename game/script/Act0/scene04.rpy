label a0s4:
    scene bg starry_sky with fade
    show truck
    v "{cps=20}IS THAT A TRUCK?{/cps} {cps=*2}WHAT THE FU-{/cps}{nw}"
    scene bg white
    show truck
    play sound "automobile-horn-153260.mp3"
    stop music
    a "OH SHIT-{w=0.9}"
    show truck
    play sound "car-crash-sound-effect-376874.mp3"
    hide truck
    scene black with in_shatter
    pause 2.0