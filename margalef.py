#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:15:20 2022

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

from funcMargalef import margalef

n = int(input("Ingrese el número total de individuos: "))
s = int(input("Ingrese el número total de especies diferentes: "))

resultado = margalef(s,n)

if (resultado < 2):
    print(f"El índice de Margalef de individuos es: {resultado}")
    print("La región tiene biodiversidad baja")
elif (resultado > 2 and resultado < 5):
    print(f"El índice de Margalef de individuos es: {resultado}")
    print("La región tiene biodiversidad media")
else:
    print(f"El índice de Margalef de individuos es: {resultado}")
    print("La región tiene biodiversidad alta")