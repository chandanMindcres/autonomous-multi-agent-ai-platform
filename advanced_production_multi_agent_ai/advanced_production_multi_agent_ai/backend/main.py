from fastapi import FastAPI
from pydantic import BaseModel
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.critic import critic_agent
from memory.vector_memory import MemoryStore

app = FastAPI()

memory = MemoryStore()

class TaskRequest(BaseModel):
    task: str

@app.post("/run-task")
async def run_task(request: TaskRequest):
    plan = planner_agent(request.task)
    execution = executor_agent(plan)
    review = critic_agent(execution)

    memory.add({
        "task": request.task,
        "plan": plan
    })

    return {
        "task": request.task,
        "plan": plan,
        "execution": execution,
        "review": review,
        "memory_size": len(memory.get_all())
    }
