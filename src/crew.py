from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from ai import load_model


@CrewBase
class CodeCommentCrew():
    """Code Comment Crew"""
    agents_config="config/agents.yaml"
    tasks_config="config/tasks"

#----------AGENTS--------------
    @agent
    def comment_adder(self)->Agent:

        #With the help of the CrewBase Decorator we can easily assign the config
        cfg_agent=self.agents_config["comment_adder"]
        llm=load_model(cfg_agent["llm"])

        return Agent(
            config=cfg_agent,
            llm=llm,
            verbose=True
        )
    
#---------TASKS---------------
    @task
    def comment_adder_task(self)->task:
        cfg_task=self.tasks_config["comment_adder_task"]
        
        return Task(
            config=cfg_task,
        )
    


#---------CREW---------------
    @crew
    def crew(self)->Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )