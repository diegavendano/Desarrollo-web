class Rectangulo:
  def __init__(self,base,altura):
      self.base = base
      self.altura = altura
  def imprimir (self):
    print("base: " ,self.base,"\n" "altura: ",self.altura)
    return ("")
  def area (self):
    area=self.base*self.altura
    return area
bas=float(input("Ingrese la base del Rectangulo: "))
alt=float(input("Ingrese la altura del Rectangulo: "))
print()
rec=Rectangulo(bas,alt)
print(rec.imprimir())
print("el area del rectangulo es\n",rec.area())
print()
if bas == alt:
  print(True)
else:
  print(False)
