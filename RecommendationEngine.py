#/usr/bin/python2

import sys
import Ratings
import common
import numpy
import numpy.random
import math
import Utilities

class GenericRecommendationEngine:
  """ This is an abstract base class representing the common methods that are present in all recommendation engines """
  
  def train(self,Ratings,training_parameters):
    pass

  def addNewUser(self,user):
    pass

  def addNewItem(self,item):
    pass

  def computeRating(user_id,item_id):
    pass


class FactorizationBasedEngine(GenericRecommendationEngine):

  def __init__(self):
    self.trained=False

  def train(self,ratings,training_parameters):
    print 'Will now train the system on the ratings data'
    self.users={}
    self.items={}
    total_users=ratings.getTotalUsers()
    total_items=ratings.getTotalItems()
    factor_dimension=training_parameters['dimensions']
    for i in range(1,total_users+1):
      initial_factor=numpy.random.uniform(0.0,1.0,factor_dimension)
      self.users[i]=common.User(i,initial_factor)
    for i in range(1,total_items+1):
      initial_factor=numpy.random.uniform(0.0,1.0,factor_dimension)
      self.items[i]=common.Component(i,initial_factor)
    data=ratings.getRatingsData()
    regularizer=training_parameters['regularizer']
    update_rate=training_parameters['alpha']
    split=self.splitData(data,training_parameters['training_split'])
    training_data=split[0]
    test_data=split[1]
    for i in range(training_parameters['iterations']):
      print 'At Iteration',(i+1)
      for key in training_data.keys():
        user_factor=self.users[key[0]].getFactor()
        item_factor=self.items[key[1]].getFactor()
        true_rating=training_data[key][0]
        prediction=(user_factor*item_factor).sum()
        error=true_rating-prediction
        temp=user_factor+(update_rate*error*item_factor)-(regularizer*user_factor)
        self.users[key[0]].setFactor(temp)
        temp=item_factor+(update_rate*error*user_factor)-(regularizer*item_factor)
        self.items[key[1]].setFactor(temp)
      total_error=0.0
      for key in test_data.keys():
        user_factor=self.users[key[0]].getFactor()
        item_factor=self.items[key[1]].getFactor()
        prediction=(user_factor*item_factor).sum()
        total_error+=((test_data[key][0]-prediction)*(test_data[key][0]-prediction))
      total_error=math.sqrt(total_error/len(test_data))
      print 'Test Error after iteration',(i+1),' is ',total_error
    print 'Training Complete' 
    self.trained=True
     
  def splitData(self,data,training_split):
    training_data={}
    test_data={}
    random_vals=numpy.random.uniform(0.0,1.0,len(data))
    count=0
    for key in data.keys():
      if random_vals[count] > training_split:
        test_data[key]=data[key]
      else:
        training_data[key]=data[key]
      count+=1
    print 'Total no of instances in training data',len(training_data)
    print 'Total no of instances in test data',len(test_data)
    return (training_data,test_data)

  def addNewUser(self,user):
    if self.trained:
      print 'added the new user information to the existing data'
    else:
      print 'use the train method to obtain an initial set of users without this addition will not make any sense'

  def addNewItem(self,item):
    if self.trained:
      print 'added the new user information to the existing data'
    else:
      print 'use the train method to obtain an initial set of users without this addition will not make any sense'

  def computeRating(user_id,item_id):
    if self.trained:
      user_factor=self.users[user_id].getFactor()
      item_factor=self.items[item_id].getFactor()
      rating=(user_factor*item_factor).sum()
      return rating
    else:
      print 'Recommendation Engine hasn\'t been trained yet. Please train it.'
      return 0.0

  def getTopNItemsForUser(self,user_id,n=10):
    if self.trained:
      user_factor=self.users[user_id].getFactor()
      preferences=[]
      for item in self.items.keys():
        item_factor=self.items[item].getFactor()
        temp=(user_factor*item_factor).sum()
        preferences.append((item,temp))
      preferences=sorted(preferences,reverse=True,key=Utilities.valueSelector)
      result=[]
      if n > len(self.items):
        n=len(self.items)
      for i in range(n):
        result.append(preferences[i][0])
      return result
    else:
      print 'Recommendation Engine hasn\'t been trained yet. Please train it.'
      return None

def main():
  ratings=Ratings.Ratings('/home/rahulravu/python_experiments/data/ml-1m/ratings.dat','::')
  engine=FactorizationBasedEngine()
  training_parameters={}
  training_parameters['iterations']=500
  training_parameters['dimensions']=10
  training_parameters['alpha']=0.01
  training_parameters['regularizer']=0.001
  training_parameters['training_split']=0.5
  engine.train(ratings,training_parameters)
  list_of_items=engine.getTopNItemsForUser(1)
  print 'Top Ten items for the current user are '
  print list_of_items


if __name__=='__main__':
  main()
