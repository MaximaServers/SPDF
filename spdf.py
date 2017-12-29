
"""Not a Doc alv"""
import os
from pathlib import Path
import warnings
from inspect import currentframe, getframeinfo
frame__ = None

class HTMLGen:
    self_tags = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "menuitem", "meta", "param", "source", "track", "wbr"]
    escape_list = {"'":"&apos;",'"':"&quot;","ÿ":"&yuml;","á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;","Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;","ñ":"&ntilde;","Ñ":"&Ntilde;","â":"&acirc;","ê":"&ecirc;","î":"&icirc;","ô":"&ocirc;","û":"&ucirc;","Â":"&Acirc;","Ê":"&Ecirc;","Î":"&Icirc;","Ô":"&Ocirc;","Û":"&Ucirc;","ä":"&auml;","ë":"&euml;","ï":"&iuml;","ö":"&ouml;","ü":"&uuml;","Ä":"&Auml;","Ë":"&Euml;","Ï":"&Iuml;","Ö":"&Ouml;","Ü":"&Uuml;","à":"&agrave;", "è":"&egrave;", "ì":"&igrave;", "ò":"&ograve;", "ù":"&ugrave;", "À":"&Agrave;", "È":"&Egrave;", "Ì":"&Igrave;", "Ò":"&Ograve;", "Ù":"&Ugrave;"}
    
    def htmlentities(self, value):
        if value is None:
            return ''
        from xml.sax.saxutils import escape
        return escape(value,self.escape_list)
        
    @staticmethod    
    def html5_stamp():
        return "<!DOCTYPE html>"

    @staticmethod
    def isset(var):
        try:
            var
            return True
        except NameError:
            return False

    @staticmethod
    def empty(var):
        if isinstance(var, int):
            return False
        elif isinstance(var, bool):
            return False
        elif isinstance(var, str):
            if len(var) or var != '':
                return False
        elif isinstance(var, tuple) or isinstance(var, dict) or isinstance(var, list) or isinstance(var, object):
            if len(var):
                return False
        return True
            
    def base(self,**opts):
        return str(self.el('html',**opts))

    def head(self,**opts):
        return str(self.el('head',**opts))
        
    def body(self,**opts):
        return str(self.el('body',**opts))
        
    def title(self,**opts):
        return str(self.el('title',**opts))
    
    def meta(self,**opts):
        return str(self.el('meta',**opts))
        
    def div(self,**opts):
        return str(self.el('div',**opts))
        
    def link(self,**opts):
        return str(self.el('link',**opts))
    
    def script(self,**opts):
        return str(self.el('script',**opts))
        
    def style(self,**opts):
        return str(self.el('style',**opts))

    def table(self,padding=23,**opts):
        if not isinstance(padding,int):
            return False
        if padding == '0' or padding == 0 or padding == False or padding == None:
            return self.table_(**opts)
        elif padding > 0:
            return self.table_(val=
                self.tr(val=
                    self.td(css="width:"+str(padding)+"pt")+
                    self.td(val=
                        self.table_(**opts)
                    )+
                    self.td(css="width:"+str(padding)+"pt")
                )
            )
        else:
            return False
    
    def table_(self,**opts):
        return str(self.el('table',**opts))

    def tbody(self,**opts):
        return str(self.el('tbody',**opts))

    def tfoot(self,**opts):
        return str(self.el('tfoot',**opts))

    def thead(self,**opts):
        return str(self.el('thead',**opts))

    def th(self,**opts):
        return str(self.el('th',**opts))

    def td(self,**opts):
        return str(self.el('td',**opts))

    def tr(self,**opts):
        return str(self.el('tr',**opts))

    def img(self,**opts):
        return str(self.el('img',**opts))

    def el(self,tag,**opts):
        html_element = ''
        val = ''
        attr = ''
        inline_style = ''
        el_class = ''
        
        if not tag:
            tag = 'div'

        val = self.htmlentities(val)
            
        if 'attr' in opts:
            if type(opts['attr']) is dict:
                attri = opts['attr']
                for attr_ in attri:
                    if attr_ not in ['style','class','id']:
                        attr += ' ' + attr_ + '="' + str(attri[attr_]) + '"'
            
        if 'css' in opts:
            if tag == 'td':
                inline_style = ' style="padding-top:2.5pt;' + str(opts['css']) + '"'
            else:
                inline_style = ' style="' + str(opts['css']) + '"'
        else:
            if tag == 'td':
                inline_style = ' style="padding-top:2.5pt;"'
            else:
                inline_style = ''
        
        if 'el_class' in opts:
            el_class = ' class="' + str(opts['el_class']) + '"'
        else:
            el_class = ''
            
        if 'el_id' in opts:
            el_id = ' id="' + str(opts['el_id']) + '"'
        else:
            el_id = ''    
            
        tag_contents = tag+el_id+el_class+attr+inline_style
            
        if tag in self.self_tags:
            if 'val' in opts:
                val = ' value="' + str(opts['val']) + '"'
            else:
                val = ''
            tag_contents += val
            html_element = '<'+tag_contents+'>'
        else:
            if 'val' in opts:
                val = str(opts['val'])
            else:
                val = ''
            html_element = '<'+tag_contents+'>' + val + '</'+tag+'>'
        return html_element

