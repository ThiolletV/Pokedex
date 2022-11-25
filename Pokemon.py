#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:11:04 2022

@author: vthiollet
"""
import sqlite3 as sq


class Pokemon:
    
    def __init__(self, name):
        self.name = name
        requete = "SELECT * FROM pokemon WHERE name = '{}' ;" .format(name)
        connexion = sq.connect('Pokemon.db')
        liste = connexion.execute(requete)
        for tup in liste:
            if tup[1] != 'Null':
                self.nom = tup[1]
            self.pv = tup[2]
            self.attaque = tup[3]
            self.defense = tup[4]
            self.attaque_speciale = tup[5]
            self.defense_speciale = tup[6]
            self.vitesse = tup[7]
            self.description = tup[8] 
            self.id_img = tup[9]
        connexion.close()
        
    def get_name(self):
        return self.name
    
    def get_nom(self):
        return self.nom
    
    def get_pv(self):
        return self.pv
    
    def get_attaque(self):
        return self.attaque
    
    def get_defense(self):
        return self.defense
        
    def get_attaque_speciale(self):
        return self.attaque_speciale
    
    def get_defense_speciale(self):
        return self.defense_speciale
        
    def get_vitesse(self):
        return self.vitesse
    
    def get_description(self):
        return self.description
    
        
    def get_id_img(self):
        return self.id_img
        
    def __str__(self):
        return self.name
    
    def ascendant(self):
        requete = "SELECT asc_name FROM evolutionDe WHERE desc_name = '{}' ;" .format(self)   
        connexion = sq.connect('Pokemon.db')
        asc = connexion.execute(requete)
        for tup in asc:
            if tup != 'Null':
                return tup
        connexion.close()
    
    def descendant(self):
        liste = []
        requete = "SELECT desc_name FROM evolutionDe WHERE asc_name = '{}' ;" .format(self)   
        connexion = sq.connect('Pokemon.db')
        desc = connexion.execute(requete)
        for tup in desc:
            if tup != 'Null':
                liste+=tup
        return liste
        connexion.close()
        
    def types(self):
        connexion = sq.connect('Pokemon.db')
        typ = list(connexion.execute("SELECT nom FROM type WHERE name IN (SELECT type_name FROM estDeType WHERE pokemon_name IN (SELECT name FROM pokemon WHERE name = '{}'));".format(self.name)))
        tab = []
        for v in typ:
            tab.append(v[0])
        return tab
        connexion.close()

    def pokemon_by_nom(nom):
        connexion = sq.connect('Pokemon.db')
        poke = connexion.execute("SELECT name FROM pokemon WHERE nom = '{}' ;".format(nom))
        for tup in poke:
            a = Pokemon(tup[0])
        return a
        connexion.close()
    
    def table_name():
        l = []
        connexion = sq.connect('Pokemon.db')
        table = list(connexion.execute("SELECT name FROM pokemon"))
        for tup in table:
            l.append(tup[0])
        return l
        connexion.close()
    
    def table_nom():
        l = []
        connexion = sq.connect('Pokemon.db')
        table = list(connexion.execute("SELECT nom FROM pokemon WHERE not nom = 'Null'"))
        for tup in table:
            l.append(tup[0])
        return l
        connexion.close()
        
    def effectif():
        connexion = sq.connect('Pokemon.db')
        n = list(connexion.execute("SELECT COUNT(*) FROM pokemon"))
        for tup in n:
            return tup[0]
        connexion.close()
         