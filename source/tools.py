from transformers import BertTokenizer, BertModel
import torch


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

    print(sentence_embedding)
    return sentence_embedding


if __name__ == '__main__':
    # test
    text2embedding('I love cat.')
