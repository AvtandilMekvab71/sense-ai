from app.models.schemas import ResearchRequest
from app.agents.topic_agent import analyze_topic

request = ResearchRequest(
    topic="AI in Healthcare",
    paper_type="Research Paper",
    word_limit=3000,
    requirements="Use peer-reviewed academic sources"
)

plan = analyze_topic(request)

print("\nMain Topic:")
print(plan.main_topic)

print("\nSubtopics:")
for topic in plan.subtopics:
    print(f"- {topic}")

print("\nResearch Goals:")
for goal in plan.research_goals:
    print(f"- {goal}")