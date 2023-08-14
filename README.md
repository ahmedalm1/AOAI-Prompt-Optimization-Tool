# AOAI-Prompt-Optimization-Tool

The Azure OpenAI Prompt Optimization Tool is an interactive Python application powered by OpenAI's GPT-3 technology and tkinter GUI framework. This tool evaluates user-provided prompts, optimizes them, and provides enhanced responses. It features dynamic input, response presentation, and user-friendly functionalities, all while leveraging the power of AI-driven language optimization.

## Prerequisites
An existing Azure OpenAI resource and model deployment of a chat model (e.g. gpt-35-turbo, gpt-4)

## Deploy the tool

### Deploy from your local machine

1. Update the environment variables listed in `.env.sample` with your API Key, Endpoint, and Deployed Model.
- `AZURE_OPENAI_API_KEY`: your Azure OpenAI resource API key.
- `AZURE_OPENAI_API_ENDPOINT`: your Azure OpenAI resource endpoint.
- `AZURE_OPENAI_DEPLOYED_MODEL`: your Azure OpenAI deployment name.

2. Run the following command to install all dependencies.
```
pip install -r requirements.txt
```

3. Run `app.py` file.

## How it works

The interface consists of four main elements:
- The prompt input text field to write your prompt.
- The response output window to see the omptimization recommendation. 
- The Submit button to send the prompt for AI analysis. 
- The Clear button to erase the prompt and start over.

![image](https://github.com/ahmedalm1/AOAI-Prompt-Optimization-Tool/assets/88718044/4423f0fc-1c7b-4568-a825-25b212af9718)

Once you enter and submit a prompt, the following response will be generated:
- Grade: a grade describing how good the prompt is on a scale from 1 to 10.
- Reason for Grade: the analysis of the prompts highlighting missing key elements and how to improve it. 
- Optimized Prompt: an example of an optimized prompt that will achieve the same goal in a more efficient way. 

![image](https://github.com/ahmedalm1/AOAI-Prompt-Optimization-Tool/assets/88718044/c7aabc3c-2e40-4af7-8eb7-e420d332290a)

## Optimization criteria 
The tool analyzes the prompt to determine its optimization level based on several criteria that aim to make the prompt clear, effective, and well-structured for the intended purpose. Below are the criteria used to evaluate whether a prompt is optimized or not:
- Clarity: The prompt should be easy to understand without ambiguity. It should convey the desired task or question clearly, so that both human readers and AI models can comprehend it accurately.
- Conciseness: An optimized prompt is concise and to the point. Unnecessary or redundant words should be eliminated to ensure efficient communication of the task to the AI model.
- Relevance: The prompt should directly relate to the desired output. Irrelevant information can confuse the AI model and result in inaccurate or off-topic responses.
- Contextual Information: Including sufficient context in the prompt can help guide the AI model towards the desired response. Relevant details or examples can improve the quality of generated content.
- Specificity: A well-optimized prompt is specific about the expected format, details, or structure of the response. Clear instructions can guide the AI model in producing accurate and relevant output.
- Language Quality: The language used in the prompt should be grammatically correct, coherent, and free of jargon that might confuse the AI model.

Overall, prompt optimization involves balancing these criteria to create a prompt that maximizes the AI model's ability to produce accurate, relevant, and contextually appropriate responses while minimizing the potential for misunderstandings or errors.
