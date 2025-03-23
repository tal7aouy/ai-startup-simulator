import matplotlib.pyplot as plt
import numpy as np
import os
from typing import Dict, List, Tuple

class SimulationVisualizer:
    """Visualization tools for the startup simulation"""
    
    @staticmethod
    def create_agent_relationship_graph(agents_info: Dict[str, Dict]):
        """Create a graph visualization of agent relationships"""
        try:
            import graphviz as gv
            dot = gv.Digraph(comment='Startup Team Dynamics')
            
            for agent_id, info in agents_info.items():
                dot.node(agent_id, f"{info['name']}\n{info['role']}")
            
            for agent_id, info in agents_info.items():
                for relation in info.get('relations', []):
                    dot.edge(agent_id, relation['to'], label=relation['type'])
            
            try:
                dot.render('agent_relationships', format='png', cleanup=True)
                return 'agent_relationships.png'
            except Exception as e:
                print(f"Error rendering graph: {e}")
                return _create_fallback_relationship_image(agents_info)
        except (ImportError, Exception) as e:
            print(f"Graphviz error: {e}")
            return _create_fallback_relationship_image(agents_info)

    @staticmethod
    def plot_startup_metrics(metrics: Dict[str, List[Tuple[str, float]]]):
        """Plot metrics over time using matplotlib"""
        fig, axs = plt.subplots(len(metrics), 1, figsize=(10, 3*len(metrics)))
        
        for i, (metric_name, data_points) in enumerate(metrics.items()):
            days = [point[0] for point in data_points]
            values = [point[1] for point in data_points]
            
            if len(metrics) > 1:
                ax = axs[i]
            else:
                ax = axs
                
            ax.plot(days, values, marker='o')
            ax.set_title(f'{metric_name} Over Time')
            ax.set_xlabel('Timeline')
            ax.set_ylabel(metric_name)
            ax.grid(True)
        
        plt.tight_layout()
        plt.savefig('startup_metrics.png')
        return 'startup_metrics.png'

def _create_fallback_relationship_image(agents_info):
    """Create a fallback image for agent relationships when graphviz is unavailable"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.axis('off')
    
    ax.set_title('Startup Team Dynamics')
    

    text = "Team Structure:\n\n"
    for agent_id, info in agents_info.items():
        text += f"• {info['name']} ({info['role']})\n"
        for relation in info.get('relations', []):
            text += f"  → {relation['type']} {relation['to']}\n"
    
    ax.text(0.1, 0.5, text, fontsize=12, va='center')
    
    plt.savefig('agent_relationships.png')
    return 'agent_relationships.png'