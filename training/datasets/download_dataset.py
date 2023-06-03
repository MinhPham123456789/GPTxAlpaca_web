from datasets import load_dataset

dataset = load_dataset("lucasmccabe-lmi/instruct_to_code_alpaca_style")
for split, data in dataset.items():
  data.to_json("train_lucasmccabe_alpaca.json")
