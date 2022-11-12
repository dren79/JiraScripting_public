import json
import pandas as pd
import plotly.express as px

filename = 'go_to_devfest'
with open(f'reports/{filename}.json', 'r') as f:
    report = json.load(f)

stories = report['stories']

df2 = pd.DataFrame.from_dict(stories, orient='index')
# This adds the key in as a column
df2['index'] = df2.index
stories_df = df2.groupby(by=['assignee', 'status_category', 'index']).count()[["hash"]].rename(columns={"hash": "count"})
# This fills each row as the group by gives a hierarchical view
stories_df = stories_df.reset_index()
stories_df.head()
# If you want to see what the dataframe looks like uncomment the print below
# print(stories_df)
fig = px.sunburst(stories_df,
                   path=['assignee', 'status_category', 'index'],
                   values='count',
                   maxdepth=3,
                   color='status_category',
                   color_discrete_map={'(?)': 'black', "new": 'red', "indeterminate": 'pink', "done": 'green'}
                   )
# Open a browser with the interactive graph
fig.show()

with open(f'reports/{filename}.html', 'a') as f:
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))