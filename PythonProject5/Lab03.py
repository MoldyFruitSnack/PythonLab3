import lab_chat as lc



def get_user_input(message,to_upper=True):
 if to_upper:
  response = input(message).strip().upper()
 else:
  response = input(message).strip()
 return response

def get_username():
 return get_user_input("Enter your username: ")

def get_group():
 return get_user_input("Enter your group name: ")


user = get_username()
print(user)
group = get_group()
print(group)


def get_message():
 return get_user_input("What's your message: ", False)

message = get_message()
print(message)

#combining functions to create the peer-to-peer chat

def initialize_chat():
 user = get_username()
 group = get_group()
 node = lc.get_peer_node(user)
 lc.join_group(node, group)
 channel = lc.get_channel(node, group)
 return channel


def start_chat():
 channel = initialize_chat()

 while True:
  try:
   msg = get_message()
   channel.send(msg.encode('utf_8'))
  except (KeyboardInterrupt, SystemExit):
   break
 channel.send("$$STOP".encode('utf_8'))
 print("FINISHED")


start_chat()



