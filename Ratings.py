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
        separator is used to split the entries of a single rating entry 
    """
    self.data={}
    """ use a dictionary data structure to store the data
        the key for this dictionary is of the form (user_id,item_id)
        the value will be (rating_id,time_stamp)
        the time stamp value is optional
    """
    f=open(filename,'rU')

    max_user_id=-1
    max_item_id=-1

    for line in f:
      result=line[:-1].split(separator)
      user_id=int(result[0])
      item_id=int(result[1])
      
      """ handle cases when timestamp information is provided """
      if len(result)==3:
        self.data[(user_id,item_id)]=(float(result[2]),)
      else:
        self.data[(user_id,item_id)]=(float(result[2]),int(result[3]))
      if user_id>max_user_id:
        max_user_id=user_id
      if item_id > max_item_id:
        max_item_id=item_id

    self.max_user_id=max_user_id
    self.max_item_id=max_item_id

  def getRatingsData(self):
    return self.data

  def getTotalUsers(self):
    return self.max_user_id

  def getTotalItems(self):
    return self.max_item_id

  def storeRating(self,user_id,item_id,rating,timestamp=-1):
    if timestamp == -1:
      self.data[(user_id,item_id)]=(rating,)
    else:
      self.data[(user_id,item_id)]=(rating,timestamp)

    if self.max_user_id<user_id:
      self.max_user_id=user_id
    if self.max_item_id<item_id:
      self.max_item_id=item_id

def main():
  x=Ratings('/home/rahulravu/python_experiments/data/ml-1m/ratings.dat','::');

if __name__=='__main__':
  main()
