from .CamelAgent import CamelAgent
from typing import Dict

class DeveloperAgent(CamelAgent):
    def __init__(self, client):
        super().__init__("Developer", "Technical Lead", client)
        
    def evaluate_tech_stack(self, requirements: Dict) -> str:
        """Evaluate and recommend technical solutions"""
        return self.think(f"Evaluate tech stack for requirements: {requirements}")
        
    def estimate_effort(self, feature: str) -> Dict:
        """Estimate development effort and technical complexity"""
        return {
            "time": self.think(f"Estimate time for {feature}"),
            "complexity": self.think(f"Evaluate complexity of {feature}")
        }
        
    def _create_prompt(self, context: str) -> str:
        """Create development-focused prompts"""
        return f"""You are a senior software engineer with full-stack development expertise.
        
        Your role: {self.role}
        Task: {context}

        Provide a technical assessment focusing on modern best practices, scalability, and efficiency.
        Consider trade-offs between development speed, technical debt, and scalability.
        Keep your response under 200 words and be specific about technologies where appropriate."""