__virtualname__ = "file"

def __virtual__():
    return __virtualname__

def touch_reg(name, atime=None, mtime=None, makedirs=False, registered={}):
    name = __context__[registered["name"]] if registered.get("name") else name
    atime = __context__[registered["atime"]] if registered.get("atime") else atime
    mtime = __context__[registered["makedirs"]] if registered.get("mtime") else mtime

    return __states__["file.touch"](name, atime=atime, mtime=mtime, makedirs=makedirs)

