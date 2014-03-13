Public Names - Python
=============
An implementation of the Public Names protocol in Python.

Synopsis
---
Import the Public Names module

```
import publicnames as pns
```

Outline valid Public Names into list(s) of text string(s) 

```
pns.outline(u"5:Names,6:Public,") == [u"Names", u"Public"]
```

Or return `None` if the text parsed is not well-formed.

Validate text as a Public Names and return its text

```
pns.uniform(u"5:Names,6:Public,") == u"5:Names,6:Public,"
```

Or return `None` if the text parsed is not well-formed.

Articulate text as Public Names

```
import pns.lang.ASCII as ascii
publicNames = pns.articulate(ascii, u"Public Names - Python")
```

Index Public Names in a simple dictionary of unicode keys and values

```
store = {}
pns.index(store, publicNames.valid)
```

Walk the graph once from an articulation, returns a list of related names
sorted by descendent order of their count of relations with the search terms
first and the names' length.

```
pns.walk(store, (u"Names", u"Python")) == [[u"5:Names,6:Public,"], [u"Public"]]
```

Articulate and index statements about topics:

```
import pns.lang.EN as lang
context = pns.articulate(lang, u"Public Names - Python")
text = u"An implementation of the Public Names protocol in Python."
for (subject, object in pns.articulateTexts(lang, text)) {
    about(subject, EN, object, context)
}
```

Search topics about names

```
publicNames.search(store)
```

Parse and encode Netstrings
---
Encode strings as text

```
pns.netunicodes([u"Names", u"Public"])
```

Iterate through the netunicoded strings

```
list(pns.netunidecodes(u"5:Names,6:Public,")) == [u"Names", "Public"]
```

Parse netunicoded strings from text into a list:

```
pns.parse(u"5:Names,6:Public,")
```

Or return `None` if the text parsed is not well-formed:

```
pns.parse(u"")
pns.parse(u"5:Names,6:Public")
pns.parse(u"5:Names,6:Publ")
pns.parse(u"1:5:Names,6:Publ")
pns.parse(u"lorem ipsum et caetera ...")
```

Outline and validate Public Names
---
Validate text as Public Names and return a new instance of the PublicNames class

```
publicNames = pns.validate(u"5:Names,6:Public,")
```

PublicNames instances hold a set of the articulated texts  

```
publicNames.field == set(u"Names", u"Public")
```

With an outline of the articulation

```
publicNames.outline == [u"Name", u"Public"]
```

A copy of the original encoded text

```
publicNames.encoded == u"5:Names,6:Public,"
```

A copy of the validated encoding

```
publicNames.valid == u"5:Names,6:Public,"
```

And methods to test the Public Names validity and the size of its field

```
publicNames.isValid() == True
publicNames.horizon() == 2

