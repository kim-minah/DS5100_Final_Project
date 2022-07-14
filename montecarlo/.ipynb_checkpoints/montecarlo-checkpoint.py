import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Die:
    """
    A class that rolls a die, changes weights, rolls and return the outcome.
    A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 

    """
    
    def __init__(self,faces): 
        """
        Internally initializes the weights to 1.0 for each face.
        Saves both faces and weights into a private dataframe that is to be shared by the other methods.       
        
        Parameters
        ----------
        faces: takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
        """
        self.faces = faces
        self.weights = np.repeat(1.0, len(self.faces)) 
        self._private_df = pd.DataFrame({'faces':self.faces,
                               'weights':self.weights})
        
    def change_weight(self,face,weight):
        """
        A method to change the weight of a single side.
        
        Parameters
        ----------
        face: the face value to be changed (needs to be a float or be able to be converted to a float)
        weight: the new weight

        """
        if face in self.faces:
            if not isinstance(float(weight), float): 
                print("Face value is not a float")
            else:
                cond = self._private_df['faces'] == face
                self._private_df.loc[cond,'weights'] = float(weight)
                
                
    def roll(self,num_times=1):
        """
        A method to roll the die one or more times. 
        
        Parameters
        ----------
        num_times: how many times the die is to be rolled; defaults to 1. 
        
        Returns
        ----------
        Output: list of outcomes from taking random samples from vector of faces according to the weights

        """
        i = 0
        results = []
        while i < num_times:
            result = self._private_df.faces.sample(weights=self._private_df.weights, replace = True).values[0] 
            results.append(result)  
            i += 1            
        return results
            
    def show(self):
        """
        A method to show the user the die’s current set of faces and weights 
        
        Returns
        ----------
        Output: the dataframe created in the initializer with any changes that may have been made to the weights      

        """
        return self._private_df

class Game:
    """
    A class that represents a 'game' consisted of rolling of one or more dice of the same kind one or more times. 
    Die "of the same kind" refer to die with the same number of sides and associated faces, but each die object may have its own weights.

    """
    
    def __init__(self, die_obj):
        """
        Each game is initialized with one or more of similarly defined dice (Die objects).
     
        Parameters
        ----------     
        Takes a single parameter, a list of already instantiated similar Die objects and saves it as a private variable to be shared with other methods     

        """
        self._private_die_obj = die_obj
        
    def play(self, num_rolls=1):
        """
        A method to play a game, i.e. to rolls all of the dice a given number of times.
        
        Parameters
        ----------
        num_times: how many times the dice should be rolled; defaults to 1. 
        
        Returns
        ----------
        Output: dataframe of the result of the playwith shape N rolls by M dice, saved as a private variable

        """
        results = [x.roll(num_rolls) for x in self._private_die_obj]
        plays = pd.DataFrame(results,
                     index=pd.Index(range(1,len(results)+1), name='Die'),
                     columns=pd.Index(range(1,num_rolls+1),
                     name='Roll Number')).T
        self._private_plays = plays
    
    def show(self,form='wide'):
        """
        A method to show the user the results of the most recent play.
        
        Parameters
        ----------
        form: a parameter to return the dataframe in narrow or wide form; defaults to 'wide'
        
        Returns
        ----------
        Output: private dataframe from the play method 

        """
        if form == 'wide':
            df = self._private_plays
            return df
        elif form == 'narrow':
            df = self._private_plays
            df_narrow = pd.DataFrame(df.stack())
            df_narrow.columns = ["Value"]
            return df_narrow
        else:
            raise ValueError("Choose between 'wide' and 'narrow' for form argument")
        
            
class Analyzer:
    """
    A class that akes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as
    attributes of an Analyzer object. 
    """
    def __init__(self,game_obj):
        """
        Each analyzer is initiatlized by a game object. At initialization time, it also infers the data type of the die faces used.
        
        Parameters
        ----------
        game_obj: a game object 

        """
        self.game_obj = game_obj
        self.df = self.game_obj.show()
        self.datatype = type(self.game_obj._private_die_obj[0].faces)
        
    
    def jackpot(self):
        """
        A method to compute how many times the game resulted in all faces being identical.
        
        Parameters
        ----------
        num_times: how many times the die is to be rolled; defaults to 1. 
        
        Returns
        ----------
        Output: an integer of the number of jackpots

        """
        df = self.df
        result = [list(row) for row in df[df.columns].to_numpy()]
        jp = [element.count(element[0])==len(element) for element in result]
        self.jp_df = pd.DataFrame(jp,index=pd.Index(range(1,len(df)+1), name='Roll Number'),
                            columns=["Jackpot or Not"])
        self.jp_count = sum(jp)
        return self.jp_count
    
    def combo(self):
        """
        A method to compute the distinct combinations of faces rolled, along with their counts.  
        
        Returns
        ----------
        Output: dataframe of combintation results stored with a multi-columned index
        """
        df = self.df  
        self.combo_counts = pd.DataFrame(df.value_counts(ascending=False),columns=["Counts"])
        return self.combo_counts
    
    def face_counts_per_roll(self):
        """
        A method to compute how many times a given face is rolled in each event.
        
        Returns
        ----------
        Output: dataframe of results with an index of the roll number and face values as columns (i.e. it is in wide format) 

        """
        df = self.df
        faces = self.game_obj._private_die_obj[0].faces
        counts = list()
        for row in df.values:
            row_val = list(row.flatten())
            row_count = [row_val.count(element) for element in faces]
            counts.append(row_count)
        self.face_counts = pd.DataFrame(counts,
                index=pd.Index(range(1,len(df)+1), name='Roll Number'),
                          columns=pd.Index(range(1,len(faces)+1),
                     name='Faces'))
        return self.face_counts