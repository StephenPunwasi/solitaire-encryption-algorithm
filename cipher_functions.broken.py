# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

#Assignment Outline Below
def clean_message(message):
    """(str) -> str
    
    #Return a copy of the message that includes only its alphabetical 
    characters, where each of those characters has been converted to 
    uppercase.
    
    >>>clean_message('Testing, 1,2,3. Testing')
    'TESTINGTESTING'
    >>>clean_message('Doe2s Th3is Th1ing W2ork?')
    'DOESTHISTHINGWORK'
    """
    
    cleaned_message = ""
    for ch in message: #TODO: what if message is not a string?
        if ch.isalpha() == True:
            cleaned_message += ch.upper()
    return cleaned_message

def encrypt_letter(letter, keystream):
    """(str, int) -> str
    
    #Apply the keystream value to the character to encrypt the character, and 
    return the result.
    
    #double check examples
    >>>encrypt_letter('H', 13)
    'U'
    >>>encrypt_letter('B', 20)
    'V'
    """
    
    letter_number = ord(letter) - ord('A') #
    keystream_letter = letter_number + keystream #
    encrypted_letter_num = keystream_letter % 26
    encrypted_letter = chr(encrypted_letter_num + ord('A'))
    return encrypted_letter
    
def decrypt_letter(letter, keystream):
    """(str, int) -> str   
    
    #Apply the keystream value to the character to decrypt the character, and 
    return the result.
    
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
    
    #Swap the card at the index with the card that follows it. Treat the deck 
    as circular: if the card at the index is on the bottom of the deck, swap 
    that card with the top card.

    (Note that in this and all functions that do something to the deck, the 
    function doesn't return anything. The deck is to be mutated.)
    
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
    
    #This is step 1 of the algorithm. Find JOKER1 and swap it with the card 
    that follows it. Treat the deck as circular.
    
    >>>card_deck = [1,2,3,4,5,JOKER1,6,7,8]
    >>>move_joker_1(card_deck)
    >>>card_deck
    [1,2,3,4,5,6,JOKER1,7,8]
    
    >>>card_deck = [1,2,3,4,5,6,7,8,JOKER1]
    >>>move_joker_1(card_deck)
    >>>card_deck
    [JOKER1,2,3,4,5,6,7,8,1]
    """
    index = card_deck.index(JOKER1)
    swap_cards(card_deck, index)
    
def move_joker_2(card_deck):
    """(list of int) -> NoneType

    #This is step 2 of the algorithm. Find JOKER2 and move it two cards down. 
    Treat the deck as circular.
    
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
    [1, 2, 3, 4, 5, 6, JOKER2, 7, 8]
    """
    
    second_joker_index = card_deck.index(JOKER2)
    
    if JOKER2 == card_deck[-1]:
        card_deck.insert(1, JOKER2)
        card_deck.pop()
    elif JOKER2 == card_deck[-2]:
        card_deck.insert(0, JOKER2)
        card_deck.pop(-2)
    else:
        card_deck.insert(second_joker_index+2, JOKER2)
        card_deck.pop(second_joker_index)

def triple_cut(card_deck):
    """(list of int) -> NoneType
    #Precondition Jokers must be in list
    #This is step 3 of the algorithm. Find the two jokers and do a triple cut.
    
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
    #works but needs to be checked 
        
def insert_top_to_bottom(card_deck):
    """(list of int) -> NoneType
    
    #This is step 4 of the algorithm. Look at the bottom card of the deck; 
    move that many cards from the top of the deck to the bottom, inserting 
    them just above the bottom card. Special case: if the bottom card is 
    JOKER2, use JOKER1 as the number of cards.
    #Precondition: Both Jokers Must Be Present
    
    >>>card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    >>>insert_top_to_bottom(card_deck)
    >>>card_deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    
    >>>card_deck = [1,2,3,4,5,6,7,9,10,11,12,13,14,8]
    >>>insert_top_to_bottom(card_deck)
    >>>card_deck
    [10,11,12,13,14,1,2,3,4,5,6,7,9,8]
    """
    #identify the card
    last_card = card_deck[-1]
    
    
    #make sure it's not the joker
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
    
    #This is step 5 of the algorithm. Look at the top card. Using that value 
    as an index, return the card in that deck at that index. Special case: if 
    the top card is JOKER2, use JOKER1 as the index.
    
    >>>card_deck = [1,2,3,4,5,6,7]
    >>>get_card_at_top_index(card_deck)
    2
    
    >>>card_deck = [3,4,5,6,7,8,9,1,2,3,4,5,6,7,10,]
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
    
    #This is the function that does all five steps of the algorithm. Return 
    the next potential keystream value.
    
    #Examples
    """
    
    move_joker_1(card_deck)
    move_joker_2(card_deck)
    triple_cut(card_deck)
    insert_top_to_bottom(card_deck)
    return get_card_at_top_index(card_deck)
    
    #Needs Super Amount of Testing
    
def get_next_keystream_value(card_deck):
    """(list of int) -> int
    
    #This is the function that repeats all five steps of the algorithm (call 
    get_next_value to get potential keystream values!) until a valid 
    keystream value (a number in the range 1-26) is produced.
    
    #Examples
    """

    keystream = get_next_value(card_deck)
    
    while keystream > 26:
        get_next_value(keystream)
    else:
        return keystream
    
def process_message(card_deck, message, encrypt_decrypt):
    """(list of int, str, str) -> str
    
    #Return the encrypted or decrypted message. Note that the message might 
    contain non-letters.
    
    #Examples
    """
    
    keystream = 0
    processed_message = ''
    message = clean_message(message)
    
    if 'e' == encrypt_decrypt:
        for ch in message:
            keystream = get_next_keystream_value(card_deck)
            processed_message += encrypt_letter(ch, keystream)
            print(keystream, ch, processed_message)
            
    #Maybe else or elif? 
    if 'd' == encrypt_decrypt:
        for ch in message:
            keystream = get_next_keystream_value(card_deck)
            processed_message += decrypt_letter(ch, keystream)
            print(keystream, ch, processed_message)
            
    
    return processed_message
    
def process_messages(card_deck, messages, encypt_decrypt):
    """(list of int, list of str, str) -> list of str
    
    #Return the list of encrypted or decrypted messages.
    
    #Examples
    """
    
    
    #return list of str
def read_messages(message_file):
    """(file open for reading) -> list of str
    
    #Read and return the contents of the file as a list of messages. Strip 
    the newline from each line.
    
    #Examples
    """
    file = open(message_file, 'r')
    messages = file.read().splitlines()
    message_list = []
    for line in messages:
        message_list += (line.split(' '))
    return message_list
    file.close()    #return list of str
    
def read_deck(deck):
    """(file open for reading) -> list of int
    
    #Read and return the contents of the file. Do not hard-code the number 28 
    anywhere; just read all of the integers from the deck file.
    
    #Examples
    """
    
    file = open(deck, 'r')
    deck = file.read().splitlines()
    card_deck = []
    for line in deck:
        card_deck += (line.split(' '))
    card_deck.pop()
    card_deck = [int(x) for x in card_deck]
    return card_deck
    file.close()