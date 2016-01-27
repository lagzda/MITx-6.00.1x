def count_vowels(s):
    # Initialise the counter to zero
    vowels = 0
    for letter in s:
        #Increment vowel count by 1 each time a vowel appears
        if letter in "aeiou":
            vowels += 1
    # Return the count of vowels        
    return vowels

#Test
print count_vowels("aelkjkje")