#!/usr/bin/env python
import sys
import random
 

def main():
    print 'This is a survey.\n',
    print 'Q1: Are you excited to take this class?\n>',
    ans=sys.stdin.readline()
    yes = "yes"
    no = "no"
    while(yes not in ans or no in ans):
        i = random.random()
        if i < 0.1 :
            print 'Are you sure?'
        elif i < 0.3 :
            print 'But it\'s really cool material!'
        elif i < 0.5 :
            print 'C\'mon, you\'ll have fun; the teachers are awesome!'
        elif i < 0.7 :
            print 'Really? You\'ll learn how to import antigravity!'
        elif i < 1 :
            print 'Listen, I\'m, not gonna take no for an answer!'
        print '>',
        ans = sys.stdin.readline()
    print 'YAY! We\'re so glad you\'re pumped for the class, it\'s gonna be a great quarter!!'



if __name__ == '__main__':
    main()
