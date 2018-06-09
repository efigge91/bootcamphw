import pandas as pd
import os

election_data = os.path.join("Resources", "election_data_1.csv")
df = pd.read_csv(election_data)

total_votes=len(df.Candidate)

output = df['Candidate'].value_counts().reset_index()
output.columns = ['Candidate', 'Votes']

output1 = (df.Candidate.value_counts() / total_votes*100).reset_index()
output1.columns = ['Candidate', 'Percentage of Votes']
output1['Percentage of Votes'] = output1['Percentage of Votes'].astype(str) + '%'

final_output = pd.merge(output1, output, on='Candidate')

f = open('PyBank.txt','w')
f.write("Election Results\n"
"-------------------------\n"
"Total Votes:" + str(total_votes) + "\n"
"-------------------------\n"
+ out.to_string(index=False) + "\n"
+ "-------------------------\n"
"Winner: " + out.iat[0,0] + "\n"
"-------------------------")
f.close()

print("Election Results\n"
"-------------------------\n"
"Total Votes:" + str(total_votes) + "\n"
"-------------------------\n"
+ out.to_string(index=False) + "\n"
+ "-------------------------\n"
"Winner: " + out.iat[0,0] + "\n"
"-------------------------")
