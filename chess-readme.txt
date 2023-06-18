THANK YOU FOR TRYING OUT MY CHESS ENGINE!!


-> online mode - you can play on same machine by running the server script on the one machine and connecting two clients on different machines
                 but same network connection so that the share same ip.

                 if you wish to play on different networks then the server script must run on some hosting platform(microsft azure, google cloud).


HOW TO ENTER IP

-> if playing locally -  then enter ip of one machine in server script and same ip in client scripts of two clients

-> if playing on different networks bind the ip of server script to an empty string ("") and in the client script enter the ip of server machine.
		    

-- NOTE --
PORT NUMBER SHOULD BE SAME.
RECOMMENDED - CHOOSE PORT above 4000

THE CODE DOES NOT HAVE REALLY GOOD ERROR HANDLING IN THE NETWORKING PART AND YOU MAY RUN INTO SOME ISSUES. 