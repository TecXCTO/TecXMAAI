from src.agent import DeepResearchAgent

def main():
    topic = input("Enter research topic: ")
    agent = DeepResearchAgent()
    
    print("\n--- Planning Research ---")
    plan = agent.plan_research(topic)
    print(plan)
    
    # In a full implementation, you would execute searches here.
    print("\n--- Generating Mock Report ---")
    report = agent.synthesize_report("Simulated findings based on the plan.")
    print(report)

if __name__ == "__main__":
    main()
