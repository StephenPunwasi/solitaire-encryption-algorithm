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
    
    #Return a copy of the message that includes only its alphabetical 
    characters, where each of those characters has been converted to 
    uppercase.
    
    >>>clean_message('Testing, 1,2,3. Testing')
    'TESTINGTESTING'
    >>>clean_message('Doe2s Th3is Th1ing W2ork?')
    'DOESTHISTHINGWORK'
    """
    
    cleaned_message = ""
    for ch in message:
        if ch.isalpha() == True:
            cleaned_message += ch.upper()
    #passed check
    
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
    
def swap_cards(card_deck, card_index):
    """(list of int, int) -> NoneType
    
    #Swap the card at the index with the card that follows it. Treat the deck 
    as circular: if the card at the index is on the bottom of the deck, swap 
    that card with the top card.

    (Note that in this and all functions that do something to the deck, the 
    function doesn't return anything. The deck is to be mutated.)
    
    #Examples
    """
    
    #check where in the index it is
    
    #if it's the last card, insert it back into card_deck as first index
    
    #else move it up 1 in the index
        
def move_joker_1():
    """(list of int) -> NoneType
    
    #This is step 1 of the algorithm. Find JOKER1 and swap it with the card 
    that follows it. Treat the deck as circular.
    
    #Examples
    """

def move_joker_2():
    """(list of int) -> NoneType

    #This is step 2 of the algorithm. Find JOKER2 and move it two cards down. 
    Treat the deck as circular.
    
    #Examples
    """

def triple_cut():
    """(list of int) -> NoneType
    
    #This is step 3 of the algorithm. Find the two jokers and do a triple cut.
    
    #Examples
    """

def insert_top_to_bottom():
    """(list of int) -> NoneType
    
    #This is step 4 of the algorithm. Look at the bottom card of the deck; 
    move that many cards from the top of the deck to the bottom, inserting 
    them just above the bottom card. Special case: if the bottom card is 
    JOKER2, use JOKER1 as the number of cards.
    
    #Examples
    """

def get_card_at_top_index():
    """(list of int) -> int
    
    #This is step 5 of the algorithm. Look at the top card. Using that value 
    as an index, return the card in that deck at that index. Special case: if 
    the top card is JOKER2, use JOKER1 as the index.
    
    #Examples
    """

def get_next_value():
    """(list of int) -> int
    
    #This is the function that does all five steps of the algorithm. Return 
    the next potential keystream value.
    
    #Examples
    """

def get_next_keystream_value():
    """(list of int) -> int
    
    #This is the function that repeats all five steps of the algorithm (call 
    get_next_value to get potential keystream values!) until a valid 
    keystream value (a number in the range 1-26) is produced.
    
    #Examples
    """
    
def process_message():
    """(list of int, str, str) -> str
    
    #Return the encrypted or decrypted message. Note that the message might 
    contain non-letters.
    
    #Examples
    """
def process_messages():
    """(list of int, list of str, str) -> str
    
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