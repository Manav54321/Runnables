from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass

class LLM(Runnable):
    def __init__(self):
        print("LLM created")

    def invoke(self, prompt):
        responses = [
            "Mumbai is the metro city of India",
            "Delhi is the capital of India",
            "Surat is the biggest diamond hub across the world, located in Gujarat, North(India)"
        ]
        return {"response": random.choice(responses)}

    def predict(self, prompt):
        responses = [
            "Mumbai is the metro city of India",
            "Delhi is the capital of India",
            "Surat is the biggest diamond hub across the world, located in Gujarat, North(India)"
        ]
        return {"response": random.choice(responses)}
        print("This method is gonna be deprecated in future!!!")  

class PromptTemplate(Runnable):
    def __init__(self, template, input_variable):
        self.template = template
        self.input_variable = input_variable

    def invoke(self, input_dict):
        return {"response": self.template.format(**input_dict)}

    def format(self, input_dict):
        return self.template.format(**input_dict)
        print("This method is gonna be deprecated in future!!!")

class StrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_dict):
        return input_dict["response"]

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data

template = PromptTemplate(
    template="Tell me a fact about {topic}",
    input_variable=["topic"]
)

template1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variable=["topic"]
)

template2 = PromptTemplate(
    template="Write a summary about the following {response}",
    input_variable=["response"]
)

parser = StrOutputParser()
llm = LLM()

chain1 = RunnableConnector([template1, llm])
print("Chain1 Output:", chain1.invoke({"topic": "India"}))

chain2 = RunnableConnector([template2, llm, parser])
chain = RunnableConnector([chain1, chain2])
print("Final Chain Output:", chain.invoke({"topic": "India"}))
