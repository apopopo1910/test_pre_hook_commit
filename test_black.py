import sys,os
import   math


def   compute(a,b):
      if(a>  10):
                   print("a est grand !")  
      else:
                print("a est petit")
      return   a+ b

class  Calculator:

            def __init__(self,value):
                       self.value=value


            def add(self,x):
                                return   self.value+  x

            def  multiply(self,x):
                                y=    self.value *     x
                                print(  "Resultat:",y);  return y


def very_long_function_name(arg1, arg2, arg3,arg4  , arg5   ):
    # Exemple de pb: ligne beaucoup trop longue qui devrait être automatiquement cassée et reformattée par Black
    print("Voici une ligne beaaaaaucoup trop longue qui ne respecte absolument pas les longueurs maximales recommandées par PEP8 et que Black doit corriger automatiquement quand le hook pre-commit sera déclenché:", arg1, arg2,arg3,arg4,arg5)
