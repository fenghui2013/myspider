import random

USERAGENT_LIST = []

def init_useragent():
    print "========================init_useragent"
    global USERAGENT_LIST
    with open('./myspider/useragent', 'r') as f:
        for line in f:
            line = line.strip()
            USERAGENT_LIST.append(line)

def get_useragent():
    print "========================get_useragent"
    global USERAGENT_LIST
    return random.choice(USERAGENT_LIST)
