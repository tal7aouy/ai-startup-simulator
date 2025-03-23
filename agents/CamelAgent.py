from anthropic import Anthropic
from typing import List, Dict

class CamelAgent:
    """Base agent with CAMEL-inspired collaborative capabilities"""
    
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
            messages=[{"role": "user", "content": prompt}]
        )
        thought = response.content[0].text
        self.memory.append({"context": context, "thought": thought})
        return thought
    
    def dialogue_with(self, other_agent, topic: str, turns: int = 3) -> List[Dict]:
        """Have a back-and-forth dialogue with another agent"""
        conversation = []
        
        # Start the conversation
        first_prompt = f"""
        You are {self.name}, the {self.role}.
        You're starting a conversation with {other_agent.name}, the {other_agent.role}, about {topic}.
        Provide your initial thoughts or questions about {topic}.
        Keep your response under 100 words and be professional.
        """
        
        response = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{"role": "user", "content": first_prompt}]
        )
        
        first_message = response.content[0].text
        conversation.append({"speaker": self.name, "message": first_message})
        print(f"  {self.name}: {first_message[:100]}...")
        
        # Continue the dialogue for specified turns
        current_speaker = other_agent
        other_speaker = self
        context = first_message
        
        for _ in range(turns):
            next_prompt = f"""
            You are {current_speaker.name}, the {current_speaker.role}.
            You're in a conversation with {other_speaker.name}, the {other_speaker.role}, about {topic}.
            
            This is what {other_speaker.name} just said:
            "{context}"
            
            Respond to their points, advancing the discussion about {topic}.
            Keep your response under 100 words and be professional.
            """
            
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[{"role": "user", "content": next_prompt}]
            )
            
            next_message = response.content[0].text
            conversation.append({"speaker": current_speaker.name, "message": next_message})
            print(f"  {current_speaker.name}: {next_message[:100]}...")
            
            # Switch speakers
            current_speaker, other_speaker = other_speaker, current_speaker
            context = next_message
        
        return conversation
    
    def _create_prompt(self, context: str) -> str:
        """Create role-specific prompts"""
        raise NotImplementedError("Subclasses must implement this method")