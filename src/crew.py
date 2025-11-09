from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from ai import load_model

@CrewBase
class CodeCommentCrew():
    """Code Comment Crew"""
    def __init__(self):
        self.agents_config="config/agents.yaml"
        self.tasks_config="config/tasks"

#----------AGENTS--------------
    @agent
    def comment_adder(self)->Agent:
        print("In a First Agent")
        #With the help of the CrewBase Decorator we can easily assign the config
        cfg_agent=self.agents_config["comment_adder"]
        # print(f"In comment_adder,this is the cfg_agent::{cfg_agent}")
        llm=load_model(cfg_agent["llm"])

        return Agent(
            # config=cfg_agent,
            role=cfg_agent["role"],
            goal=cfg_agent["goal"],
            backstory=cfg_agent["backstory"],
            llm=llm,
            verbose=True
        )
    
#---------TASKS---------------
    @task
    def comment_adder_task(self)->task:
        print("In a First Task")
        cfg_task=self.tasks_config["comment_adder_task"]
        
        return Task(
            config=cfg_task,
        )
    


#---------CREW---------------
    @crew
    def crew(self)->Crew:
        print("Now Finally in a Crew")
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )