import os

import openai
from googleapiclient.discovery import build

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GOOGLE_SEARCH_ENGINE_ID = os.environ.get("GOOGLE_SEARCH_ENGINE_ID")

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    return service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

search_query = "where can i find the best chilli crabs in singapore?"
    
results = google_search(search_query, GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID, num=3)
combined_results = ''
for result in results["items"]:

    combined_results += f"{result['title']}: {result['snippet']}, found at url - {result['link']}"

print(combined_results)

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": f"You are a chatbot that would be given a question and a list of top google search results. Augment your answers with these results: {combined_results}, and include the associated url."},
      {"role": "user", "content": search_query},
      {"role": "assistant", "content": "Search results: "}]
)

print(completion.choices[0].message)