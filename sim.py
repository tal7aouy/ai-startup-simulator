import os
from dotenv import load_dotenv
from anthropic import Anthropic, DefaultHttpxClient
from agents.ceo import CEOAgent
from agents.developer import DeveloperAgent
from agents.marketer import MarketerAgent
from viz import SimulationVisualizer
import numpy as np
load_dotenv()

MILESTONES = [
    ("Day 1-5", "Market research & tech stack selection"),
    ("Day 6-15", "MVP development"),
    ("Day 16-25", "User testing & marketing prep"),
    ("Day 26-30", "Launch & analytics")
]

class StartupSimulation:
    def __init__(self, product_idea: str):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
            
        self.client = Anthropic(
            api_key=api_key,
            http_client=DefaultHttpxClient()
        )
        
        self.ceo = CEOAgent(self.client)
        self.developer = DeveloperAgent(self.client)
        self.marketer = MarketerAgent(self.client)
        self.product = product_idea
        self.metrics = {
            'User Signups': [],
            'Conversion Rate': [],
            'Development Velocity': [],
            'Customer Satisfaction': []
        }
        self.agent_info = {
            'ceo': {
                'name': 'CEO', 
                'role': 'Chief Executive Officer',
                'relations': [
                    {'to': 'dev', 'type': 'directs'},
                    {'to': 'mkt', 'type': 'directs'}
                ]
            },
            'dev': {
                'name': 'Developer', 
                'role': 'Technical Lead',
                'relations': [
                    {'to': 'mkt', 'type': 'collaborates'}
                ]
            },
            'mkt': {
                'name': 'Marketer', 
                'role': 'Marketing Lead',
                'relations': [
                    {'to': 'ceo', 'type': 'reports to'}
                ]
            }
        }
        
    
    def _execute_milestone(self, period: str, task: str):
        """Execute tasks for each milestone period"""
        day_num = int(period.split('-')[-1])

        if "Market research" in task:
            print("🔍 Conducting market research...")
            market_analysis = self.marketer.analyze_market(self.product)
            print(f"📊 Market size: {market_analysis['market_size']}")
            print(f"🏢 Competitors: {market_analysis['competitors']}")
            print(f"🎯 Positioning: {market_analysis['positioning']}")
            
            print("\n💻 Evaluating technology options...")
            tech_requirements = {
                "product": self.product,
                "market_size": market_analysis['market_size'],
                "time_constraint": "4 weeks"
            }
            tech_stack = self.developer.evaluate_tech_stack(tech_requirements)
            print(f"🛠️ Recommended tech stack: {tech_stack}")
            
            print("\n🧠 CEO making strategic decisions...")
            options = ["Focus on quick MVP", "Build robust architecture", "Outsource development"]
            strategy = self.ceo.make_strategic_decision("Development approach", options)
            print(f"📝 Strategic plan: {strategy}")
            
            # Add CAMEL-based dialogue between CEO and Developer
            print("\n🗣️ CEO and Developer discussing tech approach...")
            # Set up references for dialogue
            self.ceo.developer = self.developer
            dialogue = self.ceo.brainstorm_with_developer(self.product)
            
        elif "MVP development" in task:
            print("📋 Planning MVP features...")
            features = [
                f"Core {self.product} functionality", 
                "User authentication",
                "Basic analytics", 
                "Payment processing"
            ]
            
            print("⏱️ Estimating development effort...")
            effort_estimates = {}
            for feature in features:
                effort = self.developer.estimate_effort(feature)
                effort_estimates[feature] = effort
                print(f"  - {feature}: {effort['time']} (Complexity: {effort['complexity']})")
            
            print("\n🔨 Beginning development...")
            print("  Day 7: Setting up development environment")
            print("  Day 9: Basic application structure complete")
            print("  Day 12: Key features implemented")
            print("  Day 15: MVP ready for testing")
            
        elif "User testing" in task:
            print("👥 Recruiting test users...")
            print("📝 Collecting user feedback...")
            
            feedback = [
                "Interface is confusing",
                "Love the core functionality",
                "Missing important feature X",
                "Performance issues on mobile"
            ]
            
            for i, item in enumerate(feedback, 1):
                print(f"  Feedback #{i}: {item}")
            
            print("\n🛠️ Developer addressing critical issues...")
            for issue in feedback[:2]: 
                print(f"  Fixing: {issue}")
            
            print("\n📣 Marketer preparing launch campaign...")
            print("  - Creating landing page")
            print("  - Preparing email templates")
            print("  - Setting up analytics")
            
            # Add CAMEL-based dialogue between CEO and Marketer
            print("\n🗣️ CEO and Marketer planning launch strategy...")
            self.ceo.marketer = self.marketer
            dialogue = self.ceo.plan_with_marketer(self.product)
            
        elif "Launch" in task:
            print("🚀 Product launch day!")
            print("📊 Initial metrics:")
            print("  - 150 website visitors")
            print("  - 45 signups")
            print("  - 12 paying customers")
            
            print("\n📈 Marketer analyzing conversion rates...")
            print("  - 30% visitor-to-signup conversion")
            print("  - 26.7% signup-to-customer conversion")
            
            print("\n👨‍💼 CEO evaluating launch success...")
            options = ["Continue with current strategy", "Pivot to different market", "Seek additional funding"]
            decision = self.ceo.make_strategic_decision("Post-launch strategy", options)
            print(f"🔮 Future direction: {decision}")

        # Update metrics
        if "Market research" in task:
            self.metrics['User Signups'].append((f"Day {day_num}", 0))
            self.metrics['Conversion Rate'].append((f"Day {day_num}", 0))
            self.metrics['Development Velocity'].append((f"Day {day_num}", 7))  
            self.metrics['Customer Satisfaction'].append((f"Day {day_num}", 0))
            
        elif "MVP development" in task:
            self.metrics['User Signups'].append((f"Day {day_num}", 5))  
            self.metrics['Development Velocity'].append((f"Day {day_num}", 9))
            
        elif "User testing" in task:
            self.metrics['User Signups'].append((f"Day {day_num}", 25))
            self.metrics['Conversion Rate'].append((f"Day {day_num}", 0.2))
            self.metrics['Development Velocity'].append((f"Day {day_num}", 6))  
            self.metrics['Customer Satisfaction'].append((f"Day {day_num}", 0.7))
            
        elif "Launch" in task:
            self.metrics['User Signups'].append((f"Day {day_num}", 45))
            self.metrics['Conversion Rate'].append((f"Day {day_num}", 0.27))
            self.metrics['Development Velocity'].append((f"Day {day_num}", 5))
            self.metrics['Customer Satisfaction'].append((f"Day {day_num}", 0.8))   
    def run(self):
        """Run the full startup simulation"""
        for period, task in MILESTONES:
            print(f"\n=== {period}: {task} ===")
            self._execute_milestone(period, task)
        
        metrics_chart = SimulationVisualizer.plot_startup_metrics(self.metrics)
        team_graph = SimulationVisualizer.create_agent_relationship_graph(self.agent_info)
        
        print(f"\n📊 Simulation metrics saved to {metrics_chart}")
        print(f"👥 Team dynamics graph saved to {team_graph}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", required=True, help="Product idea to simulate")
    args = parser.parse_args()
    
    sim = StartupSimulation(args.product)
    sim.run()