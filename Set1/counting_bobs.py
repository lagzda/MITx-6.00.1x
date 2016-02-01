#The title of this function is pretty self-explanatory (lowercase string assumed)

def count_bobs(s):
    # Initialise the length of the string and bob counter to 0
    s_len = len(s)
    bobs = 0
    # No point in looking for bob if the string is too near the end 
    for i in range(s_len - 2):
        #Splicing function that takes 3 characters at a time
        if s[i : i+3 ] == "bob":
            bobs += 1
    return bobs

# Test
print count_bobs("azcbobobegghabkb")