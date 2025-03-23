from anthropic import Anthropic
class BaseAgent:
    def __init__(self, name: str, role: str, client: Anthropic):
        self.name = name
        self.role = role
        self.client = client
        self.memory = []
        
    def think(self, context: str) -> str:
        """Process information and make decisions"""
        prompt = self._create_prompt(context)
        response = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return response.content[0].text

    def _create_prompt(self, context: str) -> str:
        raise NotImplementedError