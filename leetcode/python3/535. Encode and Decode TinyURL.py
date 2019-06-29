'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/
'''
import random
import string
class Codec:
    alphabat = string.ascii_letters + '0123456789' # string.sacii_letters 26个字母的大小写
    def __init__(self):
        self.url2code = {}
        self.code2url ={}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabat) for _ in range(6))
            if code not in self.code2url: 
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl
        return 'http://tinyurl.com/' + self.url2code[longUrl]        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


'''
讨论区方法
It's possible that a randomly generated code has already been generated before. 
In that case, another random code is generated instead. Repeat until we have a code that's not already in use. 
How long can this take? Well, even if we get up to using half of the code space, which is a whopping 626/2 = 28,400,117,792 entries, 
then each code has a 50% chance of not having appeared yet. So the expected/average number of attempts is 2, 
and for example only one in a billion URLs takes more than 30 attempts. 
And if we ever get to an even larger number of entries and this does become a problem, then we can just use length 7. 
We'd need to anyway, as we'd be running out of available codes.
'''