"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message_file1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    
    open_deck = open(DECK_FILENAME, 'r')
    card_deck = cipher_functions.read_deck(open_deck)
    open_messages = open(MSG_FILENAME, 'r')    
    messages = cipher_functions.read_messages(open_messages)
    processed = cipher_functions.process_messages(card_deck, messages, MODE)
    print(processed)
    pass

main()
