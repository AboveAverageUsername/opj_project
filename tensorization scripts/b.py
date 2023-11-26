from transformers import ElectraTokenizer, TFBertModel

tokenizer = ElectraTokenizer.from_pretrained('classla/bcms-bertic')


model = TFBertModel.from_pretrained("classla/bcms-bertic", from_pt=True)

text = "yeet"

encoded_input = tokenizer(text, return_tensors='tf')
print(encoded_input)


output = model(encoded_input)


#print(output)
