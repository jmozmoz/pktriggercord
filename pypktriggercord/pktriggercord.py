'''Wrapper for pktriggercord-servermode.h

Generated with:
/usr/bin/ctypesgen.py -l pktriggercord.so.0.84.03 pktriggercord-servermode.h pslr.h pslr_enum.h pslr_lens.h pslr_model.h pslr_scsi.h pktriggercord-servermode.h -o pktriggercord.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

# compatiblity patch from https://github.com/oxplot/fysom/issues/1
try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring
    
_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["pktriggercord.so.0.84.03"] = load_library("pktriggercord.so.0.84.03")

# 1 libraries
# End libraries

# No modules

enum_anon_1 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 36

PSLR_COLOR_SPACE_SRGB = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 36

PSLR_COLOR_SPACE_ADOBERGB = (PSLR_COLOR_SPACE_SRGB + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 36

PSLR_COLOR_SPACE_MAX = (PSLR_COLOR_SPACE_ADOBERGB + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 36

pslr_color_space_t = enum_anon_1 # /home/joachim/git/pktriggercord/pslr_enum.h: 36

enum_anon_2 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 44

PSLR_AF_MODE_MF = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 44

PSLR_AF_MODE_AF_S = (PSLR_AF_MODE_MF + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 44

PSLR_AF_MODE_AF_C = (PSLR_AF_MODE_AF_S + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 44

PSLR_AF_MODE_AF_A = (PSLR_AF_MODE_AF_C + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 44

PSLR_AF_MODE_MAX = (PSLR_AF_MODE_AF_A + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 44

pslr_af_mode_t = enum_anon_2 # /home/joachim/git/pktriggercord/pslr_enum.h: 44

enum_anon_3 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 51

PSLR_AE_METERING_MULTI = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 51

PSLR_AE_METERING_CENTER = (PSLR_AE_METERING_MULTI + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 51

PSLR_AE_METERING_SPOT = (PSLR_AE_METERING_CENTER + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 51

PSLR_AE_METERING_MAX = (PSLR_AE_METERING_SPOT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 51

pslr_ae_metering_t = enum_anon_3 # /home/joachim/git/pktriggercord/pslr_enum.h: 51

enum_anon_4 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_MANUAL = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_MANUAL_REDEYE = 1 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_SLOW = 2 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_SLOW_REDEYE = 3 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_TRAILING_CURTAIN = 4 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_AUTO = 5 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_AUTO_REDEYE = 6 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_WIRELESS = 8 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

PSLR_FLASH_MODE_MAX = 9 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

pslr_flash_mode_t = enum_anon_4 # /home/joachim/git/pktriggercord/pslr_enum.h: 64

enum_anon_5 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_SINGLE = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_CONTINUOUS_HI = (PSLR_DRIVE_MODE_SINGLE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_SELF_TIMER_12 = (PSLR_DRIVE_MODE_CONTINUOUS_HI + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_SELF_TIMER_2 = (PSLR_DRIVE_MODE_SELF_TIMER_12 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_REMOTE = (PSLR_DRIVE_MODE_SELF_TIMER_2 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_REMOTE_3 = (PSLR_DRIVE_MODE_REMOTE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_CONTINUOUS_LO = (PSLR_DRIVE_MODE_REMOTE_3 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

PSLR_DRIVE_MODE_MAX = (PSLR_DRIVE_MODE_CONTINUOUS_LO + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 75

pslr_drive_mode_t = enum_anon_5 # /home/joachim/git/pktriggercord/pslr_enum.h: 75

enum_anon_6 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 83

PSLR_AF_POINT_SEL_AUTO_5 = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 83

PSLR_AF_POINT_SEL_SELECT = (PSLR_AF_POINT_SEL_AUTO_5 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 83

PSLR_AF_POINT_SEL_SPOT = (PSLR_AF_POINT_SEL_SELECT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 83

PSLR_AF_POINT_SEL_AUTO_11 = (PSLR_AF_POINT_SEL_SPOT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 83

PSLR_AF_POINT_SEL_MAX = (PSLR_AF_POINT_SEL_AUTO_11 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 83

pslr_af_point_sel_t = enum_anon_6 # /home/joachim/git/pktriggercord/pslr_enum.h: 83

enum_anon_7 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_NONE = (-1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_NATURAL = (PSLR_JPEG_IMAGE_TONE_NONE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_BRIGHT = (PSLR_JPEG_IMAGE_TONE_NATURAL + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_PORTRAIT = (PSLR_JPEG_IMAGE_TONE_BRIGHT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_LANDSCAPE = (PSLR_JPEG_IMAGE_TONE_PORTRAIT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_VIBRANT = (PSLR_JPEG_IMAGE_TONE_LANDSCAPE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_MONOCHROME = (PSLR_JPEG_IMAGE_TONE_VIBRANT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_MUTED = (PSLR_JPEG_IMAGE_TONE_MONOCHROME + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_REVERSAL_FILM = (PSLR_JPEG_IMAGE_TONE_MUTED + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_BLEACH_BYPASS = (PSLR_JPEG_IMAGE_TONE_REVERSAL_FILM + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_RADIANT = (PSLR_JPEG_IMAGE_TONE_BLEACH_BYPASS + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

PSLR_JPEG_IMAGE_TONE_MAX = (PSLR_JPEG_IMAGE_TONE_RADIANT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 98

pslr_jpeg_image_tone_t = enum_anon_7 # /home/joachim/git/pktriggercord/pslr_enum.h: 98

enum_anon_8 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_AUTO = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_DAYLIGHT = (PSLR_WHITE_BALANCE_MODE_AUTO + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_SHADE = (PSLR_WHITE_BALANCE_MODE_DAYLIGHT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_CLOUDY = (PSLR_WHITE_BALANCE_MODE_SHADE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_FLUORESCENT_DAYLIGHT_COLOR = (PSLR_WHITE_BALANCE_MODE_CLOUDY + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_FLUORESCENT_DAYLIGHT_WHITE = (PSLR_WHITE_BALANCE_MODE_FLUORESCENT_DAYLIGHT_COLOR + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_FLUORESCENT_COOL_WHITE = (PSLR_WHITE_BALANCE_MODE_FLUORESCENT_DAYLIGHT_WHITE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_TUNGSTEN = (PSLR_WHITE_BALANCE_MODE_FLUORESCENT_COOL_WHITE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_FLASH = (PSLR_WHITE_BALANCE_MODE_TUNGSTEN + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_MANUAL = (PSLR_WHITE_BALANCE_MODE_FLASH + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_FLUORESCENT_WARM_WHITE = 15 # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_CTE = 16 # /home/joachim/git/pktriggercord/pslr_enum.h: 115

PSLR_WHITE_BALANCE_MODE_MAX = 17 # /home/joachim/git/pktriggercord/pslr_enum.h: 115

pslr_white_balance_mode_t = enum_anon_8 # /home/joachim/git/pktriggercord/pslr_enum.h: 115

enum_anon_9 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 121

PSLR_CUSTOM_EV_STEPS_1_2 = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 121

PSLR_CUSTOM_EV_STEPS_1_3 = (PSLR_CUSTOM_EV_STEPS_1_2 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 121

PSLR_CUSTOM_EV_STEPS_MAX = (PSLR_CUSTOM_EV_STEPS_1_3 + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 121

pslr_custom_ev_steps_t = enum_anon_9 # /home/joachim/git/pktriggercord/pslr_enum.h: 121

enum_anon_10 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 128

PSLR_IMAGE_FORMAT_JPEG = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 128

PSLR_IMAGE_FORMAT_RAW = (PSLR_IMAGE_FORMAT_JPEG + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 128

PSLR_IMAGE_FORMAT_RAW_PLUS = (PSLR_IMAGE_FORMAT_RAW + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 128

PSLR_IMAGE_FORMAT_MAX = (PSLR_IMAGE_FORMAT_RAW_PLUS + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 128

pslr_image_format_t = enum_anon_10 # /home/joachim/git/pktriggercord/pslr_enum.h: 128

enum_anon_11 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 134

PSLR_RAW_FORMAT_PEF = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 134

PSLR_RAW_FORMAT_DNG = (PSLR_RAW_FORMAT_PEF + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 134

PSLR_RAW_FORMAT_MAX = (PSLR_RAW_FORMAT_DNG + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 134

pslr_raw_format_t = enum_anon_11 # /home/joachim/git/pktriggercord/pslr_enum.h: 134

enum_anon_12 = c_int # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_NONE = 0 # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_HISPEED = (PSLR_EXPOSURE_SUBMODE_NONE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_DOF = (PSLR_EXPOSURE_SUBMODE_HISPEED + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_MTF = (PSLR_EXPOSURE_SUBMODE_DOF + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_STANDARD = (PSLR_EXPOSURE_SUBMODE_MTF + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_PORTRAIT = (PSLR_EXPOSURE_SUBMODE_STANDARD + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_LANDSCAPE = (PSLR_EXPOSURE_SUBMODE_PORTRAIT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_MACRO = (PSLR_EXPOSURE_SUBMODE_LANDSCAPE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_SPORT = (PSLR_EXPOSURE_SUBMODE_MACRO + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_NIGHTSCENEPORTRAIT = (PSLR_EXPOSURE_SUBMODE_SPORT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_NOFLASH = (PSLR_EXPOSURE_SUBMODE_NIGHTSCENEPORTRAIT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_NIGHTSCENE = (PSLR_EXPOSURE_SUBMODE_NOFLASH + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_SURFANDSNOW = (PSLR_EXPOSURE_SUBMODE_NIGHTSCENE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_TEXT = (PSLR_EXPOSURE_SUBMODE_SURFANDSNOW + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_SUNSET = (PSLR_EXPOSURE_SUBMODE_TEXT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_KIDS = (PSLR_EXPOSURE_SUBMODE_SUNSET + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_PET = (PSLR_EXPOSURE_SUBMODE_KIDS + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_CANDLELIGHT = (PSLR_EXPOSURE_SUBMODE_PET + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_MUSEUM = (PSLR_EXPOSURE_SUBMODE_CANDLELIGHT + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_FOOD = (PSLR_EXPOSURE_SUBMODE_MUSEUM + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_STAGE = (PSLR_EXPOSURE_SUBMODE_FOOD + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_NIGHTSNAP = (PSLR_EXPOSURE_SUBMODE_STAGE + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_SWALLOWDOF = (PSLR_EXPOSURE_SUBMODE_NIGHTSNAP + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

PSLR_EXPOSURE_SUBMODE_MAX = (PSLR_EXPOSURE_SUBMODE_SWALLOWDOF + 1) # /home/joachim/git/pktriggercord/pslr_enum.h: 161

pslr_exposure_submode_t = enum_anon_12 # /home/joachim/git/pktriggercord/pslr_enum.h: 161

# /home/joachim/git/pktriggercord/pslr_enum.h: 163
if hasattr(_libs['pktriggercord.so.0.84.03'], 'str_comparison_i'):
    str_comparison_i = _libs['pktriggercord.so.0.84.03'].str_comparison_i
    str_comparison_i.argtypes = [String, String, c_int]
    str_comparison_i.restype = c_int

# /home/joachim/git/pktriggercord/pslr_enum.h: 164
if hasattr(_libs['pktriggercord.so.0.84.03'], 'find_in_array'):
    find_in_array = _libs['pktriggercord.so.0.84.03'].find_in_array
    find_in_array.argtypes = [POINTER(POINTER(c_char)), c_int, String]
    find_in_array.restype = c_int

# /home/joachim/git/pktriggercord/pslr_enum.h: 166
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_color_space'):
    get_pslr_color_space = _libs['pktriggercord.so.0.84.03'].get_pslr_color_space
    get_pslr_color_space.argtypes = [String]
    get_pslr_color_space.restype = pslr_color_space_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 167
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_color_space_str'):
    get_pslr_color_space_str = _libs['pktriggercord.so.0.84.03'].get_pslr_color_space_str
    get_pslr_color_space_str.argtypes = [pslr_color_space_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_color_space_str.restype = ReturnString
    else:
        get_pslr_color_space_str.restype = String
        get_pslr_color_space_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 169
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_af_mode'):
    get_pslr_af_mode = _libs['pktriggercord.so.0.84.03'].get_pslr_af_mode
    get_pslr_af_mode.argtypes = [String]
    get_pslr_af_mode.restype = pslr_af_mode_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 170
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_af_mode_str'):
    get_pslr_af_mode_str = _libs['pktriggercord.so.0.84.03'].get_pslr_af_mode_str
    get_pslr_af_mode_str.argtypes = [pslr_af_mode_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_af_mode_str.restype = ReturnString
    else:
        get_pslr_af_mode_str.restype = String
        get_pslr_af_mode_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 172
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_ae_metering'):
    get_pslr_ae_metering = _libs['pktriggercord.so.0.84.03'].get_pslr_ae_metering
    get_pslr_ae_metering.argtypes = [String]
    get_pslr_ae_metering.restype = pslr_ae_metering_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 173
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_ae_metering_str'):
    get_pslr_ae_metering_str = _libs['pktriggercord.so.0.84.03'].get_pslr_ae_metering_str
    get_pslr_ae_metering_str.argtypes = [pslr_ae_metering_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_ae_metering_str.restype = ReturnString
    else:
        get_pslr_ae_metering_str.restype = String
        get_pslr_ae_metering_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 175
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_flash_mode'):
    get_pslr_flash_mode = _libs['pktriggercord.so.0.84.03'].get_pslr_flash_mode
    get_pslr_flash_mode.argtypes = [String]
    get_pslr_flash_mode.restype = pslr_flash_mode_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 176
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_flash_mode_str'):
    get_pslr_flash_mode_str = _libs['pktriggercord.so.0.84.03'].get_pslr_flash_mode_str
    get_pslr_flash_mode_str.argtypes = [pslr_flash_mode_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_flash_mode_str.restype = ReturnString
    else:
        get_pslr_flash_mode_str.restype = String
        get_pslr_flash_mode_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 178
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_drive_mode'):
    get_pslr_drive_mode = _libs['pktriggercord.so.0.84.03'].get_pslr_drive_mode
    get_pslr_drive_mode.argtypes = [String]
    get_pslr_drive_mode.restype = pslr_drive_mode_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 179
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_drive_mode_str'):
    get_pslr_drive_mode_str = _libs['pktriggercord.so.0.84.03'].get_pslr_drive_mode_str
    get_pslr_drive_mode_str.argtypes = [pslr_drive_mode_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_drive_mode_str.restype = ReturnString
    else:
        get_pslr_drive_mode_str.restype = String
        get_pslr_drive_mode_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 181
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_af_point_sel'):
    get_pslr_af_point_sel = _libs['pktriggercord.so.0.84.03'].get_pslr_af_point_sel
    get_pslr_af_point_sel.argtypes = [String]
    get_pslr_af_point_sel.restype = pslr_af_point_sel_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 182
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_af_point_sel_str'):
    get_pslr_af_point_sel_str = _libs['pktriggercord.so.0.84.03'].get_pslr_af_point_sel_str
    get_pslr_af_point_sel_str.argtypes = [pslr_af_point_sel_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_af_point_sel_str.restype = ReturnString
    else:
        get_pslr_af_point_sel_str.restype = String
        get_pslr_af_point_sel_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 184
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_jpeg_image_tone'):
    get_pslr_jpeg_image_tone = _libs['pktriggercord.so.0.84.03'].get_pslr_jpeg_image_tone
    get_pslr_jpeg_image_tone.argtypes = [String]
    get_pslr_jpeg_image_tone.restype = pslr_jpeg_image_tone_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 185
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_jpeg_image_tone_str'):
    get_pslr_jpeg_image_tone_str = _libs['pktriggercord.so.0.84.03'].get_pslr_jpeg_image_tone_str
    get_pslr_jpeg_image_tone_str.argtypes = [pslr_jpeg_image_tone_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_jpeg_image_tone_str.restype = ReturnString
    else:
        get_pslr_jpeg_image_tone_str.restype = String
        get_pslr_jpeg_image_tone_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 187
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_white_balance_mode'):
    get_pslr_white_balance_mode = _libs['pktriggercord.so.0.84.03'].get_pslr_white_balance_mode
    get_pslr_white_balance_mode.argtypes = [String]
    get_pslr_white_balance_mode.restype = pslr_white_balance_mode_t

# /home/joachim/git/pktriggercord/pslr_enum.h: 188
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_white_balance_mode_str'):
    get_pslr_white_balance_mode_str = _libs['pktriggercord.so.0.84.03'].get_pslr_white_balance_mode_str
    get_pslr_white_balance_mode_str.argtypes = [pslr_white_balance_mode_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_white_balance_mode_str.restype = ReturnString
    else:
        get_pslr_white_balance_mode_str.restype = String
        get_pslr_white_balance_mode_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 191
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_custom_ev_steps_str'):
    get_pslr_custom_ev_steps_str = _libs['pktriggercord.so.0.84.03'].get_pslr_custom_ev_steps_str
    get_pslr_custom_ev_steps_str.argtypes = [pslr_custom_ev_steps_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_custom_ev_steps_str.restype = ReturnString
    else:
        get_pslr_custom_ev_steps_str.restype = String
        get_pslr_custom_ev_steps_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 193
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_image_format_str'):
    get_pslr_image_format_str = _libs['pktriggercord.so.0.84.03'].get_pslr_image_format_str
    get_pslr_image_format_str.argtypes = [pslr_image_format_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_image_format_str.restype = ReturnString
    else:
        get_pslr_image_format_str.restype = String
        get_pslr_image_format_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 195
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_raw_format_str'):
    get_pslr_raw_format_str = _libs['pktriggercord.so.0.84.03'].get_pslr_raw_format_str
    get_pslr_raw_format_str.argtypes = [pslr_raw_format_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_raw_format_str.restype = ReturnString
    else:
        get_pslr_raw_format_str.restype = String
        get_pslr_raw_format_str.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_enum.h: 197
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_pslr_exposure_submode_str'):
    get_pslr_exposure_submode_str = _libs['pktriggercord.so.0.84.03'].get_pslr_exposure_submode_str
    get_pslr_exposure_submode_str.argtypes = [pslr_exposure_submode_t]
    if sizeof(c_int) == sizeof(c_void_p):
        get_pslr_exposure_submode_str.restype = ReturnString
    else:
        get_pslr_exposure_submode_str.restype = String
        get_pslr_exposure_submode_str.errcheck = ReturnString

uintptr_t = c_ulong # /usr/include/stdint.h: 122

# /home/joachim/git/pktriggercord/pslr_scsi.h: 35
try:
    debug = (c_uint8).in_dll(_libs['pktriggercord.so.0.84.03'], 'debug')
except:
    pass

# /home/joachim/git/pktriggercord/pslr_scsi.h: 36
if hasattr(_libs['pktriggercord.so.0.84.03'], 'write_debug'):
    _func = _libs['pktriggercord.so.0.84.03'].write_debug
    _restype = None
    _argtypes = [String]
    write_debug = _variadic_function(_func,_restype,_argtypes)

enum_anon_18 = c_int # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_OK = 0 # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_DEVICE_ERROR = (PSLR_OK + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_SCSI_ERROR = (PSLR_DEVICE_ERROR + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_COMMAND_ERROR = (PSLR_SCSI_ERROR + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_READ_ERROR = (PSLR_COMMAND_ERROR + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_NO_MEMORY = (PSLR_READ_ERROR + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_PARAM = (PSLR_NO_MEMORY + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

PSLR_ERROR_MAX = (PSLR_PARAM + 1) # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

pslr_result = enum_anon_18 # /home/joachim/git/pktriggercord/pslr_scsi.h: 54

# /home/joachim/git/pktriggercord/pslr_scsi.h: 56
if hasattr(_libs['pktriggercord.so.0.84.03'], 'scsi_read'):
    scsi_read = _libs['pktriggercord.so.0.84.03'].scsi_read
    scsi_read.argtypes = [c_int, POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32]
    scsi_read.restype = c_int

# /home/joachim/git/pktriggercord/pslr_scsi.h: 59
if hasattr(_libs['pktriggercord.so.0.84.03'], 'scsi_write'):
    scsi_write = _libs['pktriggercord.so.0.84.03'].scsi_write
    scsi_write.argtypes = [c_int, POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32]
    scsi_write.restype = c_int

# /home/joachim/git/pktriggercord/pslr_scsi.h: 62
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_drives'):
    get_drives = _libs['pktriggercord.so.0.84.03'].get_drives
    get_drives.argtypes = [POINTER(c_int)]
    get_drives.restype = POINTER(POINTER(c_char))

# /home/joachim/git/pktriggercord/pslr_scsi.h: 64
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_drive_info'):
    get_drive_info = _libs['pktriggercord.so.0.84.03'].get_drive_info
    get_drive_info.argtypes = [String, POINTER(c_int), String, c_int, String, c_int]
    get_drive_info.restype = pslr_result

# /home/joachim/git/pktriggercord/pslr_scsi.h: 68
if hasattr(_libs['pktriggercord.so.0.84.03'], 'close_drive'):
    close_drive = _libs['pktriggercord.so.0.84.03'].close_drive
    close_drive.argtypes = [POINTER(c_int)]
    close_drive.restype = None

# /home/joachim/git/pktriggercord/pslr_model.h: 136
class struct_ipslr_handle(Structure):
    pass

ipslr_handle_t = struct_ipslr_handle # /home/joachim/git/pktriggercord/pslr_model.h: 45

# /home/joachim/git/pktriggercord/pslr_model.h: 50
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'nom',
    'denom',
]
struct_anon_19._fields_ = [
    ('nom', c_int32),
    ('denom', c_int32),
]

pslr_rational_t = struct_anon_19 # /home/joachim/git/pktriggercord/pslr_model.h: 50

# /home/joachim/git/pktriggercord/pslr_model.h: 106
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'bufmask',
    'current_iso',
    'current_shutter_speed',
    'current_aperture',
    'lens_max_aperture',
    'lens_min_aperture',
    'set_shutter_speed',
    'set_aperture',
    'max_shutter_speed',
    'auto_bracket_mode',
    'auto_bracket_ev',
    'auto_bracket_picture_count',
    'fixed_iso',
    'jpeg_resolution',
    'jpeg_saturation',
    'jpeg_quality',
    'jpeg_contrast',
    'jpeg_sharpness',
    'jpeg_image_tone',
    'jpeg_hue',
    'zoom',
    'focus',
    'image_format',
    'raw_format',
    'light_meter_flags',
    'ec',
    'custom_ev_steps',
    'custom_sensitivity_steps',
    'exposure_mode',
    'exposure_submode',
    'user_mode_flag',
    'ae_metering_mode',
    'af_mode',
    'af_point_select',
    'selected_af_point',
    'focused_af_point',
    'auto_iso_min',
    'auto_iso_max',
    'drive_mode',
    'shake_reduction',
    'white_balance_mode',
    'white_balance_adjust_mg',
    'white_balance_adjust_ba',
    'flash_mode',
    'flash_exposure_compensation',
    'manual_mode_ev',
    'color_space',
    'lens_id1',
    'lens_id2',
    'battery_1',
    'battery_2',
    'battery_3',
    'battery_4',
]
struct_anon_20._fields_ = [
    ('bufmask', c_uint16),
    ('current_iso', c_uint32),
    ('current_shutter_speed', pslr_rational_t),
    ('current_aperture', pslr_rational_t),
    ('lens_max_aperture', pslr_rational_t),
    ('lens_min_aperture', pslr_rational_t),
    ('set_shutter_speed', pslr_rational_t),
    ('set_aperture', pslr_rational_t),
    ('max_shutter_speed', pslr_rational_t),
    ('auto_bracket_mode', c_uint32),
    ('auto_bracket_ev', pslr_rational_t),
    ('auto_bracket_picture_count', c_uint32),
    ('fixed_iso', c_uint32),
    ('jpeg_resolution', c_uint32),
    ('jpeg_saturation', c_uint32),
    ('jpeg_quality', c_uint32),
    ('jpeg_contrast', c_uint32),
    ('jpeg_sharpness', c_uint32),
    ('jpeg_image_tone', c_uint32),
    ('jpeg_hue', c_uint32),
    ('zoom', pslr_rational_t),
    ('focus', c_int32),
    ('image_format', c_uint32),
    ('raw_format', c_uint32),
    ('light_meter_flags', c_uint32),
    ('ec', pslr_rational_t),
    ('custom_ev_steps', c_uint32),
    ('custom_sensitivity_steps', c_uint32),
    ('exposure_mode', c_uint32),
    ('exposure_submode', c_uint32),
    ('user_mode_flag', c_uint32),
    ('ae_metering_mode', c_uint32),
    ('af_mode', c_uint32),
    ('af_point_select', c_uint32),
    ('selected_af_point', c_uint32),
    ('focused_af_point', c_uint32),
    ('auto_iso_min', c_uint32),
    ('auto_iso_max', c_uint32),
    ('drive_mode', c_uint32),
    ('shake_reduction', c_uint32),
    ('white_balance_mode', c_uint32),
    ('white_balance_adjust_mg', c_uint32),
    ('white_balance_adjust_ba', c_uint32),
    ('flash_mode', c_uint32),
    ('flash_exposure_compensation', c_int32),
    ('manual_mode_ev', c_int32),
    ('color_space', c_uint32),
    ('lens_id1', c_uint32),
    ('lens_id2', c_uint32),
    ('battery_1', c_uint32),
    ('battery_2', c_uint32),
    ('battery_3', c_uint32),
    ('battery_4', c_uint32),
]

pslr_status = struct_anon_20 # /home/joachim/git/pktriggercord/pslr_model.h: 106

ipslr_status_parse_t = CFUNCTYPE(UNCHECKED(None), POINTER(ipslr_handle_t), POINTER(pslr_status)) # /home/joachim/git/pktriggercord/pslr_model.h: 108

# /home/joachim/git/pktriggercord/pslr_model.h: 128
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'id',
    'name',
    'old_scsi_command',
    'need_exposure_mode_conversion',
    'is_little_endian',
    'buffer_size',
    'max_jpeg_stars',
    'jpeg_resolutions',
    'jpeg_property_levels',
    'fastest_shutter_speed',
    'base_iso_min',
    'base_iso_max',
    'extended_iso_min',
    'extended_iso_max',
    'max_supported_image_tone',
    'has_jpeg_hue',
    'parser_function',
]
struct_anon_21._fields_ = [
    ('id', c_uint32),
    ('name', String),
    ('old_scsi_command', c_uint8),
    ('need_exposure_mode_conversion', c_uint8),
    ('is_little_endian', c_uint8),
    ('buffer_size', c_int),
    ('max_jpeg_stars', c_int),
    ('jpeg_resolutions', c_int * 4),
    ('jpeg_property_levels', c_int),
    ('fastest_shutter_speed', c_int),
    ('base_iso_min', c_int),
    ('base_iso_max', c_int),
    ('extended_iso_min', c_int),
    ('extended_iso_max', c_int),
    ('max_supported_image_tone', pslr_jpeg_image_tone_t),
    ('has_jpeg_hue', c_uint8),
    ('parser_function', ipslr_status_parse_t),
]

ipslr_model_info_t = struct_anon_21 # /home/joachim/git/pktriggercord/pslr_model.h: 128

# /home/joachim/git/pktriggercord/pslr_model.h: 134
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'offset',
    'addr',
    'length',
]
struct_anon_22._fields_ = [
    ('offset', c_uint32),
    ('addr', c_uint32),
    ('length', c_uint32),
]

ipslr_segment_t = struct_anon_22 # /home/joachim/git/pktriggercord/pslr_model.h: 134

struct_ipslr_handle.__slots__ = [
    'fd',
    'status',
    'id',
    'model',
    'segments',
    'segment_count',
    'offset',
    'status_buffer',
]
struct_ipslr_handle._fields_ = [
    ('fd', c_int),
    ('status', pslr_status),
    ('id', c_uint32),
    ('model', POINTER(ipslr_model_info_t)),
    ('segments', ipslr_segment_t * 4),
    ('segment_count', c_uint32),
    ('offset', c_uint32),
    ('status_buffer', c_uint8 * 456),
]

# /home/joachim/git/pktriggercord/pslr_model.h: 147
if hasattr(_libs['pktriggercord.so.0.84.03'], 'find_model_by_id'):
    find_model_by_id = _libs['pktriggercord.so.0.84.03'].find_model_by_id
    find_model_by_id.argtypes = [c_uint32]
    find_model_by_id.restype = POINTER(ipslr_model_info_t)

# /home/joachim/git/pktriggercord/pslr_model.h: 149
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_hw_jpeg_quality'):
    get_hw_jpeg_quality = _libs['pktriggercord.so.0.84.03'].get_hw_jpeg_quality
    get_hw_jpeg_quality.argtypes = [POINTER(ipslr_model_info_t), c_int]
    get_hw_jpeg_quality.restype = c_int

# /home/joachim/git/pktriggercord/pslr_model.h: 151
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_uint32_be'):
    get_uint32_be = _libs['pktriggercord.so.0.84.03'].get_uint32_be
    get_uint32_be.argtypes = [POINTER(c_uint8)]
    get_uint32_be.restype = c_uint32

# /home/joachim/git/pktriggercord/pslr_model.h: 152
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_uint32_le'):
    get_uint32_le = _libs['pktriggercord.so.0.84.03'].get_uint32_le
    get_uint32_le.argtypes = [POINTER(c_uint8)]
    get_uint32_le.restype = c_uint32

# /home/joachim/git/pktriggercord/pslr_model.h: 153
if hasattr(_libs['pktriggercord.so.0.84.03'], 'set_uint32_be'):
    set_uint32_be = _libs['pktriggercord.so.0.84.03'].set_uint32_be
    set_uint32_be.argtypes = [c_uint32, POINTER(c_uint8)]
    set_uint32_be.restype = None

# /home/joachim/git/pktriggercord/pslr_model.h: 154
if hasattr(_libs['pktriggercord.so.0.84.03'], 'set_uint32_le'):
    set_uint32_le = _libs['pktriggercord.so.0.84.03'].set_uint32_le
    set_uint32_le.argtypes = [c_uint32, POINTER(c_uint8)]
    set_uint32_le.restype = None

get_uint32_func = CFUNCTYPE(UNCHECKED(c_uint32), POINTER(c_uint8)) # /home/joachim/git/pktriggercord/pslr_model.h: 156

get_uint16_func = CFUNCTYPE(UNCHECKED(c_uint16), POINTER(c_uint8)) # /home/joachim/git/pktriggercord/pslr_model.h: 157

get_int32_func = CFUNCTYPE(UNCHECKED(c_int32), POINTER(c_uint8)) # /home/joachim/git/pktriggercord/pslr_model.h: 158

# /home/joachim/git/pktriggercord/pslr_model.h: 160
if hasattr(_libs['pktriggercord.so.0.84.03'], 'hexdump'):
    hexdump = _libs['pktriggercord.so.0.84.03'].hexdump
    hexdump.argtypes = [POINTER(c_uint8), c_uint32]
    hexdump.restype = None

# /home/joachim/git/pktriggercord/pslr_model.h: 161
if hasattr(_libs['pktriggercord.so.0.84.03'], 'hexdump_debug'):
    hexdump_debug = _libs['pktriggercord.so.0.84.03'].hexdump_debug
    hexdump_debug.argtypes = [POINTER(c_uint8), c_uint32]
    hexdump_debug.restype = None

enum_anon_23 = c_int # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_PEF = 0 # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_DNG = (PSLR_BUF_PEF + 1) # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_JPEG_4 = (PSLR_BUF_DNG + 1) # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_JPEG_3 = (PSLR_BUF_JPEG_4 + 1) # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_JPEG_2 = (PSLR_BUF_JPEG_3 + 1) # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_JPEG_1 = (PSLR_BUF_JPEG_2 + 1) # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_PREVIEW = 8 # /home/joachim/git/pktriggercord/pslr.h: 66

PSLR_BUF_THUMBNAIL = 9 # /home/joachim/git/pktriggercord/pslr.h: 66

pslr_buffer_type = enum_anon_23 # /home/joachim/git/pktriggercord/pslr.h: 66

enum_anon_24 = c_int # /home/joachim/git/pktriggercord/pslr.h: 73

USER_FILE_FORMAT_PEF = 0 # /home/joachim/git/pktriggercord/pslr.h: 73

USER_FILE_FORMAT_DNG = (USER_FILE_FORMAT_PEF + 1) # /home/joachim/git/pktriggercord/pslr.h: 73

USER_FILE_FORMAT_JPEG = (USER_FILE_FORMAT_DNG + 1) # /home/joachim/git/pktriggercord/pslr.h: 73

USER_FILE_FORMAT_MAX = (USER_FILE_FORMAT_JPEG + 1) # /home/joachim/git/pktriggercord/pslr.h: 73

user_file_format = enum_anon_24 # /home/joachim/git/pktriggercord/pslr.h: 73

# /home/joachim/git/pktriggercord/pslr.h: 79
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'uff',
    'file_format_name',
    'extension',
]
struct_anon_25._fields_ = [
    ('uff', user_file_format),
    ('file_format_name', String),
    ('extension', String),
]

user_file_format_t = struct_anon_25 # /home/joachim/git/pktriggercord/pslr.h: 79

# /home/joachim/git/pktriggercord/pslr.h: 81
try:
    file_formats = (user_file_format_t * 3).in_dll(_libs['pktriggercord.so.0.84.03'], 'file_formats')
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 83
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_file_format_t'):
    get_file_format_t = _libs['pktriggercord.so.0.84.03'].get_file_format_t
    get_file_format_t.argtypes = [user_file_format]
    get_file_format_t.restype = POINTER(user_file_format_t)

enum_anon_26 = c_int # /home/joachim/git/pktriggercord/pslr.h: 89

PSLR_CUSTOM_SENSITIVITY_STEPS_1EV = 0 # /home/joachim/git/pktriggercord/pslr.h: 89

PSLR_CUSTOM_SENSITIVITY_STEPS_AS_EV = (PSLR_CUSTOM_SENSITIVITY_STEPS_1EV + 1) # /home/joachim/git/pktriggercord/pslr.h: 89

PSLR_CUSTOM_SENSITIVITY_STEPS_MAX = (PSLR_CUSTOM_SENSITIVITY_STEPS_AS_EV + 1) # /home/joachim/git/pktriggercord/pslr.h: 89

pslr_custom_sensitivity_steps_t = enum_anon_26 # /home/joachim/git/pktriggercord/pslr.h: 89

enum_anon_27 = c_int # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_P = 0 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_GREEN = 1 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_TV = 4 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_AV = 5 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_M = 8 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_B = 9 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_AV_OFFAUTO = 10 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_M_OFFAUTO = 11 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_B_OFFAUTO = 12 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_TAV = 13 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_SV = 15 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_X = 16 # /home/joachim/git/pktriggercord/pslr.h: 111

PSLR_EXPOSURE_MODE_MAX = 17 # /home/joachim/git/pktriggercord/pslr.h: 111

pslr_exposure_mode_t = enum_anon_27 # /home/joachim/git/pktriggercord/pslr.h: 111

enum_anon_28 = c_int # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_GREEN = 0 # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_P = (PSLR_GUI_EXPOSURE_MODE_GREEN + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_SV = (PSLR_GUI_EXPOSURE_MODE_P + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_TV = (PSLR_GUI_EXPOSURE_MODE_SV + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_AV = (PSLR_GUI_EXPOSURE_MODE_TV + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_TAV = (PSLR_GUI_EXPOSURE_MODE_AV + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_M = (PSLR_GUI_EXPOSURE_MODE_TAV + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_B = (PSLR_GUI_EXPOSURE_MODE_M + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_X = (PSLR_GUI_EXPOSURE_MODE_B + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

PSLR_GUI_EXPOSURE_MODE_MAX = (PSLR_GUI_EXPOSURE_MODE_X + 1) # /home/joachim/git/pktriggercord/pslr.h: 124

pslr_gui_exposure_mode_t = enum_anon_28 # /home/joachim/git/pktriggercord/pslr.h: 124

class pslr_handle_t(c_void_p):
    pass

#pslr_handle_t = POINTER(None) # /home/joachim/git/pktriggercord/pslr.h: 126

# /home/joachim/git/pktriggercord/pslr.h: 133
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'a',
    'b',
    'addr',
    'length',
]
struct_anon_29._fields_ = [
    ('a', c_uint32),
    ('b', c_uint32),
    ('addr', c_uint32),
    ('length', c_uint32),
]

pslr_buffer_segment_info = struct_anon_29 # /home/joachim/git/pktriggercord/pslr.h: 133

pslr_progress_callback_t = CFUNCTYPE(UNCHECKED(None), c_uint32, c_uint32) # /home/joachim/git/pktriggercord/pslr.h: 135

# /home/joachim/git/pktriggercord/pslr.h: 137
if hasattr(_libs['pktriggercord.so.0.84.03'], 'sleep_sec'):
    sleep_sec = _libs['pktriggercord.so.0.84.03'].sleep_sec
    sleep_sec.argtypes = [c_double]
    sleep_sec.restype = None

# /home/joachim/git/pktriggercord/pslr.h: 139
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_init'):
    pslr_init = _libs['pktriggercord.so.0.84.03'].pslr_init
    pslr_init.argtypes = [String, String]
    pslr_init.restype = pslr_handle_t

# /home/joachim/git/pktriggercord/pslr.h: 140
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_connect'):
    pslr_connect = _libs['pktriggercord.so.0.84.03'].pslr_connect
    pslr_connect.argtypes = [pslr_handle_t]
    pslr_connect.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 141
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_disconnect'):
    pslr_disconnect = _libs['pktriggercord.so.0.84.03'].pslr_disconnect
    pslr_disconnect.argtypes = [pslr_handle_t]
    pslr_disconnect.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 142
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_shutdown'):
    pslr_shutdown = _libs['pktriggercord.so.0.84.03'].pslr_shutdown
    pslr_shutdown.argtypes = [pslr_handle_t]
    pslr_shutdown.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 143
for _lib in _libs.items():
    if not hasattr(_lib, 'pslr_model'):
        continue
    pslr_model = _lib.pslr_model
    pslr_model.argtypes = [c_uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        pslr_model.restype = ReturnString
    else:
        pslr_model.restype = String
        pslr_model.errcheck = ReturnString
    break

# /home/joachim/git/pktriggercord/pslr.h: 145
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_shutter'):
    pslr_shutter = _libs['pktriggercord.so.0.84.03'].pslr_shutter
    pslr_shutter.argtypes = [pslr_handle_t]
    pslr_shutter.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 146
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_focus'):
    pslr_focus = _libs['pktriggercord.so.0.84.03'].pslr_focus
    pslr_focus.argtypes = [pslr_handle_t]
    pslr_focus.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 148
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_status'):
    pslr_get_status = _libs['pktriggercord.so.0.84.03'].pslr_get_status
    pslr_get_status.argtypes = [pslr_handle_t, POINTER(pslr_status)]
    pslr_get_status.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 149
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_status_buffer'):
    pslr_get_status_buffer = _libs['pktriggercord.so.0.84.03'].pslr_get_status_buffer
    pslr_get_status_buffer.argtypes = [pslr_handle_t, POINTER(c_uint8)]
    pslr_get_status_buffer.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 151
if hasattr(_libs['pktriggercord.so.0.84.03'], 'collect_status_info'):
    collect_status_info = _libs['pktriggercord.so.0.84.03'].collect_status_info
    collect_status_info.argtypes = [pslr_handle_t, pslr_status]
    if sizeof(c_int) == sizeof(c_void_p):
        collect_status_info.restype = ReturnString
    else:
        collect_status_info.restype = String
        collect_status_info.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr.h: 153
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_buffer'):
    pslr_get_buffer = _libs['pktriggercord.so.0.84.03'].pslr_get_buffer
    pslr_get_buffer.argtypes = [pslr_handle_t, c_int, pslr_buffer_type, c_int, POINTER(POINTER(c_uint8)), POINTER(c_uint32)]
    pslr_get_buffer.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 156
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_progress_callback'):
    pslr_set_progress_callback = _libs['pktriggercord.so.0.84.03'].pslr_set_progress_callback
    pslr_set_progress_callback.argtypes = [pslr_handle_t, pslr_progress_callback_t, uintptr_t]
    pslr_set_progress_callback.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 159
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_shutter'):
    pslr_set_shutter = _libs['pktriggercord.so.0.84.03'].pslr_set_shutter
    pslr_set_shutter.argtypes = [pslr_handle_t, pslr_rational_t]
    pslr_set_shutter.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 160
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_aperture'):
    pslr_set_aperture = _libs['pktriggercord.so.0.84.03'].pslr_set_aperture
    pslr_set_aperture.argtypes = [pslr_handle_t, pslr_rational_t]
    pslr_set_aperture.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 161
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_iso'):
    pslr_set_iso = _libs['pktriggercord.so.0.84.03'].pslr_set_iso
    pslr_set_iso.argtypes = [pslr_handle_t, c_uint32, c_uint32, c_uint32]
    pslr_set_iso.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 162
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_ec'):
    pslr_set_ec = _libs['pktriggercord.so.0.84.03'].pslr_set_ec
    pslr_set_ec.argtypes = [pslr_handle_t, pslr_rational_t]
    pslr_set_ec.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 164
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_white_balance'):
    pslr_set_white_balance = _libs['pktriggercord.so.0.84.03'].pslr_set_white_balance
    pslr_set_white_balance.argtypes = [pslr_handle_t, pslr_white_balance_mode_t]
    pslr_set_white_balance.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 165
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_white_balance_adjustment'):
    pslr_set_white_balance_adjustment = _libs['pktriggercord.so.0.84.03'].pslr_set_white_balance_adjustment
    pslr_set_white_balance_adjustment.argtypes = [pslr_handle_t, pslr_white_balance_mode_t, c_uint32, c_uint32]
    pslr_set_white_balance_adjustment.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 166
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_flash_mode'):
    pslr_set_flash_mode = _libs['pktriggercord.so.0.84.03'].pslr_set_flash_mode
    pslr_set_flash_mode.argtypes = [pslr_handle_t, pslr_flash_mode_t]
    pslr_set_flash_mode.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 167
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_flash_exposure_compensation'):
    pslr_set_flash_exposure_compensation = _libs['pktriggercord.so.0.84.03'].pslr_set_flash_exposure_compensation
    pslr_set_flash_exposure_compensation.argtypes = [pslr_handle_t, pslr_rational_t]
    pslr_set_flash_exposure_compensation.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 168
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_drive_mode'):
    pslr_set_drive_mode = _libs['pktriggercord.so.0.84.03'].pslr_set_drive_mode
    pslr_set_drive_mode.argtypes = [pslr_handle_t, pslr_drive_mode_t]
    pslr_set_drive_mode.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 169
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_af_mode'):
    pslr_set_af_mode = _libs['pktriggercord.so.0.84.03'].pslr_set_af_mode
    pslr_set_af_mode.argtypes = [pslr_handle_t, pslr_af_mode_t]
    pslr_set_af_mode.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 170
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_af_point_sel'):
    pslr_set_af_point_sel = _libs['pktriggercord.so.0.84.03'].pslr_set_af_point_sel
    pslr_set_af_point_sel.argtypes = [pslr_handle_t, pslr_af_point_sel_t]
    pslr_set_af_point_sel.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 171
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_ae_metering_mode'):
    pslr_set_ae_metering_mode = _libs['pktriggercord.so.0.84.03'].pslr_set_ae_metering_mode
    pslr_set_ae_metering_mode.argtypes = [pslr_handle_t, pslr_ae_metering_t]
    pslr_set_ae_metering_mode.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 172
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_color_space'):
    pslr_set_color_space = _libs['pktriggercord.so.0.84.03'].pslr_set_color_space
    pslr_set_color_space.argtypes = [pslr_handle_t, pslr_color_space_t]
    pslr_set_color_space.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 174
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_stars'):
    pslr_set_jpeg_stars = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_stars
    pslr_set_jpeg_stars.argtypes = [pslr_handle_t, c_int]
    pslr_set_jpeg_stars.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 175
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_resolution'):
    pslr_set_jpeg_resolution = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_resolution
    pslr_set_jpeg_resolution.argtypes = [pslr_handle_t, c_int]
    pslr_set_jpeg_resolution.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 176
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_image_tone'):
    pslr_set_jpeg_image_tone = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_image_tone
    pslr_set_jpeg_image_tone.argtypes = [pslr_handle_t, pslr_jpeg_image_tone_t]
    pslr_set_jpeg_image_tone.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 178
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_sharpness'):
    pslr_set_jpeg_sharpness = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_sharpness
    pslr_set_jpeg_sharpness.argtypes = [pslr_handle_t, c_int32]
    pslr_set_jpeg_sharpness.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 179
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_contrast'):
    pslr_set_jpeg_contrast = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_contrast
    pslr_set_jpeg_contrast.argtypes = [pslr_handle_t, c_int32]
    pslr_set_jpeg_contrast.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 180
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_saturation'):
    pslr_set_jpeg_saturation = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_saturation
    pslr_set_jpeg_saturation.argtypes = [pslr_handle_t, c_int32]
    pslr_set_jpeg_saturation.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 181
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_jpeg_hue'):
    pslr_set_jpeg_hue = _libs['pktriggercord.so.0.84.03'].pslr_set_jpeg_hue
    pslr_set_jpeg_hue.argtypes = [pslr_handle_t, c_int32]
    pslr_set_jpeg_hue.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 183
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_image_format'):
    pslr_set_image_format = _libs['pktriggercord.so.0.84.03'].pslr_set_image_format
    pslr_set_image_format.argtypes = [pslr_handle_t, pslr_image_format_t]
    pslr_set_image_format.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 184
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_raw_format'):
    pslr_set_raw_format = _libs['pktriggercord.so.0.84.03'].pslr_set_raw_format
    pslr_set_raw_format.argtypes = [pslr_handle_t, pslr_raw_format_t]
    pslr_set_raw_format.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 185
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_user_file_format'):
    pslr_set_user_file_format = _libs['pktriggercord.so.0.84.03'].pslr_set_user_file_format
    pslr_set_user_file_format.argtypes = [pslr_handle_t, user_file_format]
    pslr_set_user_file_format.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 186
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_user_file_format'):
    get_user_file_format = _libs['pktriggercord.so.0.84.03'].get_user_file_format
    get_user_file_format.argtypes = [POINTER(pslr_status)]
    get_user_file_format.restype = user_file_format

# /home/joachim/git/pktriggercord/pslr.h: 188
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_delete_buffer'):
    pslr_delete_buffer = _libs['pktriggercord.so.0.84.03'].pslr_delete_buffer
    pslr_delete_buffer.argtypes = [pslr_handle_t, c_int]
    pslr_delete_buffer.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 190
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_green_button'):
    pslr_green_button = _libs['pktriggercord.so.0.84.03'].pslr_green_button
    pslr_green_button.argtypes = [pslr_handle_t]
    pslr_green_button.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 192
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_button_test'):
    pslr_button_test = _libs['pktriggercord.so.0.84.03'].pslr_button_test
    pslr_button_test.argtypes = [pslr_handle_t, c_int, c_int]
    pslr_button_test.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 194
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_ae_lock'):
    pslr_ae_lock = _libs['pktriggercord.so.0.84.03'].pslr_ae_lock
    pslr_ae_lock.argtypes = [pslr_handle_t, c_uint8]
    pslr_ae_lock.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 196
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_dust_removal'):
    pslr_dust_removal = _libs['pktriggercord.so.0.84.03'].pslr_dust_removal
    pslr_dust_removal.argtypes = [pslr_handle_t]
    pslr_dust_removal.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 198
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_bulb'):
    pslr_bulb = _libs['pktriggercord.so.0.84.03'].pslr_bulb
    pslr_bulb.argtypes = [pslr_handle_t, c_uint8]
    pslr_bulb.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 200
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_buffer_open'):
    pslr_buffer_open = _libs['pktriggercord.so.0.84.03'].pslr_buffer_open
    pslr_buffer_open.argtypes = [pslr_handle_t, c_int, pslr_buffer_type, c_int]
    pslr_buffer_open.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 201
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_buffer_read'):
    pslr_buffer_read = _libs['pktriggercord.so.0.84.03'].pslr_buffer_read
    pslr_buffer_read.argtypes = [pslr_handle_t, POINTER(c_uint8), c_uint32]
    pslr_buffer_read.restype = c_uint32

# /home/joachim/git/pktriggercord/pslr.h: 202
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_buffer_close'):
    pslr_buffer_close = _libs['pktriggercord.so.0.84.03'].pslr_buffer_close
    pslr_buffer_close.argtypes = [pslr_handle_t]
    pslr_buffer_close.restype = None

# /home/joachim/git/pktriggercord/pslr.h: 203
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_buffer_get_size'):
    pslr_buffer_get_size = _libs['pktriggercord.so.0.84.03'].pslr_buffer_get_size
    pslr_buffer_get_size.argtypes = [pslr_handle_t]
    pslr_buffer_get_size.restype = c_uint32

# /home/joachim/git/pktriggercord/pslr.h: 205
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_set_exposure_mode'):
    pslr_set_exposure_mode = _libs['pktriggercord.so.0.84.03'].pslr_set_exposure_mode
    pslr_set_exposure_mode.argtypes = [pslr_handle_t, pslr_exposure_mode_t]
    pslr_set_exposure_mode.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 206
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_select_af_point'):
    pslr_select_af_point = _libs['pktriggercord.so.0.84.03'].pslr_select_af_point
    pslr_select_af_point.argtypes = [pslr_handle_t, c_uint32]
    pslr_select_af_point.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 208
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_camera_name'):
    pslr_camera_name = _libs['pktriggercord.so.0.84.03'].pslr_camera_name
    pslr_camera_name.argtypes = [pslr_handle_t]
    if sizeof(c_int) == sizeof(c_void_p):
        pslr_camera_name.restype = ReturnString
    else:
        pslr_camera_name.restype = String
        pslr_camera_name.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr.h: 209
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_max_jpeg_stars'):
    pslr_get_model_max_jpeg_stars = _libs['pktriggercord.so.0.84.03'].pslr_get_model_max_jpeg_stars
    pslr_get_model_max_jpeg_stars.argtypes = [pslr_handle_t]
    pslr_get_model_max_jpeg_stars.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 210
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_jpeg_property_levels'):
    pslr_get_model_jpeg_property_levels = _libs['pktriggercord.so.0.84.03'].pslr_get_model_jpeg_property_levels
    pslr_get_model_jpeg_property_levels.argtypes = [pslr_handle_t]
    pslr_get_model_jpeg_property_levels.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 211
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_buffer_size'):
    pslr_get_model_buffer_size = _libs['pktriggercord.so.0.84.03'].pslr_get_model_buffer_size
    pslr_get_model_buffer_size.argtypes = [pslr_handle_t]
    pslr_get_model_buffer_size.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 212
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_fastest_shutter_speed'):
    pslr_get_model_fastest_shutter_speed = _libs['pktriggercord.so.0.84.03'].pslr_get_model_fastest_shutter_speed
    pslr_get_model_fastest_shutter_speed.argtypes = [pslr_handle_t]
    pslr_get_model_fastest_shutter_speed.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 213
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_base_iso_min'):
    pslr_get_model_base_iso_min = _libs['pktriggercord.so.0.84.03'].pslr_get_model_base_iso_min
    pslr_get_model_base_iso_min.argtypes = [pslr_handle_t]
    pslr_get_model_base_iso_min.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 214
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_base_iso_max'):
    pslr_get_model_base_iso_max = _libs['pktriggercord.so.0.84.03'].pslr_get_model_base_iso_max
    pslr_get_model_base_iso_max.argtypes = [pslr_handle_t]
    pslr_get_model_base_iso_max.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 215
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_extended_iso_min'):
    pslr_get_model_extended_iso_min = _libs['pktriggercord.so.0.84.03'].pslr_get_model_extended_iso_min
    pslr_get_model_extended_iso_min.argtypes = [pslr_handle_t]
    pslr_get_model_extended_iso_min.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 216
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_extended_iso_max'):
    pslr_get_model_extended_iso_max = _libs['pktriggercord.so.0.84.03'].pslr_get_model_extended_iso_max
    pslr_get_model_extended_iso_max.argtypes = [pslr_handle_t]
    pslr_get_model_extended_iso_max.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 217
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_jpeg_resolutions'):
    pslr_get_model_jpeg_resolutions = _libs['pktriggercord.so.0.84.03'].pslr_get_model_jpeg_resolutions
    pslr_get_model_jpeg_resolutions.argtypes = [pslr_handle_t]
    pslr_get_model_jpeg_resolutions.restype = POINTER(c_int)

# /home/joachim/git/pktriggercord/pslr.h: 218
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_only_limited'):
    pslr_get_model_only_limited = _libs['pktriggercord.so.0.84.03'].pslr_get_model_only_limited
    pslr_get_model_only_limited.argtypes = [pslr_handle_t]
    pslr_get_model_only_limited.restype = c_uint8

# /home/joachim/git/pktriggercord/pslr.h: 219
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_has_jpeg_hue'):
    pslr_get_model_has_jpeg_hue = _libs['pktriggercord.so.0.84.03'].pslr_get_model_has_jpeg_hue
    pslr_get_model_has_jpeg_hue.argtypes = [pslr_handle_t]
    pslr_get_model_has_jpeg_hue.restype = c_uint8

# /home/joachim/git/pktriggercord/pslr.h: 220
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_need_exposure_conversion'):
    pslr_get_model_need_exposure_conversion = _libs['pktriggercord.so.0.84.03'].pslr_get_model_need_exposure_conversion
    pslr_get_model_need_exposure_conversion.argtypes = [pslr_handle_t]
    pslr_get_model_need_exposure_conversion.restype = c_uint8

# /home/joachim/git/pktriggercord/pslr.h: 221
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_model_max_supported_image_tone'):
    pslr_get_model_max_supported_image_tone = _libs['pktriggercord.so.0.84.03'].pslr_get_model_max_supported_image_tone
    pslr_get_model_max_supported_image_tone.argtypes = [pslr_handle_t]
    pslr_get_model_max_supported_image_tone.restype = pslr_jpeg_image_tone_t

# /home/joachim/git/pktriggercord/pslr.h: 223
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_jpeg_buffer_type'):
    pslr_get_jpeg_buffer_type = _libs['pktriggercord.so.0.84.03'].pslr_get_jpeg_buffer_type
    pslr_get_jpeg_buffer_type.argtypes = [pslr_handle_t, c_int]
    pslr_get_jpeg_buffer_type.restype = pslr_buffer_type

# /home/joachim/git/pktriggercord/pslr.h: 224
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_get_jpeg_resolution'):
    pslr_get_jpeg_resolution = _libs['pktriggercord.so.0.84.03'].pslr_get_jpeg_resolution
    pslr_get_jpeg_resolution.argtypes = [pslr_handle_t, c_int]
    pslr_get_jpeg_resolution.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 226
if hasattr(_libs['pktriggercord.so.0.84.03'], 'exposure_mode_conversion'):
    exposure_mode_conversion = _libs['pktriggercord.so.0.84.03'].exposure_mode_conversion
    exposure_mode_conversion.argtypes = [pslr_exposure_mode_t]
    exposure_mode_conversion.restype = pslr_gui_exposure_mode_t

# /home/joachim/git/pktriggercord/pslr.h: 227
if hasattr(_libs['pktriggercord.so.0.84.03'], 'format_rational'):
    format_rational = _libs['pktriggercord.so.0.84.03'].format_rational
    format_rational.argtypes = [pslr_rational_t, String]
    if sizeof(c_int) == sizeof(c_void_p):
        format_rational.restype = ReturnString
    else:
        format_rational.restype = String
        format_rational.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr.h: 229
if hasattr(_libs['pktriggercord.so.0.84.03'], 'pslr_test'):
    pslr_test = _libs['pktriggercord.so.0.84.03'].pslr_test
    pslr_test.argtypes = [pslr_handle_t, c_uint8, c_int, c_int, c_int, c_int, c_int, c_int]
    pslr_test.restype = c_int

# /home/joachim/git/pktriggercord/pslr.h: 231
if hasattr(_libs['pktriggercord.so.0.84.03'], 'copyright'):
    copyright = _libs['pktriggercord.so.0.84.03'].copyright
    copyright.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        copyright.restype = ReturnString
    else:
        copyright.restype = String
        copyright.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr.h: 233
if hasattr(_libs['pktriggercord.so.0.84.03'], 'write_debug'):
    _func = _libs['pktriggercord.so.0.84.03'].write_debug
    _restype = None
    _argtypes = [String]
    write_debug = _variadic_function(_func,_restype,_argtypes)

# /home/joachim/git/pktriggercord/pslr.h: 235
if hasattr(_libs['pktriggercord.so.0.84.03'], 'debug_onoff'):
    debug_onoff = _libs['pktriggercord.so.0.84.03'].debug_onoff
    debug_onoff.argtypes = [POINTER(ipslr_handle_t), c_char]
    debug_onoff.restype = c_int

# /home/joachim/git/pktriggercord/pktriggercord-servermode.h: 34
if hasattr(_libs['pktriggercord.so.0.84.03'], 'servermode_socket'):
    servermode_socket = _libs['pktriggercord.so.0.84.03'].servermode_socket
    servermode_socket.argtypes = []
    servermode_socket.restype = c_int

# /home/joachim/git/pktriggercord/pktriggercord-servermode.h: 36
if hasattr(_libs['pktriggercord.so.0.84.03'], 'camera_connect'):
    camera_connect = _libs['pktriggercord.so.0.84.03'].camera_connect
    camera_connect.argtypes = [String, String, c_int, String]
    camera_connect.restype = pslr_handle_t

# /home/joachim/git/pktriggercord/pktriggercord-servermode.h: 38
if hasattr(_libs['pktriggercord.so.0.84.03'], 'camera_close'):
    camera_close = _libs['pktriggercord.so.0.84.03'].camera_close
    camera_close.argtypes = [pslr_handle_t]
    camera_close.restype = None

# /home/joachim/git/pktriggercord/pktriggercord-servermode.h: 40
class struct_timeval(Structure):
    pass

# /home/joachim/git/pktriggercord/pktriggercord-servermode.h: 40
if hasattr(_libs['pktriggercord.so.0.84.03'], 'timeval_diff'):
    timeval_diff = _libs['pktriggercord.so.0.84.03'].timeval_diff
    timeval_diff.argtypes = [POINTER(struct_timeval), POINTER(struct_timeval)]
    timeval_diff.restype = c_long

# /home/joachim/git/pktriggercord/pslr_lens.h: 33
if hasattr(_libs['pktriggercord.so.0.84.03'], 'get_lens_name'):
    get_lens_name = _libs['pktriggercord.so.0.84.03'].get_lens_name
    get_lens_name.argtypes = [c_uint32, c_uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        get_lens_name.restype = ReturnString
    else:
        get_lens_name.restype = String
        get_lens_name.errcheck = ReturnString

# /home/joachim/git/pktriggercord/pslr_model.h: 41
try:
    MAX_RESOLUTION_SIZE = 4
except:
    pass

# /home/joachim/git/pktriggercord/pslr_model.h: 42
try:
    MAX_STATUS_BUF_SIZE = 456
except:
    pass

# /home/joachim/git/pktriggercord/pslr_model.h: 43
try:
    MAX_SEGMENTS = 4
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 43
try:
    PSLR_LIGHT_METER_AE_LOCK = 8
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 45
try:
    PSLR_AF_POINT_TOP_LEFT = 1
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 46
try:
    PSLR_AF_POINT_TOP_MID = 2
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 47
try:
    PSLR_AF_POINT_TOP_RIGHT = 4
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 48
try:
    PSLR_AF_POINT_FAR_LEFT = 8
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 49
try:
    PSLR_AF_POINT_MID_LEFT = 16
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 50
try:
    PSLR_AF_POINT_MID_MID = 32
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 51
try:
    PSLR_AF_POINT_MID_RIGHT = 64
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 52
try:
    PSLR_AF_POINT_FAR_RIGHT = 128
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 53
try:
    PSLR_AF_POINT_BOT_LEFT = 256
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 54
try:
    PSLR_AF_POINT_BOT_MID = 512
except:
    pass

# /home/joachim/git/pktriggercord/pslr.h: 55
try:
    PSLR_AF_POINT_BOT_RIGHT = 1024
except:
    pass

ipslr_handle = struct_ipslr_handle # /home/joachim/git/pktriggercord/pslr_model.h: 136

timeval = struct_timeval # /home/joachim/git/pktriggercord/pktriggercord-servermode.h: 40

# No inserted files

