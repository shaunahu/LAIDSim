from transformers import BertTokenizer, BertModel
import torch
import pickle

def text2embedding(sentence):
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)

    inputs = tokenizer(sentence, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    last_hidden_states = outputs.last_hidden_state
    sentence_embedding = last_hidden_states[:, 0, :]

    sentence_embedding = sentence_embedding.numpy()

    # print(sentence_embedding)
    return sentence_embedding


def create_user_embedding():
    user_profiles = []
    with open("../data/input/user_profile.txt", "r") as file:
        for line in file.readlines():
            profile = line.split(": ")[1]
            user_profiles.append(profile)

    user_embeddings = []
    for user in user_profiles:
        embedding = text2embedding(user)
        user_embeddings.append(embedding)
        print(user)

    save_pickle(user_embeddings, "../data/input/user_embedding.pickle")


def save_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f'{filename} saved!')


def load_pickle(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        print(f'{filename} loaded!')
        return data


if __name__ == '__main__':
    # test
    # create_user_embedding()
    data = load_pickle('../data/input/user_embedding.pickle')
    print(data)