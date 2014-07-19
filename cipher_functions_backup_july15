# Functions for running an encryption or decryption.
#test
# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

decryption_letter = ord('A')

#Assignment Outline Below
def clean_message(message):
    """(str) -> str
    
    Return a copy of the message that includes only its alphabetical 
    characters, where each of those characters has been converted to 
    uppercase.
    
    >>>clean_message('Testing, 1,2,3. Testing')
    'TESTINGTESTING'
    >>>clean_message('Doe2s Th3is Th1ing W2ork?')
    'DOESTHISTHINGWORK'
    """
    
    cleaned_message = ''
    for ch in message:
        if ch.isalpha() == True:
            cleaned_message += ch.upper()
    return cleaned_message
<<<<<<< HEAD
    #recheck
=======
    #passed check
    
    
    
>>>>>>> FETCH_HEAD
def encrypt_letter(letter, keystream):
    """(str, int) -> str
    
    #Apply the keystream value to the character to encrypt the character, and 
    return the result.
    
    >>>encrypt_letter('H', 13)
    91
    >>>encrypt_letter('B', 20)
    40
    """
    
    letter_number = ord(letter) - decryption_letter
    encrypted_letter = letter_number * keystream
    
    return encrypted_letter
    
    
    
def decrypt_letter(letter, keystream):
    """(str, int) -> str   
    
    #Apply the keystream value to the character to decrypt the character, and 
    return the result.
    
    >>>decrypt_letter('A', 5)
    78
    >>>decrypt_letter('Q', 9)
    74
    """
    
    letter_number = ord(letter) // keystream 
    
    decrypted_letter = letter_number + decryption_letter
    
    return decrypted_letter
    #needs to be re-checked 
    
    
    
def swap_cards(sample_deck, card_index):
    """(list of int, int) -> NoneType
    
    #Swap the card at the index with the card that follows it. Treat the deck 
    as circular: if the card at the index is on the bottom of the deck, swap 
    that card with the top card.

    (Note that in this and all functions that do something to the deck, the 
    function doesn't return anything. The deck is to be mutated.)
    
    #Examples
    """
<<<<<<< HEAD
    #Needs to be checked
    
    last_card = card_deck[-1]
    card_to_swap = card_deck[card_index + 1]
    face_card = card_deck[card_index]
    
    #check if card is at bottom of the deck
    if face_card == card_deck[-1]:
        card_deck.remove(last_card)
        card_deck.insert(0, last_card)
    else:
    #swap the card at index with the next card
        card_deck.remove(card_to_swap)
        card_deck.insert(card_index, card_to_swap)


#Double check that arguements for Algo are required

def move_joker_1(card_deck):
=======
    
    i = 0
    i_last = 27
    
    for i in range(len(sample_deck) - 1):
        if (0 <= i <= 26 and sample_deck[i] == JOKER1):
            sample_deck[i] = sample_deck[i + 1]
            sample_deck[i + 1] = JOKER1 #something is wrong with this line
        elif (sample_deck[i_last] == JOKER1):
            sample_deck[i_last] = sample_deck[i]
            sample_deck[i] = JOKER1
        
        
        
def move_joker_1(sample_deck):
>>>>>>> FETCH_HEAD
    """(list of int) -> NoneType
    
    Find JOKER1 and swap it with the following card in sample_deck.
    
    >>>move_joker_1(('1 3 5 27 4 3')
    
    >>>
    """
<<<<<<< HEAD
    joker1_index = card_deck.index(JOKER1)
    if JOKER1 == card_deck[-1]:
        card_deck.remove(JOKER1)
        card_deck.insert(0, JOKER1)
    else:
        card_deck.remove(JOKER1)
        card_deck.insert(joker1_index + 1, JOKER1)
    #works
    
def move_joker_2(card_deck):
=======
    
    swap_cards(sample_deck, JOKER1)
    
    
    
def move_joker_2(sample_deck):
>>>>>>> FETCH_HEAD
    """(list of int) -> NoneType

    #This is step 2 of the algorithm. Find JOKER2 and move it two cards down. 
    Treat the deck as circular.
    
    #Examples
    """
