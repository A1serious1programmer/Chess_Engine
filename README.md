
-- NOTE --
DEMO -

https://github.com/ojas-sharma-01/Chess_Engine/assets/114296963/edd49a35-e817-4b0e-a2f2-45e87705fc28


Trial.py is under devolopment . it features against ai gameplay.

chess2.py is the main file (client script).
chess-server.py is the server script.
Move_Validation.py is the file which generates the valid moves for the respective pieces. it has 6 functions to generate the valid moves for 6 respective pieces( rook, bishop, knight, king, pawn, queen).
Marker.py is a file which initialises the marker turtles.

-> online mode - you can play on same machine by running the server script on the one machine and connecting two clients on different machines
                 but same network connection so that the share same ip.

                 if you wish to play on different networks then the server script must run on some hosting platform(microsft azure, google cloud).


HOW TO ENTER IP

-> if playing locally -  then enter ip of one machine in server script and same ip in client scripts of two clients

-> if playing on different networks bind the ip of server script to an empty string ("") and in the client script enter the ip of server machine.

PORT NUMBER SHOULD BE SAME.
RECOMMENDED - CHOOSE PORT above 4000
