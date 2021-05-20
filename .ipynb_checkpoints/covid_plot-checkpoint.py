
import pandas as pd
import matplotlib.pyplot as plt

def read_in_data(filename):
    '''
    INPUT: 
    filename: path to file name: e.g. /home/shared_data/covid-19-data/rolling-averages/us-states.csv
    OUTPUT: Pandas dataframe - converted from csv input
    '''


def get_extreme_states(df, num_states):
     '''
    INPUT: 
    df: Pandas dataframe with raw state data
    num_states: The number of states to include on either extreme end (e.g. 5 will return 5 states with lowest overall average covid
    cases per 100k)
    OUTPUT: 
    low_states: states with lowest covid cases
    high_states: states with highest covid cases
    '''
    import pandas as pd

    mean_df = df.groupby('state').cases_avg_per_100k.agg(['mean'])
    largest_states = mean_df.nlargest(3,'mean')
    smallest_states = mean_df.nsmallest(3,'mean')
    
    largest_states.reset_index(inplace=True)
    largest_states = largest_states.rename(columns = {'index':'state'})
    smallest_states.reset_index(inplace=True)
    smallest_states = smallest_states.rename(columns = {'index':'state'})

    return([smallest_states.state,largest_states.state])
    
def make_plot(df,states_to_plot):
     '''
    INPUT: 
    df: Pandas dataframe with raw state data
    states_to_plot: list of states to plot (e.g. ['Oregon','Texas','California'])
    OUTPUT: 
    ax: handle to current plot
    '''
    ...
        
    
   
      
def modify_plot(ax,states_to_plot):
     '''
    This function modifies date formatting on plot to make them look better.
    INPUT: 
    ax: handle to current plot
 
    '''
    
    ...
  
   
