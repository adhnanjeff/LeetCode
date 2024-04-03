#Problem 2877

#Name colums for DataFrames
import pandas as pd

def create_dataframe(student_data):
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

result_df = create_dataframe(student_data)
print(result_df)
