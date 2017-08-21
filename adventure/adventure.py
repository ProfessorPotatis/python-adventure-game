#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how command-line options can be handled by a script.
"""



import sys
import os
#from datetime import datetime
import getopt



#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Sofia Kristiansen"
EMAIL = "sofiakristiansen@gmail.com"
VERSION = "1.0"
USAGE = """{program} - Bucketlist – The Game. By {author} ({email}), version {version}.

Usage:
  {program} [options]

Options:
  -h --help                      Displays this help message.
  -i --info                      Displays a description of the game.
  -v --version                   Print version and exit.
  -a --about                     Displays a short description of the author.
  -c --cheat                     Displays shortcuts and cheats in the game.

Commands in game:
  [i] OR [info]          Displays a description of the country or room you're in.

  [h] OR [help]          Displays this list of commands you can carry out.

  [fr] OR [forward]      Go to the next country or room, if it's available.

  [ba] OR [backward]     Go back to the country or room you came from.

  [look]                 Look around.

  [l] OR [lead]          Displays a hint, or more.

  [o] OR [object]        Displays the objects in the room or country you're in.

  [w] OR [watch]         Displays a description of the specific object.
     + [name of object]

  [o] OR [open]          Opens the specific object, if possible.
     + [name of object]

  [k] OR [kick]          Kicks the specific object, if possible.
     + [name of object]

  [m] OR [move]          Moves the specific object, if possible.
     + [name of object]


""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)
MSG_AUTHOR = "{author} can be contacted by email {email}.".format(author=AUTHOR, email=EMAIL)
COMMANDS = """
Commands:
  [i] OR [info]          Displays a description of the country or room you're in.

  [h] OR [help]          Displays this list of commands you can carry out.

  [fr] OR [forward]      Go to the next country or room, if it's available.

  [ba] OR [backward]     Go back to the country or room you came from.

  [look]                 Look around.

  [l] OR [lead]          Displays a hint, or more.

  [o] OR [object]        Displays the objects in the room or country you're in.

  [w] OR [watch]         Displays a description of the specific object.
     + [name of object]

  [o] OR [open]          Opens the specific object, if possible.
     + [name of object]

  [k] OR [kick]          Kicks the specific object, if possible.
     + [name of object]

  [m] OR [move]          Moves the specific object, if possible.
     + [name of object]
"""

#AIRPORT
AIRPORT_INFO = """
You've decided to check off all of your bucketlist items at the same time and gone to the nearest airport to get going.
You have a backpack with you with all the stuff you need, if you want you can check it out by typing in 'inv'.
First on your bucketlist is to go to Paris to see the Eiffel Tower.

You arrive to a small airport early in the morning and there are almost no people to be seen.
You are kind of thirsty, so you pick up a water bottle at 7/11 and put it in your backpack 'inv'.
You then proceed to check in at the counter and get your boarding pass for the flight to Paris.
You put the boarding pass in your backpack.
You are now ready to go through the security check.

                        ----------------
                        |Security Check|
                        |  |!| ______  |
                        | :   :     :  |
                        | :   :  :  :  |
                        | :   :  :  :  |
                        | :   :  :  :  |
                        | :   :  :  :  |
                        | :______:  :  |
                        ---------///----

To see your options type in: 'h' or 'help'.
"""
AIRPORT_LOOK = """
At the security check there are black ropes put up in a zig-zag manner, so that no one can cut in line.
As you are at the airport early there are only you and two other people queing.
You are number three in line.
There are a mix of women and men working with checking everyones handluggage for prohibited items at the front counter.
There's also a sign in front of the line, which you can't see yet as it is pointed in the wrong direction.
"""
AIRPORT_LEAD = """
Maybe you should move the sign so that you are able to read it?
Type 'm sign' or 'move sign' to do so.
"""
AIRPORT_OBJ = """
At the front of the line there's a sign pointed in the wrong direction.
"""

#PARIS
PARIS_INFO = """
It's a beautiful springday in Paris.
You decide to make your way to the Eiffel Tower immediatly and take a shortcut through a small alleyway.
You hear birds singing and feel the sun warming your skin as you approach what you came for:
The magnificent Eiffel Tower that is towering before your eyes.

On the grass around the tower people are having picknicks and taking touristphotos of themselves.
As you are about to pick up your camera from your backpack a gang of shady looking folks makes their way towards you.

– Hand over that camera and all of your money!
"""
PARIS_LOOK = """
You look around at the shady looking folks. They are the same height as you, and you certainly could take them out if you wanted to.
The gang leader looks as if he is about to grab your backpack from you.
You look down to your feet and see that you are wearing your steelcap boots.
"""
PARIS_LEAD = """
As you are wearing your steelcap boots, maybe you should use your feet to defend yourself?
Type 'k gang leader' or 'kick gang leader' to do so.
"""
PARIS_OBJ = """
The gang leader.
"""

#ROME
ROME_INFO = """
The Colosseum is an oval amphitheatre in the centre of the city of Rome.
Built of concrete and sand, it is the largest amphitheatre ever built. The
Colosseum is situated east of the Roman Forum.
"""
ROME_LOOK = """
As you stroll around the ancient Piazza del Colosseo you notice that someone has
concreted a small crack quite recently.
"""
ROME_LEAD = """
I wonder what's inside that crack that has been recently concreted...
"""
ROME_OBJ = """
Cracking concrete.
"""
ROME_NEWOBJ = """
Ancient chest.
"""

