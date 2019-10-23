import json
import sys
if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

apiUrl = 'https://jisho.org/api/v1/search/words?keyword='

class japanese(object):
    def __init__(self, word, reading):
        self.word = word
        self.reading = reading

    def __str__(self):
        if self.word != '':
            return '%s (%s)' % (
                self.word,
                self.reading
                )
        else:
           return '%s' % (
               self.reading
               )

class english(object):
    def __init__(self, meaning):
        self.meaning = meaning

    def __str__(self):
        return '%s' % (
            self.meaning[0]
        )

class jishoResult(object):
    def __init__(self, iscommon, jlpt, ja, en):
        self.iscommon = iscommon
        self.jlpt = jlpt
        self.ja = ja
        self.en = en

    def __str__(self):
        return '%s = %s' % (
            self.ja[0],
            self.en[0]
        )

def parse(data):
    results = []
    if not data['data']:
        return data
    for res in data['data']:
        ja = []
        en = []
        for jar in res['japanese']:
           # This might seem silly but the code will throw KeyErrors without it soo...
            try:
                word = jar['word']
            except:
                word = '' 

            ja.append(
                japanese(
                    word,
                    jar['reading'],
                )
            )

        for enr in res['senses']:
            enm = []
            for ed in enr['english_definitions']:
                enm.append(ed)

            en.append(
                english(
                    enm
                )
            )

        if 'is_common' in res:
            common = res['is_common']
        else:
            common = False

        results.append(
            jishoResult(
                common,
                res['jlpt'],
                ja,
                en
            )
        )

    return results


def search(s):
    f = urlopen(apiUrl+s)
    s = json.loads(f.read().decode('utf-8'))
    f.close()
    return parse(s)
