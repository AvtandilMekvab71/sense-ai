from pydantic import BaseModel


class ResearchRequest(BaseModel):
    topic: str
    paper_type: str
    word_limit: int
    requirements: str


class ResearchPlan(BaseModel):
    main_topic: str
    subtopics: list[str]
    research_goals: list[str]