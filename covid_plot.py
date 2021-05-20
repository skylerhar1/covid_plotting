
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

    max_mean = (mean_df['mean'].agg(['max']))[0]
    max_state = mean_df[mean_df['mean']==max_mean]

    min_mean = (mean_df['mean'].agg(['min']))[0]
    min_state = mean_df[mean_df['mean']==min_mean]
    print(max_state)
    print(min_state)
    df.drop['']
    #print(mean_df)
    return [max_state,min_state]
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
  
   