#ZURICH
ZURICH_INFO = """
You crack the door open and take the stairs up to level four.
You end up in a long corridor. At the end of the corridor there's a sign on a wooden
door. It says:

-----------------------------------
|                                 |
|  Learn german in five minutes   |
|                                 |
-----------------------------------

Sounds a bit shady, but you're curious and don't have much else to do.
You enter the room.
"""
ZURICH_LOOK = """
The room is empty. There are no people to be seen anywhere. The only thing you
notice is a book laying on the floor in the middle of the room.
"""
ZURICH_LEAD = """
Maybe you could open the book.
"""
ZURICH_OBJ = """
Book.
"""

#BERLIN
BERLIN_INFO = """
'What's all the fuzz about?' you think to yourself when you stand and spectate the wall.
As you are not a very well-read kind of person, you wonder if the fuzz is about how
the wall was built.
"""
BERLIN_LOOK = """
You look at the wall some more, but can't figure it out.
'It's just a wall' you think to yourself. 'Not a very good one either.'
You see others taking pictures of themselves pretending to move or kick the wall.
"""
BERLIN_LEAD = """
Try to move or kick the berlin wall.
"""
BERLIN_OBJ = """
Berlin wall.
"""

#LONDON
LONDON_INFO = """
The Port of London lies along the banks of the River Thames from London, England to the North Sea.
The port can handle cruise liners, ro-ro ferries and cargo of all types including
containers, timber, paper, vehicles, aggregates, crude oil, petroleum products,
liquefied petroleum gas, coal, metals, grain and other dry and liquid bulk materials.
"""
LONDON_LOOK = """
At the port you see a ship that is about to load its cargo. With a huge crane it
takes shipping containers and puts them on the boat, one by one. It still has
some shipping containers to load, before it can take off to Thailand. One of the
containers that is about to get loaded on board is one that is close to you.
"""
LONDON_LEAD = """
That shipping container could be a comfy ride to Thailand.
"""
LONDON_OBJ = """
Shipping container.
"""

#THAILAND
THAI_INFO = """
You arrive to Phra Nang Beach with a longtail boat from Ao Nang in the afternoon.
You jump in the water and the fine white sand finds its way between your toes.
This lovely beach was recently voted one of the 10 most beautiful beaches in the world.
And has jaw-dropping spectacular scenery. Cliffs towers themselves out of the water
and embraces the beach so that it feels like a secluded one.

You find a bungalow you like under one of the palmtrees and pays for a nights stay.
"""
THAI_LOOK = """
When you look around you see climbers climbing the cliffs, people ordering food
from longtail boats, others sunbathing and swimming and some exploring the caves.
Behind the strip of sand there are a couple of bungalows hiding under the palmtrees.
"""
THAI_LEAD = """
Maybe you should go check out your bungalow.
"""
THAI_OBJ = """
Beach bungalow.
"""

