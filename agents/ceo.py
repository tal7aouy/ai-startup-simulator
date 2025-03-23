from .CamelAgent import CamelAgent
from typing import List, Dict

class CEOAgent(CamelAgent):
    def __init__(self, client):
        super().__init__("CEO", "Chief Executive Officer", client)
        self.developer = None
        self.marketer = None
        
    def make_strategic_decision(self, issue: str, options: List[str]) -> str:
        """Make high-level strategic decisions"""
        return self.think(f"Strategic decision needed on {issue}. Options: {options}")
        
    def resolve_conflict(self, issue: str, participants: List[str]) -> str:
        """Resolve conflicts between team members"""
        return self.think(f"Based on debate among {participants} about {issue}, resolve this conflict")
        
    def _create_prompt(self, context: str) -> str:
        """Create strategic decision-making prompts"""
        return f"""You are the CEO of a promising tech startup with a vision for innovation and growth.
                
        Your role: {self.role}
        Task: {context}

        Provide a decisive, balanced assessment considering business impact, market opportunity, resources, and risk.
        Focus on both short-term execution and long-term strategic positioning.
        Keep your response under 200 words and provide clear reasoning for your choices."""
    
    def brainstorm_with_developer(self, topic: str) -> List[Dict]:
        """Brainstorm technical solutions with the developer"""
        if not self.developer:
            return [{"speaker": "System", "message": "Developer reference not set"}]
        return self.dialogue_with(self.developer, f"technical approach for {topic}")
    
    def plan_with_marketer(self, topic: str) -> List[Dict]:
        """Plan marketing strategy with the marketer"""
        if not self.marketer:
            return [{"speaker": "System", "message": "Marketer reference not set"}]
        return self.dialogue_with(self.marketer, f"marketing strategy for {topic}")