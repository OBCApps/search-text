
import os
import json

dataset_input = "./src/dataset/data_elecciones"
#dataset_input = "dataset\\data_elecciones_dev"
diretion_new_dataset = "clean_data"

def load_file(filename):
    #print(f"clean-Load File : {filename}")
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def id_text(tweets):
    clean_tweets = {}
    for tweet in tweets:
        if "id" in tweet and "text" in tweet:
            clean_tweets[tweet["id"]] = tweet["text"]
    return clean_tweets

def write_file(clean_tweets, filename):
    print(f"clean-Write File : {filename}")
    directory = os.path.dirname(filename)
    print(f"write in : {directory}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(clean_tweets, file)

def generate_clean_tweets():
    print("... Limpiando tweets ...")
    if not os.path.exists(diretion_new_dataset):
        os.makedirs(diretion_new_dataset)

    for filename in os.listdir(dataset_input):
        if filename.endswith(".json"):
            input_file = os.path.join(dataset_input, filename)
            output_file = os.path.join(diretion_new_dataset, filename)

            tweets = load_file(input_file)
            clean_tweets = id_text(tweets)
            write_file(clean_tweets, output_file)
    print("... Limpieza finalizada ...")


def generate_clean_tweets_web(data):
    print("... Limpiando tweets ...")
    global diretion_new_dataset
    diretion_new_dataset = "clean_data_dev"

    if not os.path.exists(diretion_new_dataset):
        os.makedirs(diretion_new_dataset)
    clean_tweets = id_text(data)
    write_file(clean_tweets, "documento")   
    print("... Limpieza finalizada ...")

# def main():
#     print("... Limpiando tweets ...")
#     generate_clean_tweets()
#     print("... Limpieza finalizada ...")


