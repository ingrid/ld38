define reallyfarright = Position(xpos=.97, xanchor='center')
define farright = Position(xpos=.9, xanchor='center')  ##### ZAALIAH
define farright2 = Position(xpos=.8, xanchor='center')
define midright = Position(xpos=.7, xanchor='center')  ### CLOSE TO CENTER
define almostcenter = Position(xpos=.6, xanchor='center')
define almostcenter2 = Position(xpos=.6, xanchor='right')
define almostcenter3 = Position(xpos=.6, xanchor='left')
define midleft = Position(xpos=0.5, xanchor='right') ##### CLOSE TO CENTER
define farleft2 = Position(xpos=0.4, xanchor='right') ##### 2ND FURTHEREST
define farleft = Position(xpos=0.3, xanchor='right') #### BRETT
define reallyfarleft = Position(xpos=0.2, xanchor='right')
define squatting = Position(ypos=0.55, yanchor=0)

define truecenterleft = Position(xpos=0.2, ypos=0.5)
define truecenterright = Position(xpos=0.8, ypos=0.5)

init python:
    define.move_transitions('move', 0.5)
    define.move_transitions('quickmove', 0.25)

### INVERT

init:
    image startmeinvert = im.MatrixColor("bg/free_cave_backdrop_download_by_takenvortex-d8y3xe7.jpg",
                                       [ -1,  0,  0, 0, 1,
                                          0, -1,  0, 0, 1,
                                          0,  0, -1, 0, 1,
                                          0,  0,  0, 1, 0, ])

### SEPIA
#image startmeSepia= im.Sepia("images/patty.png")

image ocean = "BG/free_ocean_background__by_angrysushiroll-daad17s.jpg"

## TIME
init -1 python:
    import time
    time = time.localtime(time.time()).tm_wday
    days = ['Monday',    # 0
            'Tuesday',   # 1
            'Wednesday', # 2
            'Thursday',  # 3
            'Friday',    # 4
            'Saturday',  # 5
            'Sunday']    # 6

init -3:
    transform dramatic_zoom:
        parallel:
            zoom 1.0
            linear 7.0 zoom 1.2
        parallel:
            xalign 0.6 yalign 1
            linear 7.0 xalign 0.4 yalign 0.9

###### CHARACTERS
define mc = Character('Princess Mermaid', color="#FF0066")
define b = Character('Broody McGee', color="#FF0066")
define cf = Character('Childhood Friend 4 Eva', color="#FF0066")
define fadeWhite = Fade(1.0, 0.0, 1.0, color="#fff")
define seahorse_name = 'Kampos'

init:
    transform visible:
        alpha 1.0
    transform invisible:
        alpha 0.0
    define alphafade = AlphaFade(0.5, enter=invisible, leave=invisible)
    define alphafade1 = AlphaFade(1.0, enter=invisible, leave=invisible)
    define alphafade3 = AlphaFade(3.0, enter=invisible, leave=invisible)

label start:
    # Initializing data
    python:
        # Create skills (name, type, hit, power)
        attack = Skill("Attack", "attack", 70, 20)
        escape = Skill("Escape", "escape")

        # Create battle actors (name, max_hp, skills)
        hero = Actor("Princess",100, [attack,escape])
        goblin = Actor("Seaweed",40, [attack])
        jellyfish = Actor("Jellyfish",40, [attack])

        # Create a dungeon stage (map,enemy)
        # "1" means wall, "0" means path.
        stage1=Stage([
            "1111111111",
            "1111011001",
            "1000000001",
            "1110111101",
            "1000000001",
            "1111111111",
            ],
            enemy=goblin)

    # The game starts here.

    # Place a player position on a dungeon stage (stage,y,x,dy,dx).
    # dx,dy means direction. If dy=1, it's down. If dx=-1, it's left.
    $ here=Coordinate(stage1,2,2,0,1)
















