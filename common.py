#/usr/bin/python2

import sys

class Component:
  """ This represents a single user/item """
  """ The class contains information about the user including the computed factors from matrix factorization method and attributes like age,gender that might be used in
      computing user similarity and finding out initial user factors for a new user """

  def __init__(self,id,factor=None,attributes=None):
    """ factor is the vector computed using a matrix factorization procedure """
    """ attributes is the dictionary containing user attributes like age,gender, etc """
    self.id=id
    self.factor=factor
    self.attributes={}
    if attributes:
      self.attributes=attributes

  def  getId(self):
    return self.id

  def getFactor(self):
    return self.factor

  def setFactor(self,factor):
    if factor!=None:
      self.factor=factor

  def getAttribute(self,attributeName):
    if attributeName in self.attributes.keys():
      return self.attributes[attributeName]
    else:
      return None

  def setAttribute(self,attributeName,attributeValue):
    self.attributes[attributeName]=attributeValue

  def setAttributes(self,attributes):
    for attributeName in attributes.keys():
      self.attributes[attributeName]=attributes[attributeName]

class User(Component):
  """ This class represents a user in the recommendation engine """
  """ Each user has a list of movies he has rated """
  def __init__(self,id,factor=None,attributes=None,movies=None):
    """ movies is a dictionary containing all mapping from movie ids to ratings """
    Component.__init__(self,id,factor,attributes)
    self.movies=movies

def main():
  """ Class for testing the functionality of the classes """
  x=User(1,[0.3,0.9])
  print x.getFactor() 

if __name__=='__main__':
  main()
