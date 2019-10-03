#! /usr/bin/env python
# -*- coding: utf-8 -*-
def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
        return False
    return True