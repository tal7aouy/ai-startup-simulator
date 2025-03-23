from .CamelAgent import CamelAgent
from typing import Dict

class MarketerAgent(CamelAgent):
    def __init__(self, client):
        super().__init__("Marketer", "Marketing Lead", client)
        
    def analyze_market(self, product: str) -> Dict:
        """Analyze market potential and competition"""
        return {
            "market_size": self.think(f"Estimate market size for {product}"),
            "competitors": self.think(f"Identify main competitors for {product}"),
            "positioning": self.think(f"Suggest positioning for {product}")
        }
        
    def _create_prompt(self, context: str) -> str:
        """Create marketing-focused prompts"""
        return f"""You are a marketing expert with experience in SaaS and tech products.
        
        Your role: {self.role}
        Task: {context}

        Provide a concise, data-driven response with market insights and strategic recommendations.
        Focus on target audience, market trends, and competitive positioning.
        Keep your response under 200 words."""