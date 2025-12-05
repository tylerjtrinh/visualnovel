label a2s2:
    menu:
        "Look inside the bag (pro-wife)":
            call a2s2_prowife
            return
        "Don't look inside the bag (anti-wife)":
            call a2s2_antiwife
            return

label a2s2_antiwife:
    a "..."
    narrator "Jason slinks back in."
    a "Welcome back."
    narrator "Valerie side eyes you."
    a "What you did was very wrong."
    j "Huh?"
    j "Never mind that...someone has done something very wrong."
    j "Very wrong!"
    j "And it's me!"
    narrator "Jason throws his hands in the air dramatically."
    j sigh "Oh, it's so over, it's so over!"
    a "Might I guess what is over?"
    j "She...she left me!"
    v "Ha!"
    j "She said that she couldn't handle the office romance."
    j "And that we're better off as coworkers."
    a "Well, I guess that's a sign—"
    j "And that I should focus on my wife."
    a "It is {i}definitely{/i} a sign, then."
    v "Great. Now let's get this guy out of here, please..."
    a "Jason, I'm sorry about that and all—"
    j "Not now, Alex."
    j "I need to go home."
    j "I think...I miss my wife."
    a "All well and good, then."
    return


label a2s2_prowife:
    narrator "You keep an eye trained on the door as your hand dips into Jason's work bag."
    a "Let's see here."
    v "I'll bet he has a..."
    a "Aha!"
    narrator "You pull out a slim metal rectangle."
    v "Ooh, a second phone! Scandalous!"
    a "That would be funny if he weren't actually in a scandal."
    narrator "Turning on the screen, you recognize it as his personal phone."
    a "That's odd."
    v "That's right, he does work an office job."
    v "The one he's on right now is probably a work phone."
    a "You're probably right."
    narrator "Memory kicks in from countless nights dialing a friend or a cab for Jason after a couple too many drinks."
    narrator "You key in his passcode."
    v "Nice work, hacker."
    a "Thanks, I learned from the best."
    narrator "Valerie has always been better than you with tech stuff."
    narrator "Or rather, you didn't care to be better."
    v "You always did prefer to be outside instead of on the screen."
    v "I admire that about you."
    narrator "You blush."
    v "Now, down to business."
    a "Here's his text messages...and here's his wife."

    v "So, what are you going to do?"

    menu:
        "Snoop":
            v "Come on, you're not going to do anything?"
            a "He's my friend..."
            v "He's not his own wife's friend!"
            v "You're already this far. Take it all the way."
        "Expose him":
            narrator "You resolve to end Jason's shenanigans once and for all."
            narrator "A few texts to his wife is sufficient."
            narrator "She doesn't respond right away, and you stow the phone, wanting nothing more to do with this."
            narrator "Jason opens the door frightfully soon after you step away from his bag."
            a "I didn't do anything!"
            j "Um, right. I didn't think so."
            j sigh "Anyway, something urgent came up."
            j "I need to go home."
            j "It was good seeing you, though, Alex."
            j "Call me if you need anything else."

    return