#ASCII ART
ASCII_EARTH = """
                                     ,,,,,,
                                 o#'9MMHb':'-,o,
                              .oH":HH$' "' ' -*R&o,
                             dMMM*""'`'      .oM"HM?.
                           ,MMM'          "HLbd< ?&H .
                          .:MH ."/          ` MM  MM&b
                         . "*H    -        &MMMMMMMMMH:
                         .    dboo        MMMMMMMMMMMM.
                         .   dMMMMMMb      *MMMMMMMMMP.
                         .    MMMMMMMP        *MMMMMP .
                              `#MMMMM           MM6P ,
                          '    `MMMP"           HM*`,
                           '    :MM             .- ,
                            '.   `#?..  .       ..'
                               -.   .         .-
                                 ''-.oo,oo.-''

"""
ASCII_AIRPORT = """
                        ----------------
                        |Security Check|
                        |  |!| ______  |
                        | :   :     :  |
                        | :   :  :  :  |
                        | :   :  :  :  |
                        | :   :  :  :  |
                        | :   :  :  :  |
                        | :______:  :  |
                        ---------///----

"""
ASCII_SIGN = """
There is something written on the sign.

                    ----------------------------
                    |                          |
                    |  No water bottles aloud  |
                    |  through security check. |
                    |                          |
                    | Empty your backpack 'inv'|
                    |   of prohibited items.   |
                    |                          |
                    ----------------------------
"""
ASCII_PARIS = """
                    |
                    |
                    A
                  _|X|_
                  ||X||
                   |V|
                   |A|
                   |V|
                 .|XXX|.
                  |xxx|
                  |xxx|
                  |xxx|
                  |xxx|
                  |xxx|
                  |xxx|
                 IIIIIII
                 |x|_|x|
               .|x.| |.x|.
                |x|   |x|
              .|xX|___|Xx|.
              IIIIIIIIIIIII
            .x`-||XXXXX||-`x.
          .x`.-.xx|xIx|xx.-.`x.
         .x`x-x_.-"` `"-._ x-xx.
        .x.-'.'           '.'-.x.
       .x`x-x               x-x`x.
     _x`-.x`_               _`x.-`x_
    `_______`                `_______`
"""
ASCII_ROME = """
   __        __________________
  ===     /======================_,
 |      II IIII IIII IIII IIII III
 |II   II   II   II   II   II   II   / ___
<==========================================,__
 | II IIII IIII IIII IIII IIII IIII IIII IIII  |
 |II   II   II   II   II   II   II   II   II   II   II   II|
<============================================================>
 | II IIII IIII IIII IIII IIII IIII IIII IIII IIII IIII II |
 |II   II   II   II   II   II   II   II   II   II   II   II|
<============================================================>
 | II IIII IIII IIII IIII IIII IIII IIII IIII IIII IIII II |
 |II   II   II   II   II   II   II   II   II   II   II   II|
=============================================================
"""
ASCII_ZURICH = """
                        ----------------
                        |              |
                        |      []      |
                        |              |
                        -------//-------
"""
ASCII_BERLIN = """
 ____________________________________
   |__|__|__|__|__|__|__|__|__|__|__|
   __|__|__|__|__|__|__|__|__|__|__|
   _|__|__|__|__|__|__|__|__|__|__|__|
   |__|__|__|__|__|__|__|__|__|__|__|__|_

"""
ASCII_LONDON = """
                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     |                                                             /
      |___________________________________________________________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwww|_______|wwwwwwwwwwwwwwww|_______|wwwwwwwwwwwwwwwwwwww|______|wwwwwwww
   wwwwwwwwwwwwwww|______|wwwwwwwwwwwwwwww|________|wwwwwwwwwwwwwwwwwwwwww
"""
ASCII_SIGN_THAI = """
                    -------------------------
                    |                       |
                    |  Welcome to Thailand! |
                    |  The land of smiles.  |
                    |           :)          |
                    -------------------------
"""
ASCII_THAI = """
                           #####
                       #######
            ######    ########       #####
        ###########/#####/#####  #############
    ############/##########--#####################
  ####         ######################          #####
 ##          ####      ##########/@@              ###
#          ####        ,-.##/`.#/#####               ##
          ###         /  |$/  |,-. ####                 #
         ##           |_,'$|_,'|  |  ###
         #              |_$$$$$`._/   ##
                          $$$$$_/     ##
                          $$$$$        #
                         $$$$$    _.--  --._
                        $$$$$   ,'           `.
                        $$$$$ .|               |.
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~
   ~      ~  ~    ~  ~ $$$$$  ~   ~       ~          ~
       ~ ~      .o,    $$$$$     ~    ~  ~        ~
  ~            ~ ^   ~ $$$$$~        ______    ~        ~
_______________________$$$$$________||||||||_________________
                       $$$$$        |>|||||||.
    ______             $$$$$        |>>|||||||.
   |Q%== ,|            $$$$$       /|>>|#####|
    ------             $$$$$      /=||>|#####|
                       $$$$$        ||||#####|
                      $$$$$$$          ||---||
                      $$$$$$$          ||   ||
---------------------$$$$$$$$$-------------------------------
                        $$$
"""
ASCII_ENDGAME = """
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 |*        |   |             /
       '          |     '* |    |  *        |*                *  *
            *      `.       |   |     *     /    *      '
  .                  |      |   |          /               *
     *'  *     '      |      |   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *|*          * .   .      *
*  '        *    `-._       CONGRATULATIONS!    .         _..:='        *
             .  '    * YOU COMPLETED THE BUCKETLIST    *   .       _.:--'
          *     .   AND ARE NOW A BUCKETLIST CHAMPION *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '
"""

#
# Global default settings affecting behaviour of script in several places
#
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2

AIRPORT_SIGN = False
PARIS = False
KICKED_GANGLEADER = False
ROME = False
CRACK_CONCRETE = False
OPEN_CHEST = False
ZURICH = False
ZU_BOOK = False
BERLIN = False
BE_WALL = False
LONDON = False
LO_CONTAINER = False
THAILAND = False
BUNGALOW_DOOR = False
ENDGAME = False


def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)



def printInfo():
    """
    Displays a description of the game.
    """
    print("Bucketlist – The Game")
    print("Go to foreign countries, learn something new and complete the activities.")
    print("Check off all of the bucketlist items to become a bucketlist champion and win the game.")
    sys.exit(EXIT_SUCCESS)



def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)



def printAbout():
    """
    Displays a short description of the author.
    """
    print("About the author:")
    print("Sofia Kristiansen is a freelance gamemaker.")
    print("Her specialty is textbased adventure games made in Python.")
    print(MSG_AUTHOR)
    sys.exit(EXIT_SUCCESS)



def printCheat():
    """
    Displays shortcuts and cheats in the game.
    """
    print("CHEATER!")
    print("At the airport security check: inv drop water bottle.")
    print("In Paris: kick gang leader")
    print("In Rome: kick cracking concrete, then open ancient chest.")
    print("In Zürich: open book.")
    print("In Berlin: kick berlin wall or move berlin wall.")
    print("In London: open shipping container.")
    print("In Thailand: open beach bungalow.")
    sys.exit(EXIT_SUCCESS)



def inventory():
    """
    Shows what the player has in his/her backpack.
    """
    invFile = open("inv.data")
    showInv = invFile.readlines()
    numOfItems = len(showInv)

    print("You've got the following items in your backpack:\n" + str(showInv))
    print("\nThere are %s item(s) in your backpack." %numOfItems)
    print("To pick up something write 'inv pick'.")
    print("To drop something write 'inv drop'.")

    gameChoice()



def pick():
    """
    The player picks the choosen item and puts it in his/her backpack 'inv.data'.
    """
    pickUp = input("What do you want to pick up? ")
    invFile1 = open("inv.data")
    showInv1 = invFile1.readlines()
    invFile1.close()

    invFile1 = open("inv.data", "w")
    showInv1.append(pickUp + "\n")
    print("You picked up %s and put it in your backpack." %pickUp)
    for item in showInv1:
        invFile1.write(item)
    invFile1.close()

    gameChoice()



