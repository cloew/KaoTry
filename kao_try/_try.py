from kao_decorators import proxy_for

class Try(object):
    """ A wrapper to allow checking if an attribute exists """
    tryVars = ["_toWrap"]
    
    def __init__(self, toWrap):
        """ Initialize with the item to wrap """
        self._toWrap = toWrap
        
    def __getattr__(self, name):
        """ Get the attr """
        return Try(getattr(self._toWrap, name)) if hasattr(self._toWrap, name) else Try(None)
            
    def done(self):
        """ Terminate the Try object and return the actual value """
        return self._toWrap