import data
import pandas as pd

attraction_totals = None
category_totals = None
for day in data.days:
    print(day)
    df = data.read_visited_key_points(day, ['category'])

    day_attraction_totals = pd.DataFrame(columns=['total'], data=df.groupby('place_id').size())
    if attraction_totals is None:
        attraction_totals = day_attraction_totals
    else:
        attraction_totals.add(day_attraction_totals, fill_value=0)

    day_category_totals = pd.DataFrame(columns=['total'], data=df.groupby('category').size())
    if category_totals is None:
        category_totals = day_category_totals
    else:
        category_totals.add(day_category_totals, fill_value=0)

kp = data.read_key_points().set_index('place_id')
attraction_totals['name'] = kp['name']
attraction_totals.sort_values(by='total', ascending=False, inplace=True)
category_totals.sort_values(by='total', ascending=False, inplace=True)

print(attraction_totals)
print(category_totals)

