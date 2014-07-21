# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

def clean_message(message):
    """(str) -> str
    
    Strip the message of all non-alphabetical characters and return as a
    capitalized string.
    
    >>>clean_message('Testing, 1,2,3. Testing')
    'TESTINGTESTING'
    >>>clean_message('Doe2s Th3is Th1ing W2ork?')
    'DOESTHISTHINGWORK'
    """
    
    cleaned_message = ""
    for ch in message: 
        if ch.isalpha() == True:
            cleaned_message += ch.upper()
    return cleaned_message

def encrypt_letter(letter, keystream):
    """(str, int) -> str
    
    Precondition: len(letter) == 1 
    
    Return encrypted version of letter based on keystream value.
            
    >>>encrypt_letter('H', 13)
    'U'
    >>>encrypt_letter('B', 20)
    'V'
    """

    letter_number = ord(letter) - ord('A')
    keystream_letter = letter_number + keystream
    encrypted_letter_num = keystream_letter % 26
    encrypted_letter = chr(encrypted_letter_num + ord('A'))
    return encrypted_letter
    
def decrypt_letter(letter, keystream):
    """(str, int) -> str   

    Precondition: len(letter) == 1 

    Return decrypted version of letter based on keystream value.
    
    >>>decrypt_letter('U', 13)
    'H'
    >>>decrypt_letter('V', 20)
    'B'
    """
    
    encrypted_letter = (ord(letter) - ord('A')) - keystream
    if encrypted_letter < 0:
        encrypted_letter += (26 + ord('A'))
    else:
        encrypted_letter += ord('A')
    
    return chr(encrypted_letter)
    
def swap_cards(card_deck, card_index):
    """(list of int, int) -> NoneType
    
    Swap the card at the provided index with the following card. Treat the
    deck as circular, so if the card the last card swaps with the first.
    
    >>>card_deck = [2,3,4,5,6,7,8,9,10]
    >>>swap_cards(card_deck, 4)
    >>>card_deck
    [2, 3, 4, 5, 7, 6, 8, 9, 10]
    
    >>>card_deck = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    >>>swap_cards(card_deck, -1)
    >>>card_deck
    [16, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2]
    """
    
    card = card_deck[card_index]
    
    if card == card_deck[-1]:
        card_deck[-1] = card_deck[0]        
        card_deck[0] = card
    else:
        card_deck[card_index] = card_deck[card_index + 1]
        card_deck[card_index + 1] = card    


def move_joker_1(card_deck):
    """(list of int) -> NoneType
    
    Step 1 of the alogrithm. Finds JOKER1 and swaps it with the next card. 
    The deck is treated circular, so the last card gets swapped with the
    first.
    
    >>>card_deck = [1, 2, 3, 4, 5, JOKER1, 6, 7, 8]
    >>>move_joker_1(card_deck)
    >>>card_deck
    [1, 2, 3, 4, 5, 6, JOKER1, 7, 8]
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, 8, JOKER1]
    >>>move_joker_1(card_deck)
    >>>card_deck
    [JOKER1, 2, 3, 4, 5, 6, 7, 8, 1]
    """
    
    first_joker_index = card_deck.index(JOKER1)
    swap_cards(card_deck, first_joker_index)    

    
def move_joker_2(card_deck):
    """(list of int) -> NoneType

    Step 2 of the algorithm. Find and move JOKER2 two cards down. Treat
    treats the card deck as circular, making the card after the last the 
    first.
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, 8, JOKER2]
    >>>move_joker_2(card_deck)
    >>>card_deck
    [1, JOKER2, 2, 3, 4, 5, 6, 7, 8]
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, JOKER2, 8]
    >>>move_joker_2(card_deck)
    >>>card_deck
    [JOKER2, 1, 2, 3, 4, 5, 6, 7, 8]
    
    >>>card_deck = [1, 2, 3, 4, 5, JOKER2, 6, 7, 8]
    >>>move_joker_2(card_deck)
    >>>card_deck
    [1, 2, 3, 4, 5, 6, 7, JOKER2, 8]
    """
    
    second_joker_index = card_deck.index(JOKER2)
    swap_cards(card_deck, second_joker_index)     
    second_joker_index = card_deck.index(JOKER2)
    swap_cards(card_deck, second_joker_index)  

def triple_cut(card_deck):
    """(list of int) -> NoneType

    Precondition: Both JOKER1 and JOKER2 must be in the card deck.
    
    Step 3 of the algorithm. Find JOKER1 and JOKER2 in the card deck. Replace
    all cards after the second joker with all cards before the joker and 
    vice versa. 
    
    >>>card_deck = [1, 2, 3, 4, JOKER1, 5, 6, 7, 8, JOKER2, 9, 10, 11, 12]
    >>>triple_cut(card_deck)
    >>>card_deck
    [9, 10, 11, 12, JOKER1, 5, 6, 7, 8, JOKER2, 1, 2, 3, 4]
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, JOKER2, 8, 9, 10, JOKER1, 11, 12]
    >>>triple_cut(card_deck)
    >>>card_deck
    [11, 12, JOKER2, 8, 9, 10, JOKER1, 1, 2, 3, 4, 5, 6, 7]
    """
    
    joker1_index = card_deck.index(JOKER1)
    joker2_index = card_deck.index(JOKER2)    
    
    if joker1_index < joker2_index:
        beginning = card_deck[joker2_index+1:] 
        middle = card_deck[joker1_index:joker2_index+1] 
        end = card_deck[:joker1_index]
        del card_deck[:]    
        card_deck.extend(beginning + middle + end)
    else:
        beginning = card_deck[joker1_index+1:] 
        middle = card_deck[joker2_index:joker1_index+1] 
        end = card_deck[:joker2_index]
        del card_deck[:]
        card_deck.extend(beginning + middle + end)        
        