<<<<<<< HEAD
    second_joker_index = card_deck.index(JOKER2)
    if JOKER2 == card_deck[-1]:
        card_deck.remove(JOKER2)
        card_deck.insert(1, JOKER2)
    elif JOKER2 == card_deck[-2]:
        card_deck.remove(JOKER2)
        card_deck.insert(0, JOKER2)    
    else:
        card_deck.remove(JOKER2)
        card_deck.insert(second_joker_index + 2, JOKER2)
    
    #works
=======
    
    i = 0


    
>>>>>>> FETCH_HEAD

def triple_cut(card_deck):
    """(list of int) -> NoneType
    #Precondition Jokers must be in list
    #This is step 3 of the algorithm. Find the two jokers and do a triple cut.
    
    #Examples
    """
    
    joker1_index = card_deck.index(JOKER1)
    joker2_index = card_deck.index(JOKER2)

    #find the first instance of a joker, either JOKER1 or JOKER2
    if joker1_index < joker2_index:
        card_deck =  card_deck[joker2_index+1:] + card_deck[joker1_index:joker2_index] + card_deck[:joker1_index]
    else:
        card_deck =  card_deck[joker1_index+1:] + card_deck[joker2_index:joker1_index] + card_deck[:joker2_index]
   
    
def insert_top_to_bottom(card_deck):
    """(list of int) -> NoneType
    
    #This is step 4 of the algorithm. Look at the bottom card of the deck; 
    move that many cards from the top of the deck to the bottom, inserting 
    them just above the bottom card. Special case: if the bottom card is 
    JOKER2, use JOKER1 as the number of cards.
    #Precondition: Both Jokers Must Be Present
    #Examples
    """
    #make sure it's not 
    last_card = card_deck[-1]
    
    if last_card != JOKER2:
        card_deck = card_deck[-last_card:] + card_deck[:-last_card]
    else:
        card_deck = card_deck[-JOKER1:] + card_deck[:-JOKER1]
    
        
    
def get_card_at_top_index(card_deck):
    """(list of int) -> int
    
    #This is step 5 of the algorithm. Look at the top card. Using that value 
    as an index, return the card in that deck at that index. Special case: if 
    the top card is JOKER2, use JOKER1 as the index.
    
    #Examples
    """

    top_card = card_deck[0]
    
    if top_card != JOKER2:
        return card_deck[top_card]
    else:
        return card_deck[JOKER1]
    #Needs Testing 
    
def get_next_value(card_deck):
    """(list of int) -> int
    
    #This is the function that does all five steps of the algorithm. Return 
    the next potential keystream value.
    
    #Examples
    """
    
    #Step 1 Move First Joker
    move_first_joker =  move_joker_1(card_deck)
    #Step 2
    #move_joker_2()
    move_second_joker = move_joker_2(move_first_joker)
    #Step 3 Triple Cut Deck
    triple_cut = triple_cut(move_second_joker)
    #Step 4 Move the top card to the bottom
    top_to_bottom = insert_top_to_bottom(triple_cut)
    #Step 5 
    potential_keystream = get_card_at_top_index(top_to_bottom)
    return potential_keystream
    
def get_next_keystream_value(card_deck):
    """(list of int) -> int
    
    #This is the function that repeats all five steps of the algorithm (call 
    get_next_value to get potential keystream values!) until a valid 
    keystream value (a number in the range 1-26) is produced.
    
    #Examples
    """
    #Make sure it's only in range 1-26
    next_keystream = get_next_value(card_deck)
    return next_keystream 
    
def process_message():
    """(list of int, str, str) -> str
    
    #Return the encrypted or decrypted message. Note that the message might 
    contain non-letters.
    
    #Examples
    """
    
    
def process_messages():
    """(list of int, list of str, str) -> list of str
    
    #Return the list of encrypted or decrypted messages.
    
    #Examples
    """
    
def read_messages():
    """(file open for reading) -> list of str
    
    #Read and return the contents of the file as a list of messages. Strip 
    the newline from each line.
    
    #Examples
    """
    
def read_deck():
    """(file open for reading) -> list of int
    
    #Read and return the contents of the file. Do not hard-code the number 28 
    anywhere; just read all of the integers from the deck file.
    
    #Examples
    """
    
    
