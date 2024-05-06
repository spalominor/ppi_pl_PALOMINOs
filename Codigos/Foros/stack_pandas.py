# Import the pandas library
import pandas as pd

# Create the original dataframe
data = {
    'USERNAME': ['RAJKUMAR.MALVIYA', 'GOURAV.MOD', 'PRASANNA.NAIK', 
                 'SANJAY.BHATNAGAR', 'UMANG.GOHIL1', 'MILIND.DESHMUKH', 
                 'HIREN.JASANI', 'SACHIN.PAWAR', 'BHAVIN.GANDHI', 
                 'ANURAG.JOSHI', 'SANGRAM.KEDARI', 'NIKHIL.BELKHEDE', 
                 'SACHIN.PAWAR'],
    'DESIGNATION': ['BM', 'ASM', 'RSM', 'NSM', 'BM', 'ZSM', 'ASM', 'NSM', 
                    'DSM', 'ZSM', 'BM', 'DSM', 'NSM'],
    'VERTICAL REPORT': ['GOURAV.MOD', 'PRASANNA.NAIK', 'MILIND.DESHMUKH', 
                        'ARUN', 'HIREN.JASANI', 'SANJAY.BHATNAGAR', 
                        'BHAVIN.GANDHI', 'ARUN', 'ANURAG.JOSHI', 
                        'SACHIN.PAWAR', 'NIKHIL.BELKHEDE', 
                        'SACHIN.PAWAR', 'ARUN']
}

# List of designations
designations = ['BM', 'ASM', 'CSM', 'DSM', 'RSM', 'ZSM', 'NSM']

# Create the original dataframe
df = pd.DataFrame(data)
df_vertical = pd.DataFrame()

# Group usernames by designation
df_designation = df.groupby(
    'DESIGNATION')['USERNAME'].apply(list).reset_index()

# Assign usernames to each column
for des in designations:
    # Use explode to expand lists into separate rows and reset index
    df_vertical[
        des] = df_designation.loc[
            df_designation[
                'DESIGNATION'] == des, 'USERNAME'].explode().reset_index(drop=True)

# Replace NaN with f'L{n}' where n is the column number
for col in df_vertical.columns:
    # Get the column number
    n = df_vertical.columns.get_loc(col) + 1  
    
    # Fill NaN values with f'L{n}'
    df_vertical[col] = df_vertical[col].fillna(f'L{n}')

# Print the result
print(df_vertical)
