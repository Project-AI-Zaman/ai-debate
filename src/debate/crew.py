from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class Debate():
    """Debate crew"""

    ############## Agents ##############
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def proposerAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['proposerAgent'],
            verbose=True
        )

    @agent
    def opposerAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['opposerAgent'],
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'],
            verbose=True
        )

    ############## Tasks ##############
    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'],
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'],
        )

    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""
        return Crew(
            agents=self.agents,  # from @agent methods above
            tasks=self.tasks,    # from @task methods above
            process=Process.sequential,
            verbose=True,
        )
