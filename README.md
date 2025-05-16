
<h1 align="center">
  <b>Human-Aligned Benchmark: Fine-Grained Assessment of Reasoning Ability in MLLMs vs. Humans</b><br>
</h1>

<p align="center">
  📚 <a href="#">[Paper]</a>
  🤗 <a href="https://huggingface.co/datasets/yanshengqiu/Human_Aligned_Bench">[Dataset]</a>
</p>




## 🚀 Quick Start

### Create the enviroment

```bash
pip install requirements.txt
```

### Data preparation

Download the data from <a href="https://huggingface.co/datasets/yanshengqiu/Human_Aligned_Bench">[Huggingface]</a> and put them in dataset floder

My project code framework for reference
```
Human_Aligned_Bench/
├── configs
├── dataset
├── models
├── prompts
├── eval.py
├── util.py
```

### Setting up the API:

1. Please set the model_name, base_url, and key for MLLMs in configs/model_keys.json.


2. Please configure the generation method using the API in lines 63-79 of util.py.


### Start eval:

```bash
python eval.py

python eval_w_hs.py
```



## 📜 Citations
```

```


**Note:** This is a research level repository and might contain issues/bugs. Please contact the authors for any query.