class SPDF(object):
    """Not a Doc alv"""
    instance_ = None
    def __init__(self):
        pass

    def is_file(self, filename):
        """Not a Doc alv"""
        return bool(Path(filename).is_file())

    @staticmethod
    def str_compare(principal: str, *comparers):
        ok = False
        for comparer in comparers:
            if str(comparer).upper().lower() == principal.upper().lower():
                ok = True
        return ok
    
    def get_mimetype(self, filename):
        """Not a Doc alv"""
        if self.is_file(filename):
            import magic
            return str(magic.from_file(filename, mime=True))
        return False

    @staticmethod
    def is_html(text):
        import re
        regex = re.compile(r'.*\<(?:\/)?.*(?:\s+)?(?:.+\=\".*\")?\>.*')
        final = regex.search(text)
        return bool(final)

    @staticmethod
    def timenow():
        import datetime, time
        return str(int(time.time())) + '-' + str(datetime.datetime.now().strftime("%Y-%b-%a_%I-%M-%S%p"))

    def gen_filename(self,ext=None):
        ext_ = str(ext).strip()
        if ext is not None:
            return ext_+'-gen-' + str(self.timenow()) + '.' + ext_
        else:
            return 'gen-' + str(self.timenow())

    def merge_dict(self, a, b, path=None):
        "merges b into a"
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self.merge_dict(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass # same leaf value
                else:
                    a[key] = b[key]
            else:
                a[key] = b[key]
        return a

    def is_pdf(self, filename):
        """Not a Doc alv"""
        return bool(self.is_(filename) == 'pdf')
     
    def page_to_pdf(self, PageObj):
        import PyPDF2
        from PyPDF2.pdf import PageObject
        if isinstance(PageObj, PageObject):
            wr = PyPDF2.PdfFileWriter()
            wr.addPage(PageObj)
            temp_file = self.gen_filename('pdf')
            with open(temp_file,'wb') as temp:
                wr.write(temp)
                temp.close()
            pdf_ = Read(temp_file).let_pdf()
            os.unlink(temp_file)
            return pdf_
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('PageObject is required as parameter, go to the line ' + str(frame__.lineno))
        return False

    def pdf_from_array(self, pages: list, destination=''):
        import PyPDF2
        from PyPDF2.pdf import PageObject

        destination = str(destination).strip()

        Writer = PyPDF2.PdfFileWriter()

        for page in pages:
            if isinstance(page, PageObject):
                Writer.addPage(page)
        
        if destination == '' or destination == '/' or len(destination) <= 4:
            destination = self.gen_filename('pdf')
        try:
            with open(destination,'wb') as file:
                Writer.write(file)
            return destination
        except:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('Failed to write to pdf, go to the line ' + str(frame__.lineno))

    def is_(self, var):
        from PyPDF2.pdf import PageObject
        from PyPDF2 import PdfFileMerger
        from PyPDF2 import PdfFileReader
        from PyPDF2 import PdfFileWriter
        if isinstance(var, str) and self.is_file(var):
            mime = self.get_mimetype(var)
            if self.str_compare(mime, 'image/jpeg', 'image/png', 'image/tiff'):
                return 'image'
            elif mime == 'application/pdf':
                return 'pdf'
            elif self.str_compare(mime, 'application/xml', 'text/xml'):
                return 'xml'
        elif isinstance(var, PdfFileReader):
            return 'pdf_obj'
        elif isinstance(var, PdfFileMerger):
            return 'merger_obj'
        elif isinstance(var, PdfFileWriter):
            return 'writer_obj'
        elif isinstance(var, PageObject):
            return 'page_obj'

    def img_to_pdf(self, *img_files):
        import PyPDF2
        import xhtml2pdf.pisa as x
        from io import StringIO
        import os

        img_html = ''
        for image in img_files:
            if self.is_file(image):
                img_html += '<img src="' + image + '"><div>&nbsp;</div>'
            else:
                warnings.warn('Image location: %s, is not valid, skipped' % image)
                continue

        S = Create()
        filename_ = S.get_dest()
        S.from_(img_html)
        S.process()

        if self.is_file(filename_):
            pdf_loaded = Read(filename=filename_).let_pdf()
            os.unlink(filename_)
            if isinstance(pdf_loaded, PyPDF2.PdfFileReader):
                return pdf_loaded
            else:
                frame__ = getframeinfo(currentframe())
                raise SPDF_R('Unknown exception at returning PdfFileReader Object! - Go to the line: ' + str(frame__.lineno))
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('Fatal error, file location returned are not valid! - Go to the line: ' + str(frame__.lineno))
   
    ######CORREGIR     
    def xml_to_pdf(self,xml):
        pass
    ######CORREGIR     
    def xml_string(self,xml):
        from xml.etree import ElementTree
        if isinstance(xml, Element):
            return "Sousa"
        else:
            return "Not valid XML"
    ######CORREGIR             
    def everything_to_pdf(self, *types):
        from PyPDF2.pdf import PageObject
        from PyPDF2 import PdfFileMerger
        from PyPDF2 import PdfFileReader
        from PyPDF2 import PdfFileWriter
        recopilator = []
        is_ = self.is_
        # print(type(types[0]),'\n',type(types[1]),'\n',type(types[2]),'\n',type(types[3]),'\n',type(types[4]))
        for file in types:
            _t = is_(file)
            if _t == 'pdf':
                recopilator.append(Read(file).let_pdf())
            elif _t == 'image':
                recopilator.append(self.img_to_pdf(file))
            elif _t == 'xml':
                import xml.etree.ElementTree as ET
                import xml.dom.minidom as MD
                simple_string = open(file,'r')
                
                e = ET.parse(file).getroot()

                print(self.xml_string(e))
            elif _t == 'pdf_obj':
                recopilator.append(file)
            elif _t == 'page_obj':
                recopilator.append(self.page_to_pdf(file))
            elif _t == 'writer_obj':
                temp_file = '/tmp/' + self.gen_filename('pdf')
                print(temp_file)
            elif _t == 'merger_obj':
                temp_file = '/tmp/' + self.gen_filename('pdf')
                print(temp_file)
        return recopilator
            

class Extract(SPDF):
    """Not a Doc alv"""
    pdf_obj = None
    string_pdf = ''
    def __init__(self, filename, password=None):
        SPDF.__init__(self)
        self.open(filename,password)

    def open(self, filename, password=None):
        """Not a Doc alv"""
        if self.is_pdf(filename):
            import pdftotext
            with open(filename,'rb') as pdf:
                if password:
                    self.pdf_obj = pdftotext.PDF(pdf, password)
                else:
                    self.pdf_obj = pdftotext.PDF(pdf)
                return self
        else:
            raise Exception('File should be PDF')

    def echo_pdf(self):
        """Not a Doc alv"""
        print('\n\n'.join(self.pdf_obj))

    def throw(self):
        """Not a Doc alv"""
        return self.pdf_obj

    def get_page(self, page_no):
        """Not a Doc alv"""
        if int(page_no) == 0:
            raise SPDF_R("La página 0 no existe")
        try:
            page = self.pdf_obj[ page_no - 1 ]
        except:
            raise SPDF_R("La página no existe")
        else:
            return page
    
    def to_string(self, breaker='\n', pages=False):
        """Not a Doc alv"""
        if pages and pages > 0:
            if isinstance(pages, list):
                text = ''
                for pageno in pages:
                    text += str(breaker) + str(self.get_page(pageno))
                self.string_pdf = text
                return self
        else:
            self.string_pdf = str(breaker).join(self.pdf_obj)
            return self

    def shrink(self):
        """Not a Doc alv"""
        from pdftotext import PDF as PTT
        if len(self.string_pdf) > 0:
            import re
            return re.sub(r'\s+',' ',self.string_pdf)
        elif isinstance(self.pdf_obj, PTT):
            return self.to_string().shrink()
        else:
            return False

class SPDF_R(Exception):
    pass

class Create(SPDF):
    """Not a Doc alv"""
    text = ''
    file = ''
    html = False
    def __init__(self, destination="/",filename=''):
        SPDF.__init__(self)
        self.file = filename
        if destination is None or destination == '/' or destination == '':
            self.dest = self.gen_filename(ext='pdf')
        elif destination != '/' and len(destination) > 0:
            self.dest = destination
        self.css = {
            '@page':{
                'size':'Letter Portrait',
                'margin':'5mm 5mm 5mm 5mm'
            },
            'h1, h2, h3, h4, h5, h6, p, label':{
                'padding':'0',
                'margin':'0'
            },
            'h1':{
                'font-weight':'bold',
                'color':'black',
                'text-shadow':'0px 0px 5px black'
            },
            'h1':{
                'font-size':'20pt'
            },
            'h2':{
                'font-size':'17pt'
            },
            'h3':{
                'font-size':'14pt'
            },
            'h4':{
                'font-size':'12pt'
            },
            'h5':{
                'font-size':'10pt'
            },
            'h6':{
                'font-size':'8pt'
            },
            'body, html':{
                'font-size':'8pt',
                'color':'black'
            }
        }

    def from_(self, text=''):
        """Not a Doc alv"""
        self.text = text
        if self.is_html(text):
            self.html = True
        return self

    def with_css(self,css: dict):
        if self.file == '':
            if bool(css):
                old_css = self.css
                self.css = self.merge_dict(old_css,css)
            return self
        else:
            warnings.warn("Rendered file mode does not allow external css, include it in rendered html.")
            return self

    css_string = ''
    def generate_css_string(self, css_obj):
        if isinstance(css_obj, dict):
            for rule_1 in css_obj:
                if isinstance(css_obj[rule_1], dict):
                    self.css_string += str(rule_1).strip() + '{ '
                    self.generate_css_string(css_obj[rule_1])
                    self.css_string += ' }'
                elif isinstance(css_obj[rule_1], str):
                    self.css_string += str(rule_1).strip() + ':' + str(css_obj[rule_1]).strip() + ';'
            return '<style>' + self.css_string + '</style>'
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('Valid CSS Object is required as parameter - Go to the line: ' + str(frame__.lineno))

    def process(self):
        """Not a doc alv"""
        if self.dest != '':
            import xhtml2pdf.pisa as xh2pdf
            if self.file != '':
                if self.is_file(self.file):
                    try:
                        xh2pdf.CreatePDF(open(self.file, 'r'), open(self.dest, 'wb'))
                        return self.dest
                    except:
                        frame__ = getframeinfo(currentframe())
                        raise SPDF_R('Error trying to create a PDF! - Go to the line: ' + str(frame__.lineno))
                    else:
                        return True
            elif self.text != '':
                from io import StringIO
                css_str = str(self.generate_css_string(self.css))
                text_html = str(self.text)
                full = css_str+' '+text_html
                print(full, self.dest)

                try:
                    xh2pdf.CreatePDF(StringIO(full), open(self.dest, 'wb'))
                    return self.dest
                except:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Error trying to create a PDF! - Go to the line: ' + str(frame__.lineno))
                else:
                    return True
            else:
                frame__ = getframeinfo(currentframe())
                raise SPDF_R('Rendered file nor text/html is not defined - Go to the line: ' + str(frame__.lineno))
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('Where the file will be saved? - Go to the line: ' + str(frame__.lineno))

    def get_dest(self):
        return self.dest

    def echo_pdf(self):
        """Not a Doc alv"""
        import xhtml2pdf.pisa as xh2pdf
        pass

class Read(SPDF):
    route = None
    pdf = None
    """Not a Doc alv"""
    def __init__(self, filename):
        SPDF.__init__(self)
        self.route = filename
        self.load()

    def __iter__(self):
        return iter(self.get_all_pages())

    def check_pypdf(self):
        import PyPDF2
        if self.pdf is not None and isinstance(self.pdf, PyPDF2.PdfFileReader):
            return True
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('PDF Integrity checking failed - Go to the line: ' + str(frame__.lineno))

    def load(self):
        if self.is_pdf(self.route):
            import PyPDF2
            self.pdf = PyPDF2.PdfFileReader(Path(self.route).open('rb'),True)
            return self
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('Invalid file location! - Go to the line: ' + str(frame__.lineno))

    def get_page(self, pageno=1):
        import PyPDF2
        if self.check_pypdf(): ## Comprobar que no se pase del pinche rango
            if int(pageno) == 0:
                frame__ = getframeinfo(currentframe())
                raise SPDF_R('La página 0 no existe - Go to the line: ' + str(frame__.lineno))
            return self.pdf.getPage(int(pageno) - 1)
    def get_pages(self, *pages): 
        import PyPDF2
        if self.check_pypdf():
            recopilator = []
            for page in pages:
                if int(page) == 0:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('La página 0 no existe - Go to the line: ' + str(frame__.lineno))
                recopilator.append(self.pdf.getPage(int(page) - 1))
            return recopilator
    
    def get_all_pages(self):
        if self.check_pypdf():
            recopilator = []
            pages = self.pdf.getNumPages()
            for page in range(0,pages):
                recopilator.append(self.pdf.getPage(page))
            return recopilator

    def get_page_range(self, from_='start', to_='end'):
        if self.check_pypdf():
            recopilator = []

            maxsize = int(self.pdf.getNumPages())

            if isinstance(from_, str) and isinstance(to_, str):
                print('str-str')

                from_ = str(from_).lower()
                to_ = str(to_).lower()

                if self.str_compare(from_,'half','h'):
                    import math
                    from_ = math.ceil(maxsize / 2)
                elif self.str_compare(from_,'not last','nl'):
                    from_ = maxsize - 1
                elif self.str_compare(from_,'not first','nf'):
                    from_ = 2
                elif self.str_compare(from_,'first','start','f','s'):
                    from_ = 1
                elif self.str_compare(from_,'last','end','l','e'):
                    from_ = maxsize
                else:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Invalid param for from_ - Go to the line: ' + str(frame__.lineno))

                if self.str_compare(to_,'half','h'):
                    import math
                    to_ = math.ceil(maxsize / 2)
                elif self.str_compare(to_,'not last','nl'):
                    to_ = maxsize - 1
                elif self.str_compare(to_,'not first','nf'):
                    to_ = 2
                elif self.str_compare(to_,'first','start','f','s'):
                    to_ = 1
                elif self.str_compare(to_,'last','end','l','e'):
                    to_ = maxsize
                else:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Invalid param for to_ - Go to the line: ' + str(frame__.lineno))
                return self.get_page_range(from_=from_,to_=to_)

            elif isinstance(from_, int) and isinstance(to_, int):
                print('int-int')
                if from_ <= 0 or to_ <= 0 or from_ > maxsize or to_ > maxsize:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Invalid pages - Go to the line: ' + str(frame__.lineno))

                if from_ == to_:
                    print('equal')
                    return [self.pdf.getPage(from_ - 1)]

                if from_ < to_:
                    print('from < to')
                    recopilator = []
                    for page in range(from_, to_ + 1):
                        real_page = page - 1
                        recopilator.append(self.pdf.getPage(real_page))
                    return recopilator

                if from_ > to_:
                    print('from > to')
                    recopilator = []
                    for page in range(from_, to_ - 1, -1):
                        real_page = page - 1 
                        recopilator.append(self.pdf.getPage(real_page))
                    return recopilator

            elif isinstance(from_, int) and isinstance(to_, str):
                print('int-str')
                if from_ <= 0 or from_ > maxsize:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Invalid pages - Go to the line: ' + str(frame__.lineno))
                
                to_ = str(to_).lower()
                if self.str_compare(to_,'half','h'):
                    import math
                    to_ = math.ceil(maxsize / 2)
                elif self.str_compare(to_,'not last','nl'):
                    to_ = maxsize - 1
                elif self.str_compare(to_,'not first','nf'):
                    to_ = 2
                elif self.str_compare(to_,'first','start','f','s'):
                    to_ = 1
                elif self.str_compare(to_,'last','end','l','e'):
                    to_ = maxsize
                else:
                    raise SPDF_R('Invalid param for to_ - Go to the line: ' + str(frame__.lineno))
                return self.get_page_range(from_=from_,to_=to_)

            elif isinstance(from_, str) and isinstance(to_, int):
                print('str-int')

                if to_ <= 0 or to_ > maxsize:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Invalid pages - Go to the line: ' + str(frame__.lineno))
                
                from_ = str(from_).lower()
                if self.str_compare(from_,'half','h'):
                    import math
                    from_ = math.ceil(maxsize / 2)
                elif self.str_compare(from_,'not last','nl'):
                    from_ = maxsize - 1
                elif self.str_compare(from_,'not first','nf'):
                    from_ = 2
                elif self.str_compare(from_,'first','start','f','s'):
                    from_ = 1
                elif self.str_compare(from_,'last','end','l','e'):
                    from_ = maxsize
                else:
                    frame__ = getframeinfo(currentframe())
                    raise SPDF_R('Invalid param for from_ - Go to the line: ' + str(frame__.lineno))
                return self.get_page_range(from_=from_,to_=to_)
            else:
                frame__ = getframeinfo(currentframe())
                raise SPDF_R('Invalid parameters - Go to the line: ' + str(frame__.lineno))

    def let_pdf(self):
        if self.pdf is not None:
            return self.pdf
        else: 
            return False

class Merge(SPDF):
    """Not a Doc alv"""
    merger = False
    def __init__(self):
        SPDF.__init__(self)

    def prepare(self,*pdfs):
        import PyPDF2
        merger = PyPDF2.PdfFileMerger()

        for pdf in pdfs:
            if (isinstance(pdf, PyPDF2.PdfFileReader)):
                merger.append(pdf)
            elif(isinstance(pdf, PyPDF2.pdf.PageObject)):
                print('PageObject')
                merger.append(self.page_to_pdf(pdf))
            elif isinstance(pdf, PyPDF2.PdfFileMerger):
                print('MergerObject')
                merger.append(self.merger_to_pdf(pdf))
            elif isinstance(pdf, str):
                _is = self.is_(pdf)
                if _is == 'image':
                    reader = self.img_to_pdf(pdf)
                    merger.append(reader)
                elif _is == 'xml':
                    print('XML file reading, not implemented yet.')
                    pass
                elif _is == 'pdf':
                    reader = Read(pdf).let_pdf()
                    merger.append(reader)
            else:
                frame__ = getframeinfo(currentframe())
                raise SPDF_R('Unknown file-type - Go to the line: ' + str(frame__.lineno))
        self.merger = merger
        return self

    def prepare_one(self, pdf):
        import PyPDF2
        merger = self.merger

        if not isinstance(merger, PyPDF2.PdfFileMerger):
            merger = PyPDF2.PdfFileMerger()

        if (isinstance(pdf, PyPDF2.PdfFileReader)):
            print('PDFObject')
            merger.append(pdf)
        elif(isinstance(pdf, PyPDF2.pdf.PageObject)):
            print('PageObject')
            merger.append(self.page_to_pdf(pdf))
        elif isinstance(pdf, PyPDF2.PdfFileMerger):
            print('MergerObject')
            merger.append(self.merger_to_pdf(pdf))
        elif isinstance(pdf, str):
            _is = self.is_(pdf)
            if _is == 'image':
                reader = self.img_to_pdf(pdf)
                merger.append(reader)
            elif _is == 'xml':
                print('XML file reading, not implemented yet.')
                pass
            elif _is == 'pdf':
                reader = Read(pdf).let_pdf()
                merger.append(reader)
        else:
            frame__ = getframeinfo(currentframe())
            raise SPDF_R('Unknown file-type - Go to the line: ' + str(frame__.lineno))
        
        self.merger = merger
        return self

    def merger_to_pdf(self, merger_):
        loc = self.gen_filename('pdf')
        with open(loc,'wb') as file_:
            merger_.write(file_)
            file_.close()
        return Read(loc).let_pdf()
        
    def merge(self,destination=None):
        if self.merger:
            if not destination or not isinstance(destination, str):
                destination = self.gen_filename('pdf')
            with open(destination,'wb') as file_:
                self.merger.write(file_)
                file_.close()
            return destination
        else:
            raise SPDF_R("There's no PDF to merge.")

    def to_merge_to(self,file,destination=None):
        if self.merger:
            if self.is_pdf(file):
                from PyPDF2 import PdfFileMerger
                new = PdfFileMerger()
                new.append(Read(file).let_pdf())
                new.append(self.merger_to_pdf(self.merger))
                if not destination or not isinstance(destination, str):
                    destination = self.gen_filename('pdf')
                with open(destination,'wb') as file_:
                    new.write(file_)
                    file_.close()
                return destination
            else:
                raise SPDF_R("Merge to what?")
        raise SPDF_R("There's no PDF to merge.")