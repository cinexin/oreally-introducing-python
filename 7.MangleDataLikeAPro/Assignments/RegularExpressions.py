'''
7.7. Write the Ontario poem
'''
mammoth = """We have seen thee, queen of cheese,\n
Lying quietly at your ease,\n
Gently fanned by evening breeze,\n
Thy fair form no flies dare seize.\n
\n
All gaily dressed soon you'll go\n
To the great Provincial show,\n
To be admired by many a beau\n
In the city of Toronto.\n
\n
Cows numerous as a swarm of bees,\n
Or as the leaves upon the trees,\n
It did require to make thee please\n
And stand unrivalled, queen of cheese.\n
\n
May you not receive a scar as\n
We have heard that Mr. Harris\n
Intends to send you off as far as\n
The great world's show at Paris.\n
\n
Of the youth beware of these,\n
For some of them might rudely squeeze\n
And bite your cheek, then songs or glees\n
We could not sing, oh! queen of cheese.\n
\n
Were't thou suspended from a balloon,\n
You'd cast a shade even at noon,\n
Folks would think it was the moon\n
About to fall and crush them soon."""

'''
7.8. Import re module to use Python regular expressions
Use re.findall() to print all the words that begin with 'c'
'''
import re
starting_with_c = re.findall(r'[c]\w+',mammoth)
print(starting_with_c)

'''
7.9. Find all 4 letter words that begin with c
'''
four_letter_beggining_with_c = re.findall(r'[c]...',mammoth)
print(four_letter_beggining_with_c)
'''
7.10. Find all the words that end with r
'''
words_ending_with_r = re.findall(r'(\b\w+[r]\b)', mammoth)
print(words_ending_with_r)
'''
7.11. Find all words that contain exactly three vowels in a row
'''
words_3_vowels_in_a_row = re.findall(r'\b\w*[aeiou][aeiou][aeiou]\w*\b', mammoth)
print(words_3_vowels_in_a_row)
