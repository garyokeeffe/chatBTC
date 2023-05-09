# ChatBTC

This is an Open Source project designed to create a free and open Bitcoin-optimized LLM.

## Codebase Structure
The codebase is organized into 5 modules: `data`, `models`, `tests`, `data_generation`, and `utilities`. Outside of these modules, the modules, the codebase requires that you create a `.env` file (with contents: `OPENAI_API_KEY='YOUR API KEY'`), and we have included a `main.py` script as an example of how to work with the files in this project. See below for a basic schematic:
```
chatBTC/
  ├─ data/
  │   ├─ answers/
  │   │   └─ data.csv
  │   └─ questions/
  │       └─ data.csv
  ├─ models/
  │   ├─ __init__.py
  │   ├─ gpt3_default_model.py
  │   ├─ gpt3_prompt_eng_model.py
  │   └─ gpt3_answer_model.py
  ├─ tests/
  ├─ data_generation/
  │   └─ bitcoin_data_generator.py
  ├─ utils/
  │   ├─ model_factory.py
  │   └─ openai_api.py
  ├─ .env
  └─ main.py
```
### data
The `data` section contains all of the questions and answers data used for training and testing the model. This data is currently stored in `.csv` format however as the project grows this module will be migrated into a more scalable location.

### models
The `models` section contains all of the modles that have been opensourced. Currently all of the models are different versions of OpenAI's gpt3.5 model: `gpt3_default_model.py` is OpenAI's baseline model, `gpt3_prompt_eng_model.py` is a prompt engineered version of this default model aimed to be able to answer Bitcoin questions well, and `gpt3_answer_model.py` is the model used to generate simulated user questions (which are used to generate testing data).

### tests
The `tests` module is currently empty, however we are building out a comprehensive testing saddle to compare and benchmark model perfomance across a broad range of Bitcoin-adjacent topics.

### data_generation
The `data_generation` module contains all of the functions used to generate data for training the data. The `bitcoin_data_generator.py` file contains code used to generate data from preexisting LLM models. We will shortly be adding code here that will allow us to generate data from podcasts and other openly available online resources.

### utils
The `utils` module contains generic utility functions that don't cleanly map onto any of the other modules. Currently it hosts an OpenAI API wrapper and a file that maps each model to it's corresponding data label.

## Project Next Steps
The following list is a brief overview of items on our to-do list:

1. **Data Collection**: We are generating data to train the model, we are using a three-pronged approach for generating data: 
- using existing LLMs to generate training data
- using text various open online resources to generate training data
- using manual training data
We need your help on this! If you are open to working with us on any of these three areas, please reach out. 

2. **Open Source LLM migration**: Right now our models all have an untenable dependency on the user having an OpenAI API key. While anyone can generate an OpenAI API key and leverage our Open Source prompt engineered optimized versions of OpenAI's baseline model. We plan on moving to an Open Source LLM ASAP (while maintaining the same quality of model).

3. **Testing**: We are building out a comprehensive testing suite so that model performance can be benchmarked and tested across a broad range of Bitcoin adjacent topics.

3. **ChatBTC Front End**: We are buiding out a front-end that will allow anyone interact with our best performing model. For now you can interact with [our top-performing LLM here](https://nostr.money).

## Contributions
If you would like to contribute to the development of ChatBTC, here are two avenues:
- you can submit a pull request or raise an issue directly on this GitHub repository
- you can reach out to one of the project maintainers on Twitter: [Mustafa](https://twitter.com/MuatafaGMI) and [Gary](https://twitter.com/garyjokeeffe)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
