#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from publicnames import netunicodes, pnsValidate, PublicNames

def pnsArticulator (words):
    return re.compile(u'(?:^|\\s+)((?:' + u')|(?:'.join(words)  + u'))(?:$|\\s+)')

def pnsArticulate (text, articulators, depth, horizon, chunks=None, chunk=0):
    bottom = articulators.length
    while (true):
        texts = text.split(articulators[depth])
        depth =+ 1
        if (texts.length > 1):
            articulated = []
            for t in texts:
                if (len(t) > 0):
                    articulated.push(t)
            L=len(articulated);
            if (L > 1):
                break

            elif (L == 1):
                text = articulated[0]
        elif (texts.length == 1 and texts[0].length > 0):
            text = texts[0]
        if (depth == bottom):
            return [text]

    if (depth < bottom):
        field = set()
        if (chunk > 0):
            for text in articulated:
                if (len(text) > chunk):
                    pnsArticulate(text, articulators, depth, horizon, chunks, chunk);
                else:
                    n = pnsArticulate(text, articulators, depth, horizon) 
                    sat = pnsValidate (n, field(), horizon)
                    if (sat != None):
                        chunks.push([sat, text])
            return chunks

        names = []
        for text in articulated:
            n = pnsArticulate (text, articulators, depth, horizon);
            sat = pnsValidate (n, field, horizon);
            if (sat != None):
                names.push (sat)
        return names

    return articulated


class Articulator:

    def __init__ (self, tokenizers, chunk=132, horizon=PublicNames.HORIZON):
        self.tokenizers = tokenizers
        self.chunk = chunk
        self.horizon = horizon

    def articulate (self, text):
        names = pnsArticulate(text, self.tokenizers, 0, self.horizon)
        if (names.length > 1):
            names.sort()
            return netunicodes(names)

        return names[0]

    def articulateNames (self, text):
        return pnsArticulate(text, self.tokenizers, 0, self.horizon);

    def articulateTexts (self, texts):
        return pnsArticulate(texts, self.tokenizers, 0, self.horizon, [], self.chunk)

Articulator.ascii = Articulator([
    re.compile(u"\s*[?!.](?:\s+|$)"), # point, split sentences
    re.compile(u"\s*[:;](?:\s+|$)"), # split head from sequence
    re.compile(u"\s*,(?:\s+|$)"), # split the sentence articulations
    re.compile(u"(?:(?:^|\s+)[({\[]+\s*)|(?:\s*[})\]]+(?:$|\s+))"), # parentheses
    re.compile(u"\s+[-]+\s+"), # disgression
    re.compile(u'["]'), # citation
    re.compile(u"((?:(?:[A-Z]+[\S]*)(?:$|\s*))+)"), # private names
    re.compile(u"\s+"), # white spaces
    re.compile(u"['\\\/*+\-#]") # common hyphens
    ])
