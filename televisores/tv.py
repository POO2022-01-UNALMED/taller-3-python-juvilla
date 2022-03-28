class TV:
    _numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        TV._numTV+=1
    def setMarca(self,marca):
        self._marca=marca
    def getMarca(self):
        return self._marca
    def setControl(self,control):
        self._control=control
    def getControl(self):
        return self._control
    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    def setVolumen(self,volumen):
        if 0<=volumen and volumen<=7 and self._estado==True:
            self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    def setCanal(self,canal):
        if 1<=canal and canal<=120 and self._estado==True:
            self._canal=canal
    def getCanal(self):
        return self._canal
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    @classmethod
    def setNumTV(cls,n):
        cls._numTV=n
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def getEstado(self):
        return self._estado
    def canalUp(self):
        if self._canal<120:
            self._canal+=1
    def canalDown(self):
        if self._canal>0:
            self._canal-=1
    def volumenUp(self):
        if self._volumen<7 and self._estado==True:
            self._volumen+=1
    def volumenDown(self):
        if self._volumen>0 and self._estado==True:
            self._volumen-=1