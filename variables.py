var_int=10
var_float=3.5
var_string="hola"
var_boolean= True
var_concatena=var_string+str(var_int)+str(var_float)+str(var_boolean)


""""
Alguna curiosidad es que los float no tienen precisión infinita. Podemos ver en el siguiente ejemplo como en realidad f se almacena como si fuera 1, ya que no es posible representar tanta precisión decimal.

f = 0.99999999999999999
print(f)      #1.0
print(1 == f) #True

Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar. La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308,
"""
n=20/2
suma_par=n*(n+1)

print(var_int)
print(var_float)
print(var_string)
print(var_boolean)
print(var_concatena)
print(suma_par)
