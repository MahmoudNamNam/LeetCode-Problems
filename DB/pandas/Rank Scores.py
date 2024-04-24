import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

df = pd.DataFrame(data)




def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method= 'dense', ascending=False)
    return scores.sort_values(by='score', ascending=False)[['score', 'rank']]


print(order_scores(df))




'''
'average': Assigns the average rank to all tied elements.
'min': Assigns the lowest rank to tied elements.
'max': Assigns the highest rank to tied elements.
'first': Assigns ranks in the order they appear in the Series or DataFrame.
'dense': Like 'min', but the rank always increases by 1 between groups.

'''