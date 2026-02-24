ai_test_generator/
│
├── main.py
├── validator.py
├── sanitizer.py
├── llm_client.py
├── example.py
├── .env
├── requirements.txt
└── ReadMe.md

## Requirements :
- make sure you have python 3.9+
- OpenRouter API key (or compatible OpenAI API key)
- install require packages --> pip install -r requirements.txt



## How to run my app:
- the app run in terminal by loading a file `example.py`
- paste your own function in the `example.py`
- type in yout terminal `python main.py example.py`



### Note:
**If you get any errors like main block exist of or any results of Ai hallucination change the OPENROUTER_MODEL in .env file if you have acess to it <3**