def drop():
    """
    The player drops the choosen item out of his/her backpack 'inv.data'.
    """
    global PARIS

    dropThis = input("What do you want to drop? ")
    invFile2 = open("inv.data")
    showInv2 = invFile2.readlines()
    invFile2.close()

    invFile2 = open("inv.data", "w")
    showInv2.remove(dropThis + "\n")
    print("You dropped %s out of your backpack." %dropThis)
    for item in showInv2:
        invFile2.write(item)
    invFile2.close()

    if "water bottle\n" not in showInv2:
        print("\nThe security check personel checked your handluggage, but did not find any prohibited items.")
        print("You are free to go to Paris. Type 'fr' or 'forward' when ready.")
        PARIS = True

    gameChoice()



def startGame():
    """
    Starts the game.
    Displays the storyline of the game.
    The player starts of at the airport.
    Displays a description and a textbased picture of the airport.
    """
    print("Welcome to Bucketlist – The Game!")
    print(ASCII_EARTH)
    print("A game where you go to foreign countries to complete activities or learn something new.")
    print("Check off all of the bucketlist items to become a bucketlist champion and win the game.")
    print("\nAre you ready to complete that bucketlist?")
    print("Write 'start' to get going!")

    gameChoice()



def airport():
    """
    First room of the game.
    The player is at the airport ready to go through the security check.
    The player is travelling with handluggage only, his/her backpack.
    The handluggage can be checked by writing 'inv'.
    """
    global PARIS

    waterBottle = "water bottle"
    boardingPassParis = "Paris boarding pass"
    invFile4 = open("inv.data")
    showInv4 = invFile4.readlines()
    invFile4.close()

    if "water bottle\n" not in showInv4:
        invFile4 = open("inv.data", "w")
        showInv4.append(waterBottle + "\n")
        for item in showInv4:
            invFile4.write(item)
        invFile4.close()

    if "Paris boarding pass\n" not in showInv4:
        invFile4 = open("inv.data", "w")
        showInv4.append(boardingPassParis + "\n")
        for item in showInv4:
            invFile4.write(item)
        invFile4.close()

    print(AIRPORT_INFO)

    if "water bottle\n" not in showInv4:
        print("\nThe security check personel checked your handluggage, but did not find any prohibited items.")
        print("You are free to go to Paris. Type 'fr' or 'forward' when ready.")
        PARIS = True

    gameChoice()



def paris():
    """
    Second room of the game.
    The player is now in Paris ready to go see the Eiffel Tower.
    The player is supposed to watch the Eiffel Tower, but has to kick a gang of robbers on his/her way there.
    """

    boardingPassParis2 = "Paris boarding pass"
    invFile5 = open("inv.data")
    showInv5 = invFile5.readlines()
    invFile5.close()

    if "Paris boarding pass\n" not in showInv5:
        invFile5 = open("inv.data", "w")
        showInv5.append(boardingPassParis2 + "\n")
        for item in showInv5:
            invFile5.write(item)
        invFile5.close()

    invFile5 = open("inv.data", "w")
    showInv5.remove(boardingPassParis2 + "\n")
    print("\nAt the gate you hand over your %s to a lady behind the gates counter." %boardingPassParis2)
    for item in showInv5:
        invFile5.write(item)
    invFile5.close()

    print("– You are just in time to board the flight to Paris, she says.")
    print("\nYou make your way to your seat, buckle up and fall asleep.")
    print("After a couple of hours you land in Paris.")
    input("\nPress enter to continue...")
    print(ASCII_PARIS)
    print(PARIS_INFO)

    gameChoice()



def rome():
    """
    Third room of the game.
    The player is now in Rome, strolling around piazza del colosseo.
    Notices a recently concreted crack that looks suspicious.
    After kicking the cracking concrete the player finds an ancient chest.
    The ancient chest contains a train ticket to the next destination.
    """
    print("\nYou get to Rome in the early evening and decide to go for a stroll in Piazza del Colosseo.")
    input("\nPress enter to continue...")
    print(ASCII_ROME)
    print(ROME_INFO)

    gameChoice()



def zurich():
    """
    Fourth room of the game.
    The player is now in Zürich.
    The player is supposed to learn german before being able to go to Berlin.
    """
    print("\nOn the train to Zürich you get some well needed sleep.")
    print("A couple of hours later you wake up to the sound of the train pulling into Zürich Hauptbahnhof.")
    print("As you are well rested you feel like meeting up some locals to practise your german.")
    print("You make your way to a building you've seen a language course ad for.")
    input("\nPress enter to enter the building...")
    print(ZURICH_INFO)
    print(ASCII_ZURICH)

    gameChoice()



def berlin():
    """
    Fifth room of the game.
    The player is now in Berlin.
    The player is supposed to go watch the berlin wall and move or kick it before
    fleeing to London.
    """
    print("\nAfter a bumpy ride from Zürich to Berlin you want to do something touristy.")
    print("You've heard about the Berlin wall, but never seen or been near it.")
    print("So you decide to go have a look.")
    input("\nPress enter to go to the Berlin wall...")
    print(ASCII_BERLIN)
    print(BERLIN_INFO)

    gameChoice()



