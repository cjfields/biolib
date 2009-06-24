# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _bpp_fontmanager
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class Clonable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Clonable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Clonable, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _bpp_fontmanager.delete_Clonable
    __del__ = lambda self : None;
    def clone(*args): return _bpp_fontmanager.Clonable_clone(*args)
Clonable_swigregister = _bpp_fontmanager.Clonable_swigregister
Clonable_swigregister(Clonable)

class Font(Clonable):
    __swig_setmethods__ = {}
    for _s in [Clonable]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Font, name, value)
    __swig_getmethods__ = {}
    for _s in [Clonable]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Font, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_Font(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_Font
    __del__ = lambda self : None;
    def clone(*args): return _bpp_fontmanager.Font_clone(*args)
    def __eq__(*args): return _bpp_fontmanager.Font___eq__(*args)
    def getFamily(*args): return _bpp_fontmanager.Font_getFamily(*args)
    def getSeries(*args): return _bpp_fontmanager.Font_getSeries(*args)
    def getType(*args): return _bpp_fontmanager.Font_getType(*args)
    def getSize(*args): return _bpp_fontmanager.Font_getSize(*args)
    def setFamily(*args): return _bpp_fontmanager.Font_setFamily(*args)
    def setSeries(*args): return _bpp_fontmanager.Font_setSeries(*args)
    def setType(*args): return _bpp_fontmanager.Font_setType(*args)
    def setSize(*args): return _bpp_fontmanager.Font_setSize(*args)
    def toString(*args): return _bpp_fontmanager.Font_toString(*args)
Font_swigregister = _bpp_fontmanager.Font_swigregister
Font_swigregister(Font)

class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _bpp_fontmanager.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _bpp_fontmanager.PySwigIterator_value(*args)
    def incr(*args): return _bpp_fontmanager.PySwigIterator_incr(*args)
    def decr(*args): return _bpp_fontmanager.PySwigIterator_decr(*args)
    def distance(*args): return _bpp_fontmanager.PySwigIterator_distance(*args)
    def equal(*args): return _bpp_fontmanager.PySwigIterator_equal(*args)
    def copy(*args): return _bpp_fontmanager.PySwigIterator_copy(*args)
    def next(*args): return _bpp_fontmanager.PySwigIterator_next(*args)
    def previous(*args): return _bpp_fontmanager.PySwigIterator_previous(*args)
    def advance(*args): return _bpp_fontmanager.PySwigIterator_advance(*args)
    def __eq__(*args): return _bpp_fontmanager.PySwigIterator___eq__(*args)
    def __ne__(*args): return _bpp_fontmanager.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _bpp_fontmanager.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _bpp_fontmanager.PySwigIterator___isub__(*args)
    def __add__(*args): return _bpp_fontmanager.PySwigIterator___add__(*args)
    def __sub__(*args): return _bpp_fontmanager.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _bpp_fontmanager.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

class Exception:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Exception, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Exception, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_Exception(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_Exception
    __del__ = lambda self : None;
    def what(*args): return _bpp_fontmanager.Exception_what(*args)
Exception_swigregister = _bpp_fontmanager.Exception_swigregister
Exception_swigregister(Exception)

class IOException(Exception):
    __swig_setmethods__ = {}
    for _s in [Exception]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IOException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, IOException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_IOException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_IOException
    __del__ = lambda self : None;
IOException_swigregister = _bpp_fontmanager.IOException_swigregister
IOException_swigregister(IOException)

class NullPointerException(Exception):
    __swig_setmethods__ = {}
    for _s in [Exception]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NullPointerException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NullPointerException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_NullPointerException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_NullPointerException
    __del__ = lambda self : None;
NullPointerException_swigregister = _bpp_fontmanager.NullPointerException_swigregister
NullPointerException_swigregister(NullPointerException)

class ZeroDivisionException(Exception):
    __swig_setmethods__ = {}
    for _s in [Exception]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ZeroDivisionException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ZeroDivisionException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_ZeroDivisionException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_ZeroDivisionException
    __del__ = lambda self : None;
ZeroDivisionException_swigregister = _bpp_fontmanager.ZeroDivisionException_swigregister
ZeroDivisionException_swigregister(ZeroDivisionException)

class BadIntegerException(Exception):
    __swig_setmethods__ = {}
    for _s in [Exception]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BadIntegerException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, BadIntegerException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_BadIntegerException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_BadIntegerException
    __del__ = lambda self : None;
    def getBadInteger(*args): return _bpp_fontmanager.BadIntegerException_getBadInteger(*args)
BadIntegerException_swigregister = _bpp_fontmanager.BadIntegerException_swigregister
BadIntegerException_swigregister(BadIntegerException)

class BadNumberException(Exception):
    __swig_setmethods__ = {}
    for _s in [Exception]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BadNumberException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, BadNumberException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_BadNumberException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_BadNumberException
    __del__ = lambda self : None;
    def getBadNumber(*args): return _bpp_fontmanager.BadNumberException_getBadNumber(*args)
BadNumberException_swigregister = _bpp_fontmanager.BadNumberException_swigregister
BadNumberException_swigregister(BadNumberException)

class NumberFormatException(Exception):
    __swig_setmethods__ = {}
    for _s in [Exception]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NumberFormatException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NumberFormatException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_NumberFormatException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_NumberFormatException
    __del__ = lambda self : None;
    def getBadNumber(*args): return _bpp_fontmanager.NumberFormatException_getBadNumber(*args)
NumberFormatException_swigregister = _bpp_fontmanager.NumberFormatException_swigregister
NumberFormatException_swigregister(NumberFormatException)

class IndexOutOfBoundsException(BadIntegerException):
    __swig_setmethods__ = {}
    for _s in [BadIntegerException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IndexOutOfBoundsException, name, value)
    __swig_getmethods__ = {}
    for _s in [BadIntegerException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, IndexOutOfBoundsException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_IndexOutOfBoundsException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_IndexOutOfBoundsException
    __del__ = lambda self : None;
    def getBounds(*args): return _bpp_fontmanager.IndexOutOfBoundsException_getBounds(*args)
IndexOutOfBoundsException_swigregister = _bpp_fontmanager.IndexOutOfBoundsException_swigregister
IndexOutOfBoundsException_swigregister(IndexOutOfBoundsException)

class ios_base(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ios_base, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ios_base, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    erase_event = _bpp_fontmanager.ios_base_erase_event
    imbue_event = _bpp_fontmanager.ios_base_imbue_event
    copyfmt_event = _bpp_fontmanager.ios_base_copyfmt_event
    def register_callback(*args): return _bpp_fontmanager.ios_base_register_callback(*args)
    def flags(*args): return _bpp_fontmanager.ios_base_flags(*args)
    def setf(*args): return _bpp_fontmanager.ios_base_setf(*args)
    def unsetf(*args): return _bpp_fontmanager.ios_base_unsetf(*args)
    def precision(*args): return _bpp_fontmanager.ios_base_precision(*args)
    def width(*args): return _bpp_fontmanager.ios_base_width(*args)
    __swig_getmethods__["sync_with_stdio"] = lambda x: _bpp_fontmanager.ios_base_sync_with_stdio
    if _newclass:sync_with_stdio = staticmethod(_bpp_fontmanager.ios_base_sync_with_stdio)
    def imbue(*args): return _bpp_fontmanager.ios_base_imbue(*args)
    def getloc(*args): return _bpp_fontmanager.ios_base_getloc(*args)
    __swig_getmethods__["xalloc"] = lambda x: _bpp_fontmanager.ios_base_xalloc
    if _newclass:xalloc = staticmethod(_bpp_fontmanager.ios_base_xalloc)
    def iword(*args): return _bpp_fontmanager.ios_base_iword(*args)
    def pword(*args): return _bpp_fontmanager.ios_base_pword(*args)
    __swig_destroy__ = _bpp_fontmanager.delete_ios_base
    __del__ = lambda self : None;
ios_base_swigregister = _bpp_fontmanager.ios_base_swigregister
ios_base_swigregister(ios_base)
cvar = _bpp_fontmanager.cvar
ios_base.boolalpha = _bpp_fontmanager.cvar.ios_base_boolalpha
ios_base.dec = _bpp_fontmanager.cvar.ios_base_dec
ios_base.fixed = _bpp_fontmanager.cvar.ios_base_fixed
ios_base.hex = _bpp_fontmanager.cvar.ios_base_hex
ios_base.internal = _bpp_fontmanager.cvar.ios_base_internal
ios_base.left = _bpp_fontmanager.cvar.ios_base_left
ios_base.oct = _bpp_fontmanager.cvar.ios_base_oct
ios_base.right = _bpp_fontmanager.cvar.ios_base_right
ios_base.scientific = _bpp_fontmanager.cvar.ios_base_scientific
ios_base.showbase = _bpp_fontmanager.cvar.ios_base_showbase
ios_base.showpoint = _bpp_fontmanager.cvar.ios_base_showpoint
ios_base.showpos = _bpp_fontmanager.cvar.ios_base_showpos
ios_base.skipws = _bpp_fontmanager.cvar.ios_base_skipws
ios_base.unitbuf = _bpp_fontmanager.cvar.ios_base_unitbuf
ios_base.uppercase = _bpp_fontmanager.cvar.ios_base_uppercase
ios_base.adjustfield = _bpp_fontmanager.cvar.ios_base_adjustfield
ios_base.basefield = _bpp_fontmanager.cvar.ios_base_basefield
ios_base.floatfield = _bpp_fontmanager.cvar.ios_base_floatfield
ios_base.badbit = _bpp_fontmanager.cvar.ios_base_badbit
ios_base.eofbit = _bpp_fontmanager.cvar.ios_base_eofbit
ios_base.failbit = _bpp_fontmanager.cvar.ios_base_failbit
ios_base.goodbit = _bpp_fontmanager.cvar.ios_base_goodbit
ios_base.app = _bpp_fontmanager.cvar.ios_base_app
ios_base.ate = _bpp_fontmanager.cvar.ios_base_ate
ios_base.binary = _bpp_fontmanager.cvar.ios_base_binary
ios_base.ios_base_in = _bpp_fontmanager.cvar.ios_base_ios_base_in
ios_base.out = _bpp_fontmanager.cvar.ios_base_out
ios_base.trunc = _bpp_fontmanager.cvar.ios_base_trunc
ios_base.beg = _bpp_fontmanager.cvar.ios_base_beg
ios_base.cur = _bpp_fontmanager.cvar.ios_base_cur
ios_base.end = _bpp_fontmanager.cvar.ios_base_end
ios_base_sync_with_stdio = _bpp_fontmanager.ios_base_sync_with_stdio
ios_base_xalloc = _bpp_fontmanager.ios_base_xalloc

class ios(ios_base):
    __swig_setmethods__ = {}
    for _s in [ios_base]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ios, name, value)
    __swig_getmethods__ = {}
    for _s in [ios_base]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ios, name)
    __repr__ = _swig_repr
    def rdstate(*args): return _bpp_fontmanager.ios_rdstate(*args)
    def clear(*args): return _bpp_fontmanager.ios_clear(*args)
    def setstate(*args): return _bpp_fontmanager.ios_setstate(*args)
    def good(*args): return _bpp_fontmanager.ios_good(*args)
    def eof(*args): return _bpp_fontmanager.ios_eof(*args)
    def fail(*args): return _bpp_fontmanager.ios_fail(*args)
    def bad(*args): return _bpp_fontmanager.ios_bad(*args)
    def exceptions(*args): return _bpp_fontmanager.ios_exceptions(*args)
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_ios(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_ios
    __del__ = lambda self : None;
    def tie(*args): return _bpp_fontmanager.ios_tie(*args)
    def rdbuf(*args): return _bpp_fontmanager.ios_rdbuf(*args)
    def copyfmt(*args): return _bpp_fontmanager.ios_copyfmt(*args)
    def fill(*args): return _bpp_fontmanager.ios_fill(*args)
    def imbue(*args): return _bpp_fontmanager.ios_imbue(*args)
    def narrow(*args): return _bpp_fontmanager.ios_narrow(*args)
    def widen(*args): return _bpp_fontmanager.ios_widen(*args)
ios_swigregister = _bpp_fontmanager.ios_swigregister
ios_swigregister(ios)

class streambuf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, streambuf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, streambuf, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _bpp_fontmanager.delete_streambuf
    __del__ = lambda self : None;
    def pubimbue(*args): return _bpp_fontmanager.streambuf_pubimbue(*args)
    def getloc(*args): return _bpp_fontmanager.streambuf_getloc(*args)
    def pubsetbuf(*args): return _bpp_fontmanager.streambuf_pubsetbuf(*args)
    def pubseekoff(*args): return _bpp_fontmanager.streambuf_pubseekoff(*args)
    def pubseekpos(*args): return _bpp_fontmanager.streambuf_pubseekpos(*args)
    def pubsync(*args): return _bpp_fontmanager.streambuf_pubsync(*args)
    def in_avail(*args): return _bpp_fontmanager.streambuf_in_avail(*args)
    def snextc(*args): return _bpp_fontmanager.streambuf_snextc(*args)
    def sbumpc(*args): return _bpp_fontmanager.streambuf_sbumpc(*args)
    def sgetc(*args): return _bpp_fontmanager.streambuf_sgetc(*args)
    def sgetn(*args): return _bpp_fontmanager.streambuf_sgetn(*args)
    def sputbackc(*args): return _bpp_fontmanager.streambuf_sputbackc(*args)
    def sungetc(*args): return _bpp_fontmanager.streambuf_sungetc(*args)
    def sputc(*args): return _bpp_fontmanager.streambuf_sputc(*args)
    def sputn(*args): return _bpp_fontmanager.streambuf_sputn(*args)
streambuf_swigregister = _bpp_fontmanager.streambuf_swigregister
streambuf_swigregister(streambuf)

class ostream(ios):
    __swig_setmethods__ = {}
    for _s in [ios]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ostream, name, value)
    __swig_getmethods__ = {}
    for _s in [ios]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ostream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_ostream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_ostream
    __del__ = lambda self : None;
    def __lshift__(*args): return _bpp_fontmanager.ostream___lshift__(*args)
    def put(*args): return _bpp_fontmanager.ostream_put(*args)
    def write(*args): return _bpp_fontmanager.ostream_write(*args)
    def flush(*args): return _bpp_fontmanager.ostream_flush(*args)
    def tellp(*args): return _bpp_fontmanager.ostream_tellp(*args)
    def seekp(*args): return _bpp_fontmanager.ostream_seekp(*args)
ostream_swigregister = _bpp_fontmanager.ostream_swigregister
ostream_swigregister(ostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

class istream(ios):
    __swig_setmethods__ = {}
    for _s in [ios]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, istream, name, value)
    __swig_getmethods__ = {}
    for _s in [ios]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, istream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_istream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_istream
    __del__ = lambda self : None;
    def __rshift__(*args): return _bpp_fontmanager.istream___rshift__(*args)
    def gcount(*args): return _bpp_fontmanager.istream_gcount(*args)
    def get(*args): return _bpp_fontmanager.istream_get(*args)
    def getline(*args): return _bpp_fontmanager.istream_getline(*args)
    def ignore(*args): return _bpp_fontmanager.istream_ignore(*args)
    def peek(*args): return _bpp_fontmanager.istream_peek(*args)
    def read(*args): return _bpp_fontmanager.istream_read(*args)
    def readsome(*args): return _bpp_fontmanager.istream_readsome(*args)
    def putback(*args): return _bpp_fontmanager.istream_putback(*args)
    def unget(*args): return _bpp_fontmanager.istream_unget(*args)
    def sync(*args): return _bpp_fontmanager.istream_sync(*args)
    def tellg(*args): return _bpp_fontmanager.istream_tellg(*args)
    def seekg(*args): return _bpp_fontmanager.istream_seekg(*args)
istream_swigregister = _bpp_fontmanager.istream_swigregister
istream_swigregister(istream)

class iostream(istream,ostream):
    __swig_setmethods__ = {}
    for _s in [istream,ostream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, iostream, name, value)
    __swig_getmethods__ = {}
    for _s in [istream,ostream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, iostream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_iostream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_iostream
    __del__ = lambda self : None;
iostream_swigregister = _bpp_fontmanager.iostream_swigregister
iostream_swigregister(iostream)

endl_cb_ptr = _bpp_fontmanager.endl_cb_ptr
endl = _bpp_fontmanager.endl
ends_cb_ptr = _bpp_fontmanager.ends_cb_ptr
ends = _bpp_fontmanager.ends
flush_cb_ptr = _bpp_fontmanager.flush_cb_ptr
flush = _bpp_fontmanager.flush
class istringstream(istream):
    __swig_setmethods__ = {}
    for _s in [istream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, istringstream, name, value)
    __swig_getmethods__ = {}
    for _s in [istream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, istringstream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_istringstream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_istringstream
    __del__ = lambda self : None;
    def rdbuf(*args): return _bpp_fontmanager.istringstream_rdbuf(*args)
    def str(*args): return _bpp_fontmanager.istringstream_str(*args)
istringstream_swigregister = _bpp_fontmanager.istringstream_swigregister
istringstream_swigregister(istringstream)

class ostringstream(ostream):
    __swig_setmethods__ = {}
    for _s in [ostream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ostringstream, name, value)
    __swig_getmethods__ = {}
    for _s in [ostream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ostringstream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_ostringstream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_ostringstream
    __del__ = lambda self : None;
    def rdbuf(*args): return _bpp_fontmanager.ostringstream_rdbuf(*args)
    def str(*args): return _bpp_fontmanager.ostringstream_str(*args)
ostringstream_swigregister = _bpp_fontmanager.ostringstream_swigregister
ostringstream_swigregister(ostringstream)

class stringstream(iostream):
    __swig_setmethods__ = {}
    for _s in [iostream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, stringstream, name, value)
    __swig_getmethods__ = {}
    for _s in [iostream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, stringstream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_stringstream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_stringstream
    __del__ = lambda self : None;
    def rdbuf(*args): return _bpp_fontmanager.stringstream_rdbuf(*args)
    def str(*args): return _bpp_fontmanager.stringstream_str(*args)
stringstream_swigregister = _bpp_fontmanager.stringstream_swigregister
stringstream_swigregister(stringstream)

class TextTools(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TextTools, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TextTools, name)
    __repr__ = _swig_repr
    __swig_getmethods__["isEmpty"] = lambda x: _bpp_fontmanager.TextTools_isEmpty
    if _newclass:isEmpty = staticmethod(_bpp_fontmanager.TextTools_isEmpty)
    __swig_getmethods__["toUpper"] = lambda x: _bpp_fontmanager.TextTools_toUpper
    if _newclass:toUpper = staticmethod(_bpp_fontmanager.TextTools_toUpper)
    __swig_getmethods__["toLower"] = lambda x: _bpp_fontmanager.TextTools_toLower
    if _newclass:toLower = staticmethod(_bpp_fontmanager.TextTools_toLower)
    __swig_getmethods__["isWhiteSpaceCharacter"] = lambda x: _bpp_fontmanager.TextTools_isWhiteSpaceCharacter
    if _newclass:isWhiteSpaceCharacter = staticmethod(_bpp_fontmanager.TextTools_isWhiteSpaceCharacter)
    __swig_getmethods__["removeWhiteSpaces"] = lambda x: _bpp_fontmanager.TextTools_removeWhiteSpaces
    if _newclass:removeWhiteSpaces = staticmethod(_bpp_fontmanager.TextTools_removeWhiteSpaces)
    __swig_getmethods__["removeFirstWhiteSpaces"] = lambda x: _bpp_fontmanager.TextTools_removeFirstWhiteSpaces
    if _newclass:removeFirstWhiteSpaces = staticmethod(_bpp_fontmanager.TextTools_removeFirstWhiteSpaces)
    __swig_getmethods__["removeLastWhiteSpaces"] = lambda x: _bpp_fontmanager.TextTools_removeLastWhiteSpaces
    if _newclass:removeLastWhiteSpaces = staticmethod(_bpp_fontmanager.TextTools_removeLastWhiteSpaces)
    __swig_getmethods__["removeSurroundingWhiteSpaces"] = lambda x: _bpp_fontmanager.TextTools_removeSurroundingWhiteSpaces
    if _newclass:removeSurroundingWhiteSpaces = staticmethod(_bpp_fontmanager.TextTools_removeSurroundingWhiteSpaces)
    __swig_getmethods__["isNewLineCharacter"] = lambda x: _bpp_fontmanager.TextTools_isNewLineCharacter
    if _newclass:isNewLineCharacter = staticmethod(_bpp_fontmanager.TextTools_isNewLineCharacter)
    __swig_getmethods__["removeNewLines"] = lambda x: _bpp_fontmanager.TextTools_removeNewLines
    if _newclass:removeNewLines = staticmethod(_bpp_fontmanager.TextTools_removeNewLines)
    __swig_getmethods__["removeLastNewLines"] = lambda x: _bpp_fontmanager.TextTools_removeLastNewLines
    if _newclass:removeLastNewLines = staticmethod(_bpp_fontmanager.TextTools_removeLastNewLines)
    __swig_getmethods__["isDecimalNumber"] = lambda x: _bpp_fontmanager.TextTools_isDecimalNumber
    if _newclass:isDecimalNumber = staticmethod(_bpp_fontmanager.TextTools_isDecimalNumber)
    __swig_getmethods__["toString"] = lambda x: _bpp_fontmanager.TextTools_toString
    if _newclass:toString = staticmethod(_bpp_fontmanager.TextTools_toString)
    __swig_getmethods__["toInt"] = lambda x: _bpp_fontmanager.TextTools_toInt
    if _newclass:toInt = staticmethod(_bpp_fontmanager.TextTools_toInt)
    __swig_getmethods__["toDouble"] = lambda x: _bpp_fontmanager.TextTools_toDouble
    if _newclass:toDouble = staticmethod(_bpp_fontmanager.TextTools_toDouble)
    __swig_getmethods__["resizeRight"] = lambda x: _bpp_fontmanager.TextTools_resizeRight
    if _newclass:resizeRight = staticmethod(_bpp_fontmanager.TextTools_resizeRight)
    __swig_getmethods__["resizeLeft"] = lambda x: _bpp_fontmanager.TextTools_resizeLeft
    if _newclass:resizeLeft = staticmethod(_bpp_fontmanager.TextTools_resizeLeft)
    __swig_getmethods__["split"] = lambda x: _bpp_fontmanager.TextTools_split
    if _newclass:split = staticmethod(_bpp_fontmanager.TextTools_split)
    __swig_getmethods__["removeSubstrings"] = lambda x: _bpp_fontmanager.TextTools_removeSubstrings
    if _newclass:removeSubstrings = staticmethod(_bpp_fontmanager.TextTools_removeSubstrings)
    __swig_getmethods__["removeChar"] = lambda x: _bpp_fontmanager.TextTools_removeChar
    if _newclass:removeChar = staticmethod(_bpp_fontmanager.TextTools_removeChar)
    __swig_getmethods__["count"] = lambda x: _bpp_fontmanager.TextTools_count
    if _newclass:count = staticmethod(_bpp_fontmanager.TextTools_count)
    __swig_getmethods__["startsWith"] = lambda x: _bpp_fontmanager.TextTools_startsWith
    if _newclass:startsWith = staticmethod(_bpp_fontmanager.TextTools_startsWith)
    __swig_getmethods__["endsWith"] = lambda x: _bpp_fontmanager.TextTools_endsWith
    if _newclass:endsWith = staticmethod(_bpp_fontmanager.TextTools_endsWith)
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_TextTools(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_TextTools
    __del__ = lambda self : None;
TextTools_swigregister = _bpp_fontmanager.TextTools_swigregister
TextTools_swigregister(TextTools)
TextTools_isEmpty = _bpp_fontmanager.TextTools_isEmpty
TextTools_toUpper = _bpp_fontmanager.TextTools_toUpper
TextTools_toLower = _bpp_fontmanager.TextTools_toLower
TextTools_isWhiteSpaceCharacter = _bpp_fontmanager.TextTools_isWhiteSpaceCharacter
TextTools_removeWhiteSpaces = _bpp_fontmanager.TextTools_removeWhiteSpaces
TextTools_removeFirstWhiteSpaces = _bpp_fontmanager.TextTools_removeFirstWhiteSpaces
TextTools_removeLastWhiteSpaces = _bpp_fontmanager.TextTools_removeLastWhiteSpaces
TextTools_removeSurroundingWhiteSpaces = _bpp_fontmanager.TextTools_removeSurroundingWhiteSpaces
TextTools_isNewLineCharacter = _bpp_fontmanager.TextTools_isNewLineCharacter
TextTools_removeNewLines = _bpp_fontmanager.TextTools_removeNewLines
TextTools_removeLastNewLines = _bpp_fontmanager.TextTools_removeLastNewLines
TextTools_isDecimalNumber = _bpp_fontmanager.TextTools_isDecimalNumber
TextTools_toString = _bpp_fontmanager.TextTools_toString
TextTools_toInt = _bpp_fontmanager.TextTools_toInt
TextTools_toDouble = _bpp_fontmanager.TextTools_toDouble
TextTools_resizeRight = _bpp_fontmanager.TextTools_resizeRight
TextTools_resizeLeft = _bpp_fontmanager.TextTools_resizeLeft
TextTools_split = _bpp_fontmanager.TextTools_split
TextTools_removeSubstrings = _bpp_fontmanager.TextTools_removeSubstrings
TextTools_removeChar = _bpp_fontmanager.TextTools_removeChar
TextTools_count = _bpp_fontmanager.TextTools_count
TextTools_startsWith = _bpp_fontmanager.TextTools_startsWith
TextTools_endsWith = _bpp_fontmanager.TextTools_endsWith

class intFontManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intFontManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intFontManager, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _bpp_fontmanager.delete_intFontManager
    __del__ = lambda self : None;
    def getCode(*args): return _bpp_fontmanager.intFontManager_getCode(*args)
    def getFont(*args): return _bpp_fontmanager.intFontManager_getFont(*args)
    def getCodes(*args): return _bpp_fontmanager.intFontManager_getCodes(*args)
    def getFonts(*args): return _bpp_fontmanager.intFontManager_getFonts(*args)
    def getNumberOfFonts(*args): return _bpp_fontmanager.intFontManager_getNumberOfFonts(*args)
intFontManager_swigregister = _bpp_fontmanager.intFontManager_swigregister
intFontManager_swigregister(intFontManager)

class doubleFontManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleFontManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleFontManager, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _bpp_fontmanager.delete_doubleFontManager
    __del__ = lambda self : None;
    def getCode(*args): return _bpp_fontmanager.doubleFontManager_getCode(*args)
    def getFont(*args): return _bpp_fontmanager.doubleFontManager_getFont(*args)
    def getCodes(*args): return _bpp_fontmanager.doubleFontManager_getCodes(*args)
    def getFonts(*args): return _bpp_fontmanager.doubleFontManager_getFonts(*args)
    def getNumberOfFonts(*args): return _bpp_fontmanager.doubleFontManager_getNumberOfFonts(*args)
doubleFontManager_swigregister = _bpp_fontmanager.doubleFontManager_swigregister
doubleFontManager_swigregister(doubleFontManager)

class charFontManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, charFontManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, charFontManager, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _bpp_fontmanager.delete_charFontManager
    __del__ = lambda self : None;
    def getCode(*args): return _bpp_fontmanager.charFontManager_getCode(*args)
    def getFont(*args): return _bpp_fontmanager.charFontManager_getFont(*args)
    def getCodes(*args): return _bpp_fontmanager.charFontManager_getCodes(*args)
    def getFonts(*args): return _bpp_fontmanager.charFontManager_getFonts(*args)
    def getNumberOfFonts(*args): return _bpp_fontmanager.charFontManager_getNumberOfFonts(*args)
charFontManager_swigregister = _bpp_fontmanager.charFontManager_swigregister
charFontManager_swigregister(charFontManager)

class XFigLaTeXFontManager(intFontManager):
    __swig_setmethods__ = {}
    for _s in [intFontManager]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, XFigLaTeXFontManager, name, value)
    __swig_getmethods__ = {}
    for _s in [intFontManager]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, XFigLaTeXFontManager, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_XFigLaTeXFontManager(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_XFigLaTeXFontManager
    __del__ = lambda self : None;
    def getCode(*args): return _bpp_fontmanager.XFigLaTeXFontManager_getCode(*args)
    def getFont(*args): return _bpp_fontmanager.XFigLaTeXFontManager_getFont(*args)
    def getCodes(*args): return _bpp_fontmanager.XFigLaTeXFontManager_getCodes(*args)
    def getFonts(*args): return _bpp_fontmanager.XFigLaTeXFontManager_getFonts(*args)
    def getNumberOfFonts(*args): return _bpp_fontmanager.XFigLaTeXFontManager_getNumberOfFonts(*args)
XFigLaTeXFontManager_swigregister = _bpp_fontmanager.XFigLaTeXFontManager_swigregister
XFigLaTeXFontManager_swigregister(XFigLaTeXFontManager)

class XFigPostscriptFontManager(intFontManager):
    __swig_setmethods__ = {}
    for _s in [intFontManager]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, XFigPostscriptFontManager, name, value)
    __swig_getmethods__ = {}
    for _s in [intFontManager]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, XFigPostscriptFontManager, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _bpp_fontmanager.new_XFigPostscriptFontManager(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bpp_fontmanager.delete_XFigPostscriptFontManager
    __del__ = lambda self : None;
    def getCode(*args): return _bpp_fontmanager.XFigPostscriptFontManager_getCode(*args)
    def getFont(*args): return _bpp_fontmanager.XFigPostscriptFontManager_getFont(*args)
    def getCodes(*args): return _bpp_fontmanager.XFigPostscriptFontManager_getCodes(*args)
    def getFonts(*args): return _bpp_fontmanager.XFigPostscriptFontManager_getFonts(*args)
    def getNumberOfFonts(*args): return _bpp_fontmanager.XFigPostscriptFontManager_getNumberOfFonts(*args)
XFigPostscriptFontManager_swigregister = _bpp_fontmanager.XFigPostscriptFontManager_swigregister
XFigPostscriptFontManager_swigregister(XFigPostscriptFontManager)


