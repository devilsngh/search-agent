Creating Tools and Using it in the model

Tool is nothing but a function which your agent calls (provide all the info related to methods arguments, arguments type, document) you basically create multiple tools (functions annotated with @tool - refer main.py) and pass it to LLM along with prompt it basically picks a suitable tool along with args which is then used by the agent to call the method. Agent calls the method the result are passed to the model and the model returns the response again).

As model -> gemma3:270m does not support tool calling  
searched for a light weight model in ollama with tool calling capabilities got to know about model -> llama3.2  
ollama pull llama3.2  


Output generated when the temperature = 1 (for creativeness) -> 
According to the current weather conditions, Tokyo is experiencing a sunny day with clear skies. The temperature is  
around 22°C (72°F) and feels like 25°C (77°F). It's a great day to explore the city! Would you like to know more about  
the forecast or any specific location in Tokyo?  

![img.png](img.png)

![img_1.png](img_1.png)

0 -> HumanMessage(content='what is the weather in ...')  
1 -> AIMessage(content='', additional_kwargs='....)  
2 -> ToolMessage(content='Tokyo weather is sunny', ....)  
3 -> AIMessage(content='The weather in tokyo is currently sunny', ......)  
