from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   servername = 'localhost'
   serverPort = 1025

   # Create socket called clientSocket and establish a TCP connection with mailserver and port

   # Fill in start
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((servername, serverPort))
   # Fill in end

   recv = clientSocket.recv(1024).decode()
   print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print (recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   mailFrom = "MAIL FROM: <mailid@gml.com>\r\n"
   clientSocket.send(mailFrom.encode())
   recv1 = clientSocket.recv(1024)
   print (recv1)
    # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   rcptTo = "RCPT TO: <madhat@wonderlan.com>\r\n"
   clientSocket.send(rcptTo.encode())
   recv1 = clientSocket.recv(1024)
   print(recv1)
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   recv1 = clientSocket.recv(1024)
   print (recv1)
   # Fill in end

   # Send message data.
   # Fill in start
   clientSocket.send(msg.encode())
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   clientSocket.send(endmsg.encode())
   recv1 = clientSocket.recv(1024)
   print (recv1)
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   clientSocket.send("QUIT\r\n".encode())
   message = clientSocket.recv(1024)
   print(message)
   clientSocket.close()
# Fill in end

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
