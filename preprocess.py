import re
import pandas as pd

class preprocess:
    import re
import pandas as pd

class preprocess:
    def tlt(cls,intab,txt):
        return txt.translate({ord(k):v for k,v, in zip(intab,outtab)})
    def clean(self,text):
        
        intab='۱۲۳۴۵۶۷۸۹۰١٢٣٤٥٦٧٨٩٠'
        outtab='12345678901234567890'
        translation_table = str.maketrans(intab, outtab)
        text = text.translate(translation_table)
        tex = re.sub(r"(?:\@|https?\://)\s+"," ",text)
        text = re.findall(r"[A-Za-z._]+|[^A-Za-z\W]+",text,re.UNICODE)
#         text = re.findall(r"[^A-Za-z\W]+",text,re.UNICODE)
        text = ' '.join(word for word in text)
       
        
        cleanr = re.compile('<.*?>')
        #cleanr = re.compile(r'<[^>]+>')
        text = re.sub(cleanr,'',text)
        
        text = re.sub(r"""\d""",'',text)
#         text = re.sub(r"""(/){1,}""",'-',text)
#         text = re.findall(r"[^\dA-Za-z\W]+|\d+",text,re.UNICODE)
#         text = ' '.join(word for word in text)
        
        text = re.sub('\r?\n','.',text)
        text = re.sub(r"-{3}",'',text)
        text = re.sub(r"-{2}",'',text)
        text = re.sub(r"""\s*\.{3,}""",u'.',text)
        text = re.sub(r"""\s*\.{2,}""",u'.',text)
        text = re.sub(r"""\s+(ن؟می)\s+""",r'\1',text)
#         text = re.sub(r"""\\d{2-3}\s+[^\dA-Za-z\W]\s+\\d{2-3}""",r'\1',text)
#         text = re.sub(r"""\s+(ی)ها|?(?(ن))
        text = re.sub(r"""(!){2,}""",r'\1',text)
        #text = re.sub(r"""(/\){2,}""",r'\1',text)
        text = re.sub(r"""(/ ){2,}""",'',text)
        text = re.sub(r"""( /){2,}""",'',text)
        text = re.sub(r"""(//){2,}""",'',text)
        text = re.sub(r"""(/){2,}""",'',text)
        text = re.sub(r"""(؟){2,}""",r'\1',text)
        text = re.sub(r"""_+""","",text)
        text = re.sub(r"""[ ]+""",r' ',text)
        text = re.sub(r"""([\n]+)[\t]*""",r'\1',text)
        text = re.sub(r"\b[a-zA-Z]\b", "", text)
        p = re.compile(r'<.*?>')
        text = p.sub('', text)
        text = re.sub(r"""product""","",text)
        text = re.sub(r"""dkp""","",text)
        text = re.sub(r"""br""","",text)
        text = re.sub(r"""mm""","",text)
        text = text.strip()
        
        return text