def london():
    """
    Sixth room of the game.
    The player is now in London.
    Still being chased by the police for what the player has done in Berlin, the
    player now has to come up with a plan to flee Europe and still complete his/
    her bucketlist.
    """
    print("\nYou made it to London, and you've almost completed your bucketlist.")
    print("You are still being chased by the police and have to leave Europe.")
    print("Luckily the last item of your bucketlist is to stay at a beach bungalow in Thailand.")
    print("In that way you could easily flee Europe and still complete your bucketlist.")
    input("\nPress enter to go to the Port of London...")
    print(LONDON_INFO)
    print(ASCII_LONDON)

    gameChoice()



def thailand():
    """
    Seventh room of the game.
    The player is now in Thailand, the last destination on his/her bucketlist.
    After fleeing Europe the player now has to move into a beach bungalow and
    stay there for the rest of his/her life. Not a to shabby way to live life
    as the player still is able to explore Asia, Australia, America and so on.
    The game ends with a ASCII picture of fireworks.
    """
    print(ASCII_SIGN_THAI)
    print("After three weeks inside a shipping container you've finally reached your last destination.")
    print("You look at your bucketlist and notice that the only thing you have to do now is to enter a beach bungalow.")
    input("\nPress enter to go to Phra Nang Beach...")
    print(THAI_INFO)
    print(ASCII_THAI)

    gameChoice()



def congrats():
    """
    YOU MADE IT! YOU WON!
    """
    print(ASCII_ENDGAME)



