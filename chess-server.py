import socket, threading
import random

def accept_client():
    global total_conn, max_conn
    while True:
        if total_conn <= max_conn:
            #accept
            cli_sock, cli_add = ser_sock.accept()
            CONNECTION_LIST.append(cli_sock)

            if len(CONNECTION_LIST) == 2:
                thread_client = threading.Thread(target = handle_game, args=[[CONNECTION_LIST[0], CONNECTION_LIST[1]]])
                thread_client.start()
                CONNECTION_LIST.clear()
            total_conn += 1
            
def handle_game(conn_list):
    global total_conn
    team = ["black", "white"][random.randint(0,1)]
    try:
        if team == "black":
            conn_list[0].send(("black turn").encode()), conn_list[1].send(("white turn").encode())
            start, end = conn_list[1], conn_list[0]
        elif team == "white":
            conn_list[0].send(("white turn").encode()), conn_list[1].send(("black turn").encode())
            start, end = conn_list[0], conn_list[1]
    except:
        for i in conn_list:
            try:
                i.send(("error : opponent left the match").encode())
                i.close()
            except Exception as x:
                pass
        total_conn -= 2
        return
    while True:
        try:
            data = start.recv(1024)
            if data:
                end.send(data)
                data = end.recv(1024)
                if data:
                    start.send(data)
                
        except Exception as x:
            print(x)
            for i in conn_list:
                try:
                    i.send(("error : opponent left the match").encode())
                    i.close()
                except Exception as x:
                    pass
            total_conn -= 2
            break
                
    
if __name__ == "__main__":
    max_conn = 10
    total_conn = 0
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = ''
    PORT = 3389
    ser_sock.bind((HOST, PORT))

    # listen
    ser_sock.listen(2)
    print('Chess server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()
