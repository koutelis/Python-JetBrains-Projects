camel = """
Switching on camera from habitat with camels...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \\
     |     \    _.-'             \\
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Yey, our little camel is sunbathing!"""

lion = """
Switching on camera from habitat with lions...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is croaking!"""

deer = """
Switching on camera from habitat with deers...
   /|       |\\
`__\\\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \\
     ;;`-'   `---__________-----.-.
     ;;;                         \_\\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Our 'Bambi' looks hungry. Let's go to feed it!"""

goose = """
Switching on camera from habitat with lovely goose...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \\
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \\
 <_  `     (  <`<            \              `-._\\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
This bird stares intently at you... (Maybe it's time to change the channel?)"""

bat = """
Switching on camera from habitat with bats...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\\\  W  //           <
       /             /~---~\             \\
      /_            |       |            _\\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\\
                ~-. /  \_/  \ .-~
                   V         V
It looks like this bat is fine."""

rabbit = """
Switching on camera from habitat with rabbits...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \\
\//\/      .- \\
 Y        /    Y 
 l       I     !
 ]\      _\    /"\\
(" ~----( ~   Y.  )
It seems there will be more rabbits soon!"""


def zookeeper():
  animals = [camel, lion, deer, goose, bat, rabbit]
  visiting = True
  while visiting:
    print('Current Zoo habitats: ')
    print(' 1 - Camel')
    print(' 2 - Lion')
    print(' 3 - Deer')
    print(' 4 - Goose')
    print(' 5 - Bat')
    print(' 6 - Rabbit')
    print()
    user_input = input("Which habitat would you like to see? Insert number 1-6 or 'exit' to leave. ")
    if user_input == 'exit':
      visiting =  False
    else:
      try:
        habitat = int(user_input)
        if habitat not in range(1, 7):
          raise ValueError
        print(animals[habitat - 1])
      except (ValueError, IndexError):
        print('Invalid input...')
  print('Thank you for visiting us. Take care!')