## START
label story1:
    $ skeptic = 0
    $ believer = 0
    scene black
    play music "BGM/Morning Pauli Ondruska.ogg"

    "This is all I've ever known."
    "I wonder if it's all I'll ever know."

    "..."

    "That's kind of sad when I think of it like that."

    "I may not be an adventurer, but still since my parents have gone I am curious about what I am missing out there."

    "And now here I am."

    "I am heir to my own kingdom."

    "My own small kingdom, one of many other kingdoms as they say."

    "There's a whole ocean out there, and I just wonder which parts of the ocean belong to me."

    "Surely there's more than... this."

    cf "Of course there's more than this."

    mc "..."

    "That's Tristan."

    "The merman with the innate ability to read my mind."

    "Of course he's ever loyal, but he's also rather distinctly... {i}Tristan{/i}."

    "And yes, I mean that like it's a bad thing."

    mc "Really?"

    mc "I mean that's true that there have been legends for generations."

    mc "People are always saying that this and that about what is out there."

    mc "Anyway I-"

    menu:

        "Have never really believed what people have said.":
            $ skeptic += 1
            mc "If they think there's something that great out there..."
            mc "Then why does everyone's opinions about it change?"
            mc "Where are the hard facts?"
            cf "It's a feeling, you know that you know."
            mc "I'm sorry.  I don't have that feeling."
            cf "... I guess it's too hard for me to explain it to you."

        "Have always believed what people have said.":
            $ believer += 1
            mc "Of course, it has to be true."


        "Can't make up my mind.":
            mc "Besides, does it really matter in the end?"
            cf "I guess not, princess."
            mc "Exactly."

    cf "Your parents always believed."
    "{i}Ah yes.{/i}"
    "Tristan had been my companion growing up."
    "One of the ones who really looked out for me."
    "Even though he was annoying."

    cf "Oh, dear [mc]. You can wipe your nose on me, it is quite okay."

    "..."
    "And still was annoying."

    "He was one part fearless protector, one part insufferable know-it-all, and one part mer-doormat."

    "But I guess at the very least I knew he was always on my side."


    ############# LOVE INTEREST 2


    "Outside the sea castle however, things were a different story."

    "Yes, I was treated with respect..."

    "But somehow it felt that everyone was just telling me what they wanted me to hear."

    "Was anyone being honest with me?"

    "Maybe no one else thought any sort of deep questions like the nature of reality."

    "All of that stuff."

    cf "Anyway [mc], you at very least don't want to be taking advice from just anyone."

    cf "There are mer-people around that just aren't very trustworthy."

    cf "That have a reputation."

    "Tristan gave a nod."

    cf "That guy."

    mc "Oh.  {b}That guy.{/b}"

    "I have no idea which guy he means."

    "{i}Ohhhhh. The one who looks homeless.{/i}"

    mc "So are you saying he might have the answers I'm looking for."

    cf "No!"

    cf "That's exactly what I wasn't saying."

    cf "He is exactly the mer-person that you shouldn't be talking with."

    cf "He is just trying to confuse mer-people."

    cf "There is a big wide world out there and there is land - LAND!"

    cf "Of course we can only vaguely picture what that land looks like, but I'm sure it's like the legends."

    cf "And mer-people don't swim, they get around completely differently through-out the land."

    menu:

        "Poppycock.":
            $ skeptic += 1
            mc "Old wives tales, surely."
            mc "Nobody really takes them seriously."
            cf "..."
            cf "I do."

        "That would be wonderful.":
            $ believer += 1
            mc "Sometimes I dream about what it would be like without these flippers."
            mc "I would feel so free... but I just have no idea of how it would work."
            mc "How I would move."
            mc "Still, it is a nice dream."


        "I've heard the legends.":
            mc "I wasn't born yesterday."
            mc "Of course I've heard of them."
            cf "I didn't mean to imply that you were that naive."
            cf "I just like talking about them."
            mc "Hm."


    mc "How do you know so much about this guy anyway?"
    cf "I saw him on Merman Mingle- errr- nothing."
    cf "I mean, everybody knows about him.  He's always creating a stir... and this is such a close knit kingdom after all."

    mc "That is true."

    "Everyone knew almost everyone."
    "And even though they were my loyal subjects I felt much of a kinship to everyone-"
    "{i}Possibly because I was related to most of them.{/i}"

  ############## TRYING TO MAP OUT

    play music "BGM/Meds - wobbly.ogg"

    mc "So what's this?"

    mc "I've poured through all of the maps and it just seems to go on forever."

    mc "Doesn't the world end someplace?"

    mc "I want to find out where it all goes."

    "Brisco looked over the maps."

    b "That's not what the world looks like."

    menu:

        "That's what I thought too":
            $ skeptic += 1
            mc "You may be right, you know?"
            b "..."
            b "Just figuring that out now?"
            mc "You know, I can just take my compliment back again..."

        "How do you know that?":
            $ believer += 1
            mc "You seem to just magically have all the answers."
            b "Perhaps that's because I do have all the answers."


        "Whatever.  It's all the same.":
            mc "Besides, does it really matter in the end?"
            cf "I guess not, princess."
            mc "Exactly."

    mc "So this is really getting me nowhere."

    b "If you want to go out, you have to explore."

    b "You have to see things yourself with fresh eyes."

    cf "That's a terrible idea."

    with hpunch

    mc "Gah!"

    mc "Where did you come from?"

    cf "Oh, shadows are really helpful at hiding mer-people."

    cf "You should try it some time."

    mc "..."

    b "He is right about that."

    b "But not about what you should do..."

    b "Are you going to listen to this stick in the mud, or are you going to have an adventure?"

    if skeptic > believer:
        mc "I'm ready for the adventure!"

        cf "..."

        cf "I'm not sure I can let you do that, [mc]."

        mc "Oh quit being that stick in the mud.  Besides, I'll have [seahorse_name]."

        cf "Don't you think for a second that I'm going to let you go on your own."


    elif believer > skeptic:
        mc "That stick in the mud knows the ways around here better than anyone."

        mc "Besides, shouldn't we stick to what we know?"

        cf "That is true.  Sticking to what one knows is always best."

        b "..."

        b "This mer-guy has to be joking, right?"

        mc "He's just really protective."





  ############## DUNGEON CRAWL

    play music "BGM/Savfk - Odyssey.ogg"


# To start exploring, call or jump to the label dungeon.
    call dungeon from _call_dungeon

    # To start battling, call the label battle with 2 actor objects: player and enemy.
    call battle(hero,goblin,jellyfish) from _call_battle_1

  ###### OPTION TO TURN BACK / CHILDHOOD FRIEND ROMANCE END




label turnback:
    cf "I can't keep doing this."








  ########### ENDING
label gettotheglass:
    "I hit something."

    "Why did I hit something?"

    if skeptic > believer:
        "BAM."

        mc "There's something wrong here."

        b "Your little world somehow became that much smaller, huh?"

        "It was as if he was revelling in me discovering the truth."

        "He didn't have to be so smug."

        "{i}This isn't real.{/i}"




    return
