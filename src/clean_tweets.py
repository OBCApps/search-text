
import os
import json


dataset_input = "dataset\\data_elecciones"
diretion_new_dataset = "clean_data"

def load_tweets_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_clean_tweets(tweets):
    clean_tweets = {}
    for tweet in tweets:
        if "id" in tweet and "text" in tweet:
            clean_tweets[tweet["id"]] = tweet["text"]
    return clean_tweets

def save_clean_tweets_to_file(clean_tweets, filename):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(clean_tweets, file)

def generate_clean_tweets():
    if not os.path.exists(diretion_new_dataset):
        os.makedirs(diretion_new_dataset)

    for filename in os.listdir(dataset_input):
        if filename.endswith(".json"):
            input_file = os.path.join(dataset_input, filename)
            output_file = os.path.join(diretion_new_dataset, filename)

            tweets = load_tweets_from_file(input_file)
            clean_tweets = extract_clean_tweets(tweets)
            save_clean_tweets_to_file(clean_tweets, output_file)

def main():
    print("... Limpiando tweets ...")
    generate_clean_tweets()
    print("... Limpieza finalizada ...")


main()