def sending_messages(send_messages, sent_messages):
    while send_messages:
        current_message = send_messages.pop()
        print(f"Print message: {current_message}")
        sent_messages.append(current_message)
def show_sent_messages(sent_messages):
    print("\nThe following messages have been printed:")
    for sent_messages in sent_messages:
        print(sent_messages)
send_messages = ['Louis', 'Kevin', 'Darryll']
sent_messages = []
sending_messages(send_messages, sent_messages)
show_sent_messages(sent_messages)
