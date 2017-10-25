import re

sampletext = "(that's okay). I want to .know #what''s going on?"
z = re.compile(r'[A-Z]', re.UNICODE).split(sampletext)  # remove caps
x = re.compile(r'\W+', re.UNICODE).split(sampletext)  # remove non-characters

if __name__ == '__main__':
    print(z)
    print(x)