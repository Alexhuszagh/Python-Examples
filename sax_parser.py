import xml.sax
from io import StringIO


EXAMPLE = u'''<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
'''


class XMLParser(xml.sax.handler.ContentHandler):
    '''Core XML handler'''

    keys = ["to", "from", "heading", "body"]

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

        self.notes = []
        for key in self.keys:
            setattr(self, key, False)

    def startElement(self, name, attrs):
        '''Element started.'''

        # get data type
        if name == 'note':
            self.note = {}
        else:
            setattr(self, name, True)

    def endElement(self, name):
        '''Element ended'''

        if name == "note":
            self.notes.append(self.note)
        else:
            setattr(self, name, False)

    def characters(self, ch):
        '''Grab characters.'''

        for key in self.keys:
            if getattr(self, key):
                self.note.setdefault(key, '')
                self.note[key] += ch


if __name__ == '__main__':
    handler = XMLParser()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    # parse data and close file object
    parser.parse(StringIO(EXAMPLE))
    print(handler.notes)
