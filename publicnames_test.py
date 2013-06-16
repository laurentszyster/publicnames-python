import publicnames as pns
import unittest

class TestPublicNames(unittest.TestCase):

    def test_netunicode(self):
        self.assertEqual(''.join(pns.netunicode(u"Public", [])), u"6:Public,")
        self.assertEqual(''.join(pns.netunicode(u"Names", [])), u"5:Names,")

    def test_netunicodes(self):
        self.assertEqual(pns.netunicodes([u"Public", u"Names"]), u"6:Public,5:Names,")
        self.assertEqual(
            pns.netunicodes([u"5:Names,6:Public,", u"The"]),
            u"17:5:Names,6:Public,,3:The,"
            )

    def test_netunidecodes(self):
        self.assertEqual(
            list(pns.netunidecodes(u"6:Public,5:Names,")), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            list(pns.netunidecodes(u"6:Public,5:Names,", False)), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            list(pns.netunidecodes(u"6:Public,5:Names,", True)), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            list(pns.netunidecodes(u"6:Public,5:Names,xxx", False)), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            list(pns.netunidecodes(u"6:Public,5:Names,xxx", True)), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            list(pns.netunidecodes(u"17:5:Names,6:Public,,3:The,")),
            [u"5:Names,6:Public,", u"The"]
            )

    def test_parse(self):
        self.assertEqual(
            pns.parse(u"6:Public,5:Names,"), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            pns.parse(u"6:Public,5:Names,xxx"), 
            [u"Public", u"Names"]
            )
        self.assertEqual(
            pns.parse(u"17:5:Names,6:Public,,3:The,"),
            [u"5:Names,6:Public,", u"The"]
            )

    def test_outline(self):
        self.assertEqual(
            pns.outline(u"5:Names,6:Public,"),
            [u"Names", u"Public"]
            )
        self.assertEqual(
            pns.outline(u"17:5:Names,6:Public,,3:The,"), 
            [[u"Names", u"Public"], u"The"]
            )

    def test_pnsValidate(self):
        self.assertEqual(
            pns.pnsValidate(pns.netunidecodes(u"5:Names,6:Public,"), set(), 2), 
            "5:Names,6:Public,"
            )
        field = set()
        self.assertEqual(
            pns.pnsValidate(pns.netunidecodes("5:Names,6:Public,"), field, 2),
            u"5:Names,6:Public,"
            )
        self.assertEqual(field, set((u"Names", u"Public")))
        self.assertEqual(
            pns.pnsValidate(pns.netunidecodes(u"5:Names,6:Public,3:The,"), set((u"The",)), 3), 
            u"5:Names,6:Public,"
            )
        self.assertEqual(
            pns.pnsValidate(pns.netunidecodes(u"5:Names,6:Public,3:The,"), set(), 2), 
            None
            )
        self.assertEqual(
            pns.pnsValidate(pns.netunidecodes(u"17:5:Names,6:Public,,3:The,"), set(), 3), 
            None
            )
        field = set()
        self.assertEqual(
            pns.pnsValidate(pns.netunidecodes(u"17:5:Names,6:Public,,3:The,"), field, 4), 
            u"17:5:Names,6:Public,,3:The,"
            )
        self.assertEqual(field, set((u"Names", u"Public", u"The" , u"5:Names,6:Public,")))

if __name__ == '__main__':
    unittest.main()