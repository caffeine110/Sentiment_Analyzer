from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import re

tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))



def tweet_cleaner(text):
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    
    words = tok.tokenize(lower_case)

    return (" ".join(words)).strip()


t = '@iamjazzyfizzle I wish I got to watch it with' 
tt = '@LOLTrish hey  long time no see! Yes.. Rains a...'
ttt = "@nationwideclass no, https://gauravaghukar.com  it's not behaving at all.."


pt = tweet_cleaner(ttt)
print(pt)
