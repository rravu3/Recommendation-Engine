#/usr/bin/python2

import sys
import common
from numpy import *
from numpy.random import *

def getId(component):
  return component.getId()

class Ratings:
  """ A class to hold the ratings matrix associated with a recommendation dataset """
  def __init__(self,filename,separator='\t'):
    """ A constructer for the ratings class. 
        The argument filename is a file providing the ratings matrix 
        separator is the character that is used for separating a single entry in the ratings file 
    """
    self.data={}
    """ use a dictionary data structure to store the data """
    if filename!=None:
      f=open(filename,'rU')
      max_user_id=-1
      max_item_id=-1
      for line in f:
        result=line[:-1].split(separator)
        user_id=int(result[0])
        item_id=int(result[1])
        self.data[(user_id,item_id)]=float(result[2])
        """ The key into the dictionary data structure is a tuple of the form (user_id,item_id) """
        """ Donno what would be the difference in storing at as a dictionary or using one of the sparse matrix construct from numpy """
        if user_id>max_user_id:
          max_user_id=user_id
        if item_id > max_item_id:
          max_item_id=item_id
      print 'Number of ratings provided',len(self.data)
      print 'Total no of users',max_user_id
      print 'Total no of items',max_item_id
      self.max_user_id=max_user_id
      self.max_item_id=max_item_id

  def getRatingsData(self):
    return self.data

  def getTotalUsers(self):
    return self.max_user_id

  def getTotalItems(self):
    return self.max_item_id

def main():
  x=Ratings('/home/rahulravu/python_experiments/Recommendation_Engine/ml-1m/ratings.dat','::');

if __name__=='__main__':
  main()
