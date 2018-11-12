import json

tweets = []

with open("twitter.json") as f:
    tweets = json.loads(f.read())

print("Opgave a:")

print("Amount of tweets:", len(tweets))

for t in range(0, min(5, len(tweets))):
    print(tweets[t])

# ---

print("\n---\nOpgave b:")

filtered = [(t["text"], t["retweet_count"]) for t in tweets if t["favorite_count"] >= 10000]

print("Amount of filtered tweets:", len(filtered))

for t in range(0, min(5, len(filtered))):
    print(filtered[t])

# ---

print("\n---\nOpgave c:")

sorted_filtered = sorted(filtered, key=lambda x: x[1], reverse=True)

for t in range(0, min(5, len(sorted_filtered))):
    print(sorted_filtered[t])

# ---

print("\n---\nOpgave d:")

shortest = min(tweets, key=lambda x: len(x["text"]))
print(shortest["text"])
