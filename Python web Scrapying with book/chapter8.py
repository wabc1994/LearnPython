#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm
import re
import string
from urllib import urlopen
import operator


def cleanText(input):
    input = re.sub("\n", " ", input)
    input = re.sub("\[[0-9]*\]", "", input)
    input = re.sub(" +", " ", input)
    input = re.sub("u\.s\.", "us", input)

    input = input.decode("ascii", "ignore")
    return input


def cleanIput(input):
    input = cleanText(input)
    cleanIput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item == "a" or item == "i"):
            cleanIput.append(item)
    return cleanIput


def getNgrams(input ,n):
    input = cleanIput(input)
    output = {}
    for i in range(len(input)-n+1):

        ngramTemp = " ".join(input[i:i+n])

        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


def inCommon(nagram):

    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with",
                   "on", "do", "say", "this", "they", "is", "an", "at", "but", "we", "his", "from", "that", "not", "by",
                   "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her", "all", "my",
                   "make", "about", "know", "will", "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see",
                   "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two",
                   "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use",
                   "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in nagram:
        if word in commonWords:
            return True
    return False


def getFirstSentenceContaining(nagram, content):

    sentences = content.split('.')
    for sentence in sentences:
        if nagram in sentence:
            return sentence
    return ""

if __name__ == "__main__":
    content = str(urlopen("http://pythonscraping.com/files/space.txt").read())
    ngrams = getNgrams(content, 2)
    sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedNGrams)
