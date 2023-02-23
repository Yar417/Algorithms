import openai
import pandas as pd

# Set your OpenAI API key
openai.api_key = "_____"
# Read the input CSV file
filename = "reviews.csv"
df = pd.read_csv(filename, delimiter=";")
# Add a new column for the ratings
df["rate"] = ""
# Add the column names to the first row
df.columns = ["email", "text preview", "data", "rate"]

# Iterate over the rows and prompt the user for a rating
for index, row in df.iterrows():
    text = row["text preview"]
    prompt = f"rate the text about the new application on a ten-point scale from 1 to 10, where 10 is the most enthusiastic, and 1 is the most negative comment. just return the number: {text}"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
    rating = response.choices[0].text.strip()
    df.loc[index, "rate"] = int(rating)  # добавил int
# Sort the DataFrame by the "rate" column in descending order
df = df.sort_values("rate", ascending=False)
# Save the modified table to a new CSV file
output_filename = filename.replace(".csv", "_analyzed.csv")
df.to_csv(output_filename, sep=";", index=False)
# Print the sorted DataFrame
# print(df)