def insert_top_to_bottom(card_deck):
    """(list of int) -> NoneType
    
    Precondition: Both JOKER1 and JOKER2 must be in the card deck.
    
    Step 4 of the algorithm. Take the value of the last card in the deck, and
    move that number of cards from the top of the deck to the bottom, just 
    above the last card.
    
    If JOKER2 is the bottom card, use the value on JOKER1. 

    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    >>>insert_top_to_bottom(card_deck)
    >>>card_deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 8]
    >>>insert_top_to_bottom(card_deck)
    >>>card_deck
    [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 9, 8]
    """

    last_card = card_deck[-1]
    
    if last_card != JOKER2:
        card_deck[-1:] = card_deck[:last_card] 
        del card_deck[:last_card]
        card_deck.append(last_card)
    else:
        card_deck[-1:] = card_deck[:JOKER1] 
        del card_deck[:JOKER1]
        card_deck.append(last_card)    
    
def get_card_at_top_index(card_deck):
    """(list of int) -> int

    Step 5 of the algorithm. Use the value on the top card as an index.
    Return the value of the card at that index. 
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7]
    >>>get_card_at_top_index(card_deck)
    2
    
    >>>card_deck = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 10]
    >>>get_card_at_top_index(card_deck)
    6    
    """
    
    top_card = card_deck[0]
    if top_card == JOKER2:
        return card_deck[JOKER1]
    else:
        return card_deck[top_card]
    
def get_next_value(card_deck):
    """(list of int) -> int
    
    Return the next potential keystream by applying all five steps of the 
    algorithm. 
    
    >>> card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_value(card_deck)
    11
    >>> get_next_value(card_deck)
    9
    """
    
    move_joker_1(card_deck)
    move_joker_2(card_deck)
    triple_cut(card_deck)
    insert_top_to_bottom(card_deck)
    return get_card_at_top_index(card_deck)
        
def get_next_keystream_value(card_deck):
    """(list of int) -> int
    
    Repeat all five steps of algorithm using the provide card deck until a 
    valid keysteam is returned.
        
    >>> card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(card_deck)
    11
    >>> get_next_keystream_value(card_deck)
    9
    """
    
    keystream = get_next_value(card_deck)
    
    while keystream in [JOKER1,JOKER2]:
        keystream = get_next_value(card_deck)
        return keystream
    else:
        return keystream
    
def process_message(card_deck, message, encrypt_decrypt):
    """(list of int, str, str) -> str
    
    Precondition: encrypt_decrypt is either 'd' or 'e'. Must start with the 
    same deck used to encrypt to properly decrypt. 
    
    Uses the card deck provided to decode or encode the message. 
    """
    
    processed_message = ''
    message = clean_message(message)
    if 'e' == encrypt_decrypt:
        for ch in message:
            keystreams = get_next_keystream_value(card_deck)
            processed_message += encrypt_letter(ch, keystreams)
    elif 'd' == encrypt_decrypt:
        for ch in message:
            keystreams = get_next_keystream_value(card_deck)
            processed_message += decrypt_letter(ch, keystreams)            
    
    return processed_message
    
def process_messages(card_deck, messages, encrypt_decrypt):
    """(list of int, list of str, str) -> list of str
    
    Precondition: encrypt_decrypt is either 'd' or 'e'
    
    Return the list of encrypted or decrypted messages based on
    encrypt_decrypt for given card_deck.
    
    >>> card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,18,\
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> messages = ['apple', 'mac', 'ipad']
    >>> process_messages(card_deck, messages, 'e')
    ['LYMSO', 'LLN', 'PXJO']
    
    >>> card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> messages = ['WNJVX', 'ALYHVJ', 'APAAM']
    >>> process_messages(card_deck, messages, 'd')
    ['LEMON', 'BANANA', 'PEACH']
    """
    
    message_list = []
    for message in messages:
        processed = process_message(card_deck, message, encrypt_decrypt)
        message_list.append(processed)
    return message_list

def read_messages(message_file):
    """(file open for reading) -> list of str
    
    Read and return the contents of message_file as a list of messages.
    """
    
    message_list = []
    for line in message_file:
        line = line.strip()
        message_list.append(line)
    return message_list
    
def read_deck(deck):
    """(file open for reading) -> list of int
    
    Precondtion: Deck file must only contain numbers. 
    
    Read and return the contents of a deck file. 
    """
    
    card_deck = []
    for line in deck:
        line = (line.strip().split(' '))
        for num in line:
            card_deck.append(int(num))
    return card_deck
