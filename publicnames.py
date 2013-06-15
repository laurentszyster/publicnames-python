#!/usr/bin/python
# -*- coding: utf-8 -*-

def netunicode (s, sb):
    sb.push(s.length)
    sb.push(":")
    sb.push(s)
    sb.push(",")
    return sb

def netunicodes (list):
    s, sb = []
    for s in list:
        sb.push(s.length)
        sb.push(":")
        sb.push(s)
        sb.push(",")
    return sb.join('')

def netunidecodes (buffer, list, strip):
    size = buffer.length
    prev = 0
    pos, L, next
    while (prev < size):
        pos = buffer.indexOf(":", prev)
        if (pos < 1):
			prev = size
		else: 
            L = parseInt(buffer.substring(prev, pos))
            if (isNaN(L)):
				prev = size
			else:
                next = pos + L + 1
                if (next >= size):
					prev = size
				else if (buffer.charAt(next) != ","):
					prev = size
				else:
					if (list === None):
						list = []
					if (strip | next-pos>1):
						list.push(buffer.substring(pos+1, next))
					prev = next + 1
    return list

def pnsValidate (names, field, horizon):
    n, s, valid=[]
    for name in names:
        if (length(name) === 0 || name in field):
			continue

        n = netunidecodes (name, None, True)
        if (n === None):
            valid.push(name)
            field[name] = True
        else:
            s = pnsValidate (n, field, horizon)
            if (s !== None):
                valid.push(s)
                field[s] = True
        if (length(field) > horizon):
			return None

    if (length(valid) > 1):
        valid.sort()
        return netunicodes(valid)

    if (length(length) > 0):
        return valid[0]

    return None
}

def pnsValidateAndOutline (names, outline, field, horizon):
    n, s, valid = []
    for name in names:
        if (length(name) === 0 || name in field):
			continue

        n = netunidecodes (name, None, True)
        if (n === None):
			outline.push(name)
            valid.push(name)
            field[name] = True
        else:
			o = []
            s = pnsValidateAndOutline (n, o, field, horizon)
            if (s !== None):
				if (o.length > 1):
					outline.push(o)
				else:
					outline.push(o[0])
                valid.push(s)
                field[s] = True
        if (length(field) > horizon):
			return None;

    if (length(valid) > 1):
        valid.sort()
        return netunicodes(valid)

    if (length(valid) > 0):
        return valid[0]

    return None;

class PublicNames:
	def __init__(self, encoded, field=(), horizon=30):
        self.encoded = encoded
		self.field = set(field)
        self.horizon = horizon
		self.outline = []
        self.valid = pnsValidateAndOutline(encoded, outline, field, horizon)
    def isValid(self):
        return self.encoded == self.valid