def gameChoice():
    """
    Choices that can be made in the game via command-line.
    """
    global AIRPORT_SIGN, PARIS, ROME, KICKED_GANGLEADER, ZURICH, \
    CRACK_CONCRETE, OPEN_CHEST, ZU_BOOK, BERLIN, BE_WALL, LONDON, LO_CONTAINER, \
    THAILAND, BUNGALOW_DOOR, ENDGAME

    invFile3 = open("inv.data")
    showInv3 = invFile3.readlines()

    choice = input("--> ")

    #gamestart options
    if "exit" in choice:
        print("You have now exited Bucketlist - The Game.")
        return

    elif "start" in choice:
        airport()


    #inventory options
    elif "inv" and "pick" in choice:
        pick()

    elif "inv" and "drop" in choice:
        drop()

    elif "inv" in choice:
        inventory()


    #airport object options
    elif choice == "w sign":
        if PARIS == False:
            if AIRPORT_SIGN == True:
                print(ASCII_SIGN)
                gameChoice()
            elif AIRPORT_SIGN == False:
                print("\nYou are not able to see what's written on the sign, as it is pointed in the wrong direction.")
                gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch sign":
        if PARIS == False:
            if AIRPORT_SIGN == True:
                print(ASCII_SIGN)
                gameChoice()
            elif AIRPORT_SIGN == False:
                print("\nYou are not able to see what's written on the sign, as it is pointed in the wrong direction.")
                gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o sign":
        if PARIS == False:
            print("\nYou can't open a sign, silly.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open sign":
        if PARIS == False:
            print("\nYou can't open a sign, silly.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k sign":
        if PARIS == False:
            print("\nYou kicked the sign. That's not very nice, so the security kicks you out of the airport.")
            print("You now have to start from the beginning.")
            input("Press enter...")
            startGame()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick sign":
        if PARIS == False:
            print("\nYou kicked the sign. That's not very nice, so the security kicks you out of the airport.")
            print("You now have to start from the beginning.")
            input("Press enter...")
            startGame()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m sign":
        if PARIS == False:
            AIRPORT_SIGN = True
            print("\nYou moved the sign so that you are able to see what's written on it.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move sign":
        if PARIS == False:
            AIRPORT_SIGN = True
            print("\nYou moved the sign so that you are able to see what's written on it.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()


    #paris object options
    elif choice == "w gang leader":
        if ROME == False:
            print("\nThe gang leader is a man. He looks gnarly and stares angrily at you.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch gang leader":
        if ROME == False:
            print("\nThe gang leader is a man. He looks gnarly and stares angrily at you.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o gang leader":
        if ROME == False:
            print("\nYou can't do that.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open gang leader":
        if ROME == False:
            print("\nYou can't do that.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k gang leader":
        if ROME == False:
            KICKED_GANGLEADER = True
            print("\nYou kicked the gang leader and he falls flat on his face in pain.")
            print("You've already seen what you came for in Paris so you jump on the next plane leaving the country.")
            print("It just so happens to be a flight to Rome, the next item on your Bucketlist!")
            print("\nType 'fr' or 'forward' to flee Paris and go to Rome.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick gang leader":
        if ROME == False:
            KICKED_GANGLEADER = True
            print("\nYou kicked the gang leader and he falls flat on his face in pain.")
            print("You've already seen what you came for in Paris so you jump on the next plane leaving the country.")
            print("It just so happens to be a flight to Rome, the next item on your Bucketlist!")
            print("\nType 'fr' or 'forward' to flee Paris and go to Rome.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m gang leader":
        if ROME == False:
            print("\nThe gang leader is to heavy to move.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move gang leader":
        if ROME == False:
            print("\nThe gang leader is to heavy to move.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()


    #rome object options
    elif choice == "w cracking concrete":
        if ZURICH == False:
            print("\nIt looks as if someone has recently concreted a crack. The concrete looks wet.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch cracking concrete":
        if ZURICH == False:
            print("\nIt looks as if someone has recently concreted a crack. The concrete looks wet.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o cracking concrete":
        if ZURICH == False:
            print("\nYou can't do that.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open cracking concrete":
        if ZURICH == False:
            print("\nYou can't do that.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k cracking concrete":
        if ZURICH == False:
            CRACK_CONCRETE = True
            print("\nYou kicked the cracking concrete and made a hole big enough so you can see what's hiding inside.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick cracking concrete":
        if ZURICH == False:
            CRACK_CONCRETE = True
            print("\nYou kicked the cracking concrete and made a hole big enough so you can see what's hiding inside.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m cracking concrete":
        if ZURICH == False:
            print("\nYou can't move the concrete, you need more force.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move cracking concrete":
        if ZURICH == False:
            print("\nYou can't move the concrete, you need more force.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o ancient chest":
        if ZURICH == False:
            if CRACK_CONCRETE == True:
                OPEN_CHEST = True
                print("\nThe chest makes a cracking noise when you open it.")
                print("Inside the chest lies a train ticket to Zürich.")
                print("And what do you know? Zürich has always been a lifelong dream of yours to visit.")
                if "Zürich train ticket\n" not in showInv3:
                    invFile3 = open("inv.data", "w")
                    showInv3.append("Zürich train ticket\n")
                    for item in showInv3:
                        invFile3.write(item)
                    invFile3.close()
                print("\nType 'fr' or 'forward' to jump on the train to Zürich.")
                gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open ancient chest":
        if ZURICH == False:
            if CRACK_CONCRETE == True:
                OPEN_CHEST = True
                print("\nThe chest makes a cracking noise when you open it.")
                print("Inside the chest lies a train ticket to Zürich.")
                print("And what do you know? Zürich has always been a lifelong dream of yours to visit.")
                if "Zürich train ticket\n" not in showInv3:
                    invFile3 = open("inv.data", "w")
                    showInv3.append("Zürich train ticket\n")
                    for item in showInv3:
                        invFile3.write(item)
                    invFile3.close()
                print("\nType 'fr' or 'forward' to jump on the train to Zürich.")
                gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    #zurich object options
    elif choice == "w book":
        if BERLIN == False:
            print("\nThe book looks old and used. The cover is a bit dusty.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch book":
        if BERLIN == False:
            print("\nThe book looks old and used. The cover is a bit dusty.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o book":
        if BERLIN == False:
            ZU_BOOK = True
            print("\nAs you open the book you are instantly drawn into it.")
            print("You are tumbling around like they do in those time travel movies.")
            print("After what feels like only a couple of seconds you are back at the Zürich Hauptbahnhof.")
            print("You don't remember how, but suddenly you speak fluent german.")
            print("You feel ready to leave Zürich and jump on the train to the next item on your bucketlist.")
            print("\nType 'fr' or 'forward' to go to Berlin.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open book":
        if BERLIN == False:
            ZU_BOOK = True
            print("\nAs you open the book you are instantly drawn into it.")
            print("You are tumbling around like they do in those time travel movies.")
            print("After what feels like only a couple of seconds you are back at the Zürich Hauptbahnhof.")
            print("You don't remember how, but suddenly you speak fluent german.")
            print("You feel ready to leave Zürich and jump on the train to the next item on your bucketlist.")
            print("\nType 'fr' or 'forward' to go to Berlin.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k book":
        if BERLIN == False:
            print("\nYou kicked the book, but nothing happened.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick book":
        if BERLIN == False:
            print("\nYou kicked the book, but nothing happened.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m book":
        if BERLIN == False:
            print("\nYou try to move the book, but it's like it is stuck to the floor.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move book":
        if BERLIN == False:
            print("\nYou try to move the book, but it's like it is stuck to the floor.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    #berlin object options
    elif choice == "w berlin wall":
        if LONDON == False:
            print("\nThe wall is made out of bricks.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch berlin wall":
        if LONDON == False:
            print("\nThe wall is made out of bricks.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o berlin wall":
        if LONDON == False:
            print("\nYou can't open a wall, silly.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open berlin wall":
        if LONDON == False:
            print("\nYou can't open a wall, silly.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k berlin wall":
        if LONDON == False:
            BE_WALL = True
            print("\nYou kicked the Berlin wall so hard that you made it end up in a pile of dust and stone.")
            print("You hear sirens around you, as someone has called the police.")
            print("You think to yourself that you haven't got any time to end up in jail.")
            print("You have to complete your bucketlist first. So you decide to flee the country.")
            print("\nType 'fr' or 'forward' to flee to London.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick berlin wall":
        if LONDON == False:
            BE_WALL = True
            print("\nYou kicked the Berlin wall so hard that you made it end up in a pile of dust and stone.")
            print("You hear sirens around you, as someone has called the police.")
            print("You think to yourself that you haven't got any time to end up in jail.")
            print("You have to complete your bucketlist first. So you decide to flee the country.")
            print("\nType 'fr' or 'forward' to flee to London.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m berlin wall":
        if LONDON == False:
            BE_WALL = True
            print("\nYou try to move the Berlin wall so hard that you made it end up in a pile of dust and stone.")
            print("You hear sirens around you, as someone has called the police.")
            print("You think to yourself that you haven't got any time to end up in jail.")
            print("You have to complete your bucketlist first. So you decide to flee the country.")
            print("\nType 'fr' or 'forward' to flee to London.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move berlin wall":
        if LONDON == False:
            BE_WALL = True
            print("\nYou try to move the Berlin wall so hard that you made it end up in a pile of dust and stone.")
            print("You hear sirens around you, as someone has called the police.")
            print("You think to yourself that you haven't got any time to end up in jail.")
            print("You have to complete your bucketlist first. So you decide to flee the country.")
            print("\nType 'fr' or 'forward' to flee to London.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    #london object options
    elif choice == "w shipping container":
        if THAILAND == False:
            print("\nThe shipping container looks like a shipping container.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch shipping container":
        if THAILAND == False:
            print("\nThe shipping container looks like a shipping container.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o shipping container":
        if THAILAND == False:
            LO_CONTAINER = True
            print("\nYou open the shipping container and sees that it is fully furnished.")
            print("'This looks comfy' you think to yourself and enter.")
            print("You close the shipping container behind you just in time for the crane to \
            bring you on board the cargo ship.")
            print("\nType 'fr' or 'forward' to get ready and go to your last destination: Thailand!")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open shipping container":
        if THAILAND == False:
            LO_CONTAINER = True
            print("\nYou open the shipping container and sees that it is fully furnished.")
            print("'This looks comfy' you think to yourself and enter.")
            print("You close the shipping container behind you just in time for the crane to\
            bring you on board the cargo ship.")
            print("\nType 'fr' or 'forward' to get ready and go to your last destination: Thailand!")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k shipping container":
        if THAILAND == False:
            print("\nThe shipping container makes a metal noise, but nothing more happens.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick shipping container":
        if THAILAND == False:
            print("\nThe shipping container makes a metal noise, but nothing more happens.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m shipping container":
        if THAILAND == False:
            print("\nOnly the crane can move the shipping container, silly.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move shipping container":
        if THAILAND == False:
            print("\nOnly the crane can move the shipping container, silly.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()


    #thailand object options
    elif choice == "w beach bungalow":
        if ENDGAME == False:
            print("\nThe beach bungalow is one of a few bungalows on the beach.")
            print("It's made out of bamboo and has a roof made out of dried grass.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "watch beach bungalow":
        if ENDGAME == False:
            print("\nThe beach bungalow is one of a few bungalows on the beach.")
            print("It's made out of bamboo and has a roof made out of dried grass.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "o beach bungalow":
        if ENDGAME == False:
            BUNGALOW_DOOR = True
            print("\nYou open the door to your beach bungalow and run in to lay on the bed.")
            print("'I'm so comfortable here' you think to yourself. 'I never want to leave'.")
            print("And you won't have to.")
            input("\nPress enter to continue...")
            ENDGAME = True
            congrats()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "open beach bungalow":
        if ENDGAME == False:
            BUNGALOW_DOOR = True
            print("\nYou open the door to your beach bungalow and run in to lay on the bed.")
            print("'I'm so comfortable here' you think to yourself. 'I never want to leave'.")
            print("And you won't have to.")
            input("\nPress enter to continue...")
            ENDGAME = True
            congrats()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "k beach bungalow":
        if ENDGAME == False:
            print("\nThe beach bungalow doesn't get a scratch.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "kick beach bungalow":
        if ENDGAME == False:
            print("\nThe beach bungalow doesn't get a scratch.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "m beach bungalow":
        if ENDGAME == False:
            print("\nThe beach bungalow is to heavy for you to move.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()

    elif choice == "move beach bungalow":
        if ENDGAME == False:
            print("\nThe beach bungalow is to heavy for you to move.")
            gameChoice()
        else:
            print("Can't do that.")
            gameChoice()



    #gameplay options
    elif "i" in choice:
        if PARIS == False:
            print(AIRPORT_INFO)
            gameChoice()
        elif ROME == False:
            print(PARIS_INFO)
            gameChoice()
        elif ZURICH == False:
            print(ROME_INFO)
            gameChoice()
        elif BERLIN == False:
            print(ZURICH_INFO)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_INFO)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_INFO)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_INFO)
            gameChoice()

    elif "info" in choice:
        if PARIS == False:
            print(AIRPORT_INFO)
            gameChoice()
        elif ROME == False:
            print(PARIS_INFO)
            gameChoice()
        elif ZURICH == False:
            print(ROME_INFO)
            gameChoice()
        elif BERLIN == False:
            print(ZURICH_INFO)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_INFO)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_INFO)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_INFO)
            gameChoice()

    elif "h" in choice:
        print(COMMANDS)
        gameChoice()

    elif "help" in choice:
        print(COMMANDS)
        gameChoice()

    elif "fr" in choice:
        if BUNGALOW_DOOR == True:
            ENDGAME = True
            congrats()
        elif LO_CONTAINER == True:
            THAILAND = True
            thailand()
        elif BE_WALL == True:
            LONDON = True
            london()
        elif ZU_BOOK == True:
            BERLIN = True
            berlin()
        elif OPEN_CHEST == True:
            ZURICH = True
            zurich()
        elif KICKED_GANGLEADER == True:
            ROME = True
            rome()
        elif "water bottle\n" not in showInv3:
            PARIS = True
            paris()
        else:
            print("\nYou can't go to your next destination yet.")
            gameChoice()


    elif "forward" in choice:
        if BUNGALOW_DOOR == True:
            ENDGAME = True
            congrats()
        elif LO_CONTAINER == True:
            THAILAND = True
            thailand()
        elif BE_WALL == True:
            LONDON = True
            london()
        elif ZU_BOOK == True:
            BERLIN = True
            berlin()
        elif OPEN_CHEST == True:
            ZURICH = True
            zurich()
        elif KICKED_GANGLEADER == True:
            ROME = True
            rome()
        elif "water bottle\n" not in showInv3:
            PARIS = True
            paris()
        else:
            print("\nYou can't go to your next destination yet.")
            gameChoice()

    elif "ba" in choice:
        if BUNGALOW_DOOR == True:
            ENDGAME = True
            print("\nYou're back in Thailand.")
            thailand()

        elif LO_CONTAINER == True:
            THAILAND = True
            print("\nYou're back in London.")
            london()

        elif BE_WALL == True:
            LONDON = True
            print("\nYou're back in Berlin.")
            berlin()

        elif ZU_BOOK == True:
            BERLIN = True
            print("\nYou're back in Zürich.")
            zurich()

        elif OPEN_CHEST == True:
            ZURICH = True
            print("\nYou're back in Rome.")
            rome()

        elif KICKED_GANGLEADER == True:
            ROME = True
            print("\nYou're back in Paris.")
            paris()

        elif "water bottle\n" not in showInv3:
            PARIS = True
            print("\nYou're back at the airport.")
            airport()

        elif PARIS == False:
            print("\nYou're already in the first room. Try something else.")
            gameChoice()

    elif "backward" in choice:
        if BUNGALOW_DOOR == True:
            ENDGAME = True
            print("\nYou're back in Thailand.")
            thailand()

        elif LO_CONTAINER == True:
            THAILAND = True
            print("\nYou're back in London.")
            london()

        elif BE_WALL == True:
            LONDON = True
            print("\nYou're back in Berlin.")
            berlin()

        elif ZU_BOOK == True:
            BERLIN = True
            print("\nYou're back in Zürich.")
            zurich()

        elif OPEN_CHEST == True:
            ZURICH = True
            print("\nYou're back in Rome.")
            rome()

        elif KICKED_GANGLEADER == True:
            ROME = True
            print("\nYou're back in Paris.")
            paris()

        elif "water bottle\n" not in showInv3:
            PARIS = True
            print("\nYou're back at the airport.")
            airport()

        elif PARIS == False:
            print("\nYou're already in the first room. Try something else.")
            gameChoice()

    elif "look" in choice:
        if PARIS == False:
            print(AIRPORT_LOOK)
            gameChoice()
        elif ROME == False:
            print(PARIS_LOOK)
            gameChoice()
        elif ZURICH == False:
            print(ROME_LOOK)
            gameChoice()
        elif BERLIN == False:
            print(ZURICH_LOOK)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_LOOK)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_LOOK)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_LOOK)
            gameChoice()

    elif "l" in choice:
        if PARIS == False:
            print(AIRPORT_LEAD)
            gameChoice()
        elif ROME == False:
            print(PARIS_LEAD)
            gameChoice()
        elif ZURICH == False:
            print(ROME_LEAD)
            gameChoice()
        elif BERLIN == False:
            print(ZURICH_LEAD)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_LEAD)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_LEAD)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_LEAD)
            gameChoice()

    elif "lead" in choice:
        if PARIS == False:
            print(AIRPORT_LEAD)
            gameChoice()
        elif ROME == False:
            print(PARIS_LEAD)
            gameChoice()
        elif ZURICH == False:
            print(ROME_LEAD)
            gameChoice()
        elif BERLIN == False:
            print(ZURICH_LEAD)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_LEAD)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_LEAD)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_LEAD)
            gameChoice()

    elif "o" in choice:
        if PARIS == False:
            print(AIRPORT_OBJ)
            gameChoice()
        elif ROME == False:
            print(PARIS_OBJ)
            gameChoice()
        elif ZURICH == False:
            if CRACK_CONCRETE == True:
                print(ROME_NEWOBJ)
                gameChoice()
            else:
                print(ROME_OBJ)
                gameChoice()
        elif BERLIN == False:
            print(ZURICH_OBJ)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_OBJ)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_OBJ)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_OBJ)
            gameChoice()

    elif "object" in choice:
        if PARIS == False:
            print(AIRPORT_OBJ)
            gameChoice()
        elif ROME == False:
            print(PARIS_OBJ)
            gameChoice()
        elif ZURICH == False:
            if CRACK_CONCRETE == True:
                print(ROME_NEWOBJ)
                gameChoice()
            else:
                print(ROME_OBJ)
                gameChoice()
        elif BERLIN == False:
            print(ZURICH_OBJ)
            gameChoice()
        elif LONDON == False:
            print(BERLIN_OBJ)
            gameChoice()
        elif THAILAND == False:
            print(LONDON_OBJ)
            gameChoice()
        elif ENDGAME == False:
            print(THAI_OBJ)
            gameChoice()


    #if no option choosen
    else:
        print("\nThat is not a valid choice. You can only choose from the menu.")
        gameChoice()



def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:

        opts, _ = getopt.getopt(sys.argv[1:], "hivac", [
            "help",
            "info",
            "version",
            "about",
            "cheat"
        ])

        for opt, _ in opts:
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-i", "--info"):
                printInfo()

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("-a", "--about"):
                printAbout()

            elif opt in ("-c", "--cheat"):
                printCheat()

            else:
                assert False, "Unhandled option"

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)



def main():
    """
    Main function to carry out the work.
    """
    #startTime = datetime.now()

    parseOptions()

    startGame()

    #gameChoice()

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
