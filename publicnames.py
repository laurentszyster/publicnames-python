#!/usr/bin/python
# -*- coding: utf-8 -*-

def netunicode (s, sb):
    sb.append(str(len(s)))
    sb.append(":")
    sb.append(s)
    sb.append(",")
    return sb

def netunicodes (list):
    sb = []
    for s in list:
        sb.append(str(len(s)))
        sb.append(":")
        sb.append(s)
        sb.append(",")
    return "".join(sb)

def netunidecodes (text, strip=True):
    size = len(text)
    prev = 0
    while (prev < size):
        pos = text.find(u":", prev)
        if (pos < 0):
            break

        try:
            L = int(text[prev:pos])
        except:
            L = 0
        if L > 0:
            next = pos + L + 1
            if (next >= size or text[next] != u","):
                break

            elif (strip or next-pos > 1):
                yield text[pos+1:next]

            prev = next + 1
        else:
            break

def parse(text):
    return list(netunidecodes(text))

def pnsOutline (names):
    valid = []
    for name in names:
        if not name:
            continue

        n = parse(name)
        if (len(n) == 0):
            valid.append(name)
        else:
            l = pnsOutline (n)
            if (l != None):
                valid.append(l)
    if (len(valid) > 1):
        return valid

    if (len(valid) > 0):
        return valid[0]

def outline(encoded):
    names = parse(encoded)
    if names:
        return pnsOutline(names)

def pnsValidate (names, field, horizon):
    valid = []
    for name in names:
        if (len(name) == 0 or name in field):
            continue

        n = parse (name)
        if (len(n) == 0):
            valid.append(name)
            field.add(name)
        else:
            s = pnsValidate (n, field, horizon)
            if (s != None):
                valid.append(s)
                field.add(s)
        if (len(field) > horizon):
            return None

    if (len(valid) > 1):
        valid.sort()
        return netunicodes(valid)

    if (len(valid) > 0):
        return valid[0]

def pnsValidateAndOutline (names, outline, field, horizon):
    valid = []
    for name in names:
        if (len(name) == 0 or name in field):
            continue

        n = parse(name)
        if (len(n) == 0):
            outline.append(name)
            valid.append(name)
            field.add(name)
        else:
            o = []
            s = pnsValidateAndOutline (n, o, field, horizon)
            if (s != None):
                if (o.len > 1):
                    outline.append(o)
                else:
                    outline.append(o[0])
                valid.append(s)
                field.add(s)
        if (len(field) > horizon):
            return None;

    if (len(valid) > 1):
        valid.sort()
        return netunicodes(valid)

    if (len(valid) > 0):
        return valid[0]

def index(encoded, store, field=(), horizon=30):
    names = parse(encoded)
    if names:
        for name in names:
            i = store.get(name)
            if i:
                i = pnsValidate((encoded, i), field, horizon)
                if i:
                    store[name] = i
            else:
                store[name] = encoded
                index(name, store)

def walk(encoded, store):
    graph = {}
    for name in netunidecodes(encoded):
        i = store[name]
        if i:
            for key in netunidecodes(i):
                graph.setdefault(key, set()).add(name)
    return graph

class PublicNames:
    HORIZON = 30
    def __init__(self, encoded, field=(), horizon=HORIZON):
        self.encoded = encoded
        self.field = set(field)
        self.outline = []
        self.valid = pnsValidateAndOutline(encoded, outline, field, horizon)
    def isValid(self):
        return self.encoded == self.valid
    def index(self, store, field=(), horizon=HORIZON):
        if self.isValid():
            return index(self.encoded, store, field, horizon)
    def walk(self, store, field=(), horizon=HORIZON):
        if self.isValid():
            return walk(self.encoded, store, field, horizon)

def validate(encoded):
    return PublicNames(encoded)

class PublicGraph:
    def __init__ (self, graph):
        self.graph = graph
