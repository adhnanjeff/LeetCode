#Problem 2878


from typing import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players.axes[0]), len(players.axes[1])]


df = pd.DataFrame({'name': ['Katherine', 'James', 'Emily',
							'Michael', 'Matthew', 'Laura'],
				'score': [98, 80, 60, 85, 49, 92],
				'age': [20, 25, 22, 24, 21, 20],
				'qualify_label': ['yes', 'yes', 'no',
									'yes', 'no', 'yes']})

print(getDataframeSize(df))

"""
# importing pandas
import pandas as pd

# creating dataframe
df = pd.DataFrame({'name': ['Katherine', 'James', 'Emily',
							'Michael', 'Matthew', 'Laura'],
				'score': [98, 80, 60, 85, 49, 92],
				'age': [20, 25, 22, 24, 21, 20],
				'qualify_label': ['yes', 'yes', 'no',
									'yes', 'no', 'yes']})

print(len(df))
print(len(df.columns))

"""