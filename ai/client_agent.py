from django.conf import settings
from openai import OpenAI
from ai import prompts

class SGEAgent:
    
    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )
     
    # Invoca o agente   
    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': prompts.SYSTEM_PROMPT,
                },
                {
                    'role': 'user',
                    'content': prompts.USER_PROMPT.replace('{{data}}'),     # replace para subsstituir o 'data'
                },
            ]
        )
        result = response.choices[0].message.content
        return result