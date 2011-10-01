#/usr/bin/python2

from RecommendationEngine import *
from Ratings import *

def exampleUsage():
  #create the ratings object by specifying a ratings file and the separator between the fields in each line
  ratings=Ratings('/home/rahulravu/python_experiments/data/ml-1m/ratings.dat','::')

  #create the recommendation engine
  engine=FactorizationBasedEngine()

  #create a dictionary of training parameters.
  training_parameters={}
  training_parameters['iterations']=5
  training_parameters['dimensions']=10
  training_parameters['alpha']=0.01
  training_parameters['regularizer']=0.001
  training_parameters['training_split']=0.5

  #train the recommendation engine
  engine.train(ratings,training_parameters)

  #get the top N items for user with user_id 1.
  list_of_items=engine.getTopNItemsForUser(1)
  print 'Top Ten items for the current user are '
  print list_of_items

if __name__=='__main__':
  exampleUsage()
