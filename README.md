Public Names - Python
=============

An implementation of the Public Names protocol in Python.

# Synopsis

Import the Public Names module

    import publicnames as pns

Parse netunicoded strings from text into a list:

    pns.parse("5:Names,6:Public,")

 Or return `None` if the text parsed is not well-formed:

    pns.parse("5:Names,6:Public")
    pns.parse("5:Names,6:Publ")
    pns.parse("1:5:Names,6:Publ")
    pns.parse("lorem ipsum et caetera ...")

Encode netunicoded strings as text

    pns.encode(["Names", "Public"])

Validate text as Public Names and return a convenient data structure for applications

    publicNames = pns.validate("5:Names,6:Public,")
    publicNames.horizon
    publicNames.field
    publicNames.outline
    publicNames.encoded
    publicNames.valid

Articulate text as Public Names

    import pns.lang.ASCII as ascii
    publicNames = pns.articulate(ascii, "Public Names - Python")
    

Index Public Names as a graph for a key value store with a Dict interface

    store = publicNames.index({})

Articulate and index statements about topics:

    import pns.lang.EN as lang
    context = pns.articulate(lang, "Public Names - Python")
    text = "An implementation of the Public Names protocol in Python."
    for (subject, object in pns.articulateTexts(lang, text)) {
        pns.about(subject, "EN", object, context)
    }