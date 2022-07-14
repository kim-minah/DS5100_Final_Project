# Metadata
##### Minah Kim
##### Monte Carlo Simulator

# Synopsis
##### Demo code

Installing:
After navigating to the repository root with the setup.py file
```
!pip install .
```
Importing:
```
from montecarlo import Die, Game, Analyzer
```
Creating dice:
```
die = Die(np.array([1,2,3,4,5,6]))
```
Playing games:
```
dice1 = Die(np.array([1,2,3,4,5,6]))
dice2 = Die(np.array([1,2,3,4,5,6]))
game = Game([dice1,dice2])
```
Analyzing games:
```
dice1 = Die(np.array([1,2,3]))
dice2 = Die(np.array([1,2,3]))
die_list = list([dice1,dice2])
game = Game([dice1, dice2])
game.play(1000)
analyzer = Analyzer(game)
```
# API Description
#### List of all classes with their public methods and attributes

##### Die class
A class that rolls a die, changes weights, rolls and return the outcome. A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 

###### Methods
* change_weight(face, weight)
  A method to change the weight of a single side.
  * Parameters:
        face: the face value to be changed 
        weight: the new weight (needs to be a float or be able to be converted to a float)
  * Returns:
        none
- roll(num_times=1)
  A method to roll the die one or more times. 
  * Parameters:
        num_times: how many times the die is to be rolled; defaults to 1. 
  * Returns:
        list of outcomes from taking random samples from vector of faces according to the weights
- show()
  A method to show the user the die’s current set of faces and weights 
  * Parameters:
        none
  * Returns:
        the dataframe created in the initializer with any changes that may have been made to the weights 

##### Game class
 A class that represents a 'game' consisted of rolling of one or more dice of the same kind one or more times. Die "of the same kind" refer to die with the same number of sides and associated faces, but each die object may have its own weights.
###### Methods
- play(num_rolls = 1)
A method to play a game, i.e. to rolls all of the dice a given number of times. A dataframe of the result of the playwith shape N rolls by M dice gets saved as a private variable.
  * Parameters:
        num_roles: how many times the die is to be rolled; defaults to 1. 
  * Returns:
        none
- show()
  A method to show the user the results of the most recent plays
  * Parameters:
        none
  * Returns:
        the private dataframe from the play method
##### Analyzer class
A class that akes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. 
###### Methods
- jackpot()
  A method to compute how many times the game resulted in all faces being identical.
  * Parameters:
        none
  * Returns:
        an integer of the number of jackpots
- combo()
  A method to compute the distinct combinations of faces rolled, along with their counts.  
  * Returns:
        dataframe of combination results stored with a multi-columned index
- face_counts_per_roll()
   A method to compute how many times a given face is rolled in each event.
   * Output: 
        dataframe of results with an index of the roll number and face values as columns (i.e. it is in wide format) 
###### Attributes
- jp_count:
  number of jackpots generated 
- combo_counts:
  distinct combinations of faces rolled, along with their counts
- face_counts:
  many times a given face is rolled in each event.


# Manifest

### Root
| Name | Description |
| ------ | ------ |
| montecarlo/ | Package directory |
| setup.py | Setup file |
| README.md | The file you're currently reading! |
| LICENSE | MIT license file |
| montecarlo_report_scenarios.ipynb | Final project template with all my module and unit test scripts and code to test scenarios |
| sgb-words.txt | File needed to test Scenario 3 in montecarlo_report_scenarios.ipynb |
| letter-freqs.csv| File needed to test Scenario 3 in montecarlo_report_scenarios.ipynb |

### montecarlo/
| Name | Description |
| ------ | ------ |
| montecarlo.py | Monte carlo module |
| montecarlo_unittest.py | Unit test file |
| montecarlo_unitest_results.txt | Results from unit test |

