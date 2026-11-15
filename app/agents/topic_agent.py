from app.models.schemas import (
    ResearchRequest,
    ResearchPlan
)

def analyze_topic(request: ResearchRequest) -> ResearchPlan:

    if request.topic == "AI in Healthcare":
        return ResearchPlan(
            main_topic = "AI in Healthcare",
            subtopics = [
                "Medical Diagnosis",
                "Drug Discovery",
                "Clinical Decision Support",
                "Ethical Considerations"
            ],
            research_goals = [
                "Understand major AI applications",
                "Evaluate benefits",
                "Analyze limitations"
            ]
        )

    return ResearchPlan(
        main_topic=request.topic,
        subtopics=["General Overview"],
        research_goals=["Understand the topic"]
    )