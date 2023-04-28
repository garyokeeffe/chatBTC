# ChatBTC

ChatBTC is an AI chat bot that has been designed to answer questions related to Bitcoin. This repository contains the source code for ChatBTC, as well as the necessary data files and documentation.

## Workflow

The following is a brief overview of the workflow used to create and train the ChatBTC chat bot:

1. **Data Collection**: Various sources of data related to Bitcoin were collected, such as books, papers, articles, tweets, etc. This data was then cleaned and preprocessed to remove any noise and ensure consistency.

      Dataset sorces:
    - Satoshi Nakamoto quotes, emails ..etc [here](https://github.com/NakamotoInstitute/nakamotoinstitute.org/blob/master/data/emails.json)
    - Twitter scrap with [Hive](https://hive.one/)
    - Bitcoin Q&A from [stack exchange](https://bitcoin.stackexchange.com/) 
    - Text data from [nomicc Ai](https://home.nomic.ai/)
    - Speach to text to collect data from podcasts & videos using tools like [OASIS](https://theoasis.com/) and [Speech recognition](https://github.com/Uberi/speech_recognition#readme)
    

     Dataset format: 
    - SQuAD dataset format, more details [here](https://rajpurkar.github.io/SQuAD-explorer/)
 
    - Atlas dataset format, more details [here](https://atlas.nomic.ai/)




2. **Language Model Selection**: A list of Language Models (LLMs) could be found [Here](https://github.com/formulahendry/awesome-gpt). by selecting the most suitable LLMs that would provide the best performance for the chatBTC.


3. **ChatBTC Front End**: The ChatBTC integration  into a website or an API.



## Contributions

If you would like to contribute to the development of ChatBTC, please submit a pull request or raise an issue on the GitHub repository. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
