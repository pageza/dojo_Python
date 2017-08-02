# Coin Tosses
# Write a function that simulates tossing a coin 5,000 times.
# Your function should print how many times the head/tail appears.

import random

def toss_coin():
    result = random.randint(0,1)
    return result

def tosses(num):
    print "Starting to toss coins..."
    heads_count = 0
    tails_count = 0
    for i in range(1,num):
        print "Tossing now...."
        flip = toss_coin()
        if flip == 1 :
            heads_count += 1
            print "Attempt #"+str(i)+" results in heads! You have "+str(heads_count)+"head(s) and "+str(tails_count)+"tail(s) so far!"
        else :
            tails_count += 1
            print "Attempt #"+str(i)+" results in tails! You have "+str(heads_count)+"head(s) and "+str(tails_count)+"tail(s) so far!"

tosses(500)
