import pandas as pd
from groq import Groq


class Task:
    def __init__(self, name, objective, deadline):
        self.name = name
        self.objective = objective
        self.deadline = deadline

    def get_ai_encouragement(self):
        try:
            client = Groq(api_key=api_key)
            prompt = f"The user is doing {self.objective}. Deadline: {self.deadline}. Give a consistent compliment and quote."
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile"
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Sorry,there seems to be a problem : {e})"


data = {
    "objective": ["mock", "homework", "projects", "notes"],
    "deadlines": ["1day", "3day", "2day", "4day"]
}
df = pd.DataFrame(data, index=["task1", "task2", "task3", "task4"])
df.to_csv("tasks.csv")
df = pd.read_csv("tasks.csv", index_col=0)



 
def show_menu():
   
    print("      Task Of 4 Days     ")
    
    
    print(df[['objective', 'deadlines']])
    


while True:
   
    
    action = input("Enter 'view [ID]', 'delete [ID]', or 'exit': ").strip().lower()

    if action == "exit":
        print("Consistent is important. have a nice day.")
        break

    try:
        
        parts = action.split()
        cmd = parts[0]
        task_id = parts[1]

        if cmd == "delete":
            df = df.drop(task_id)
            df.to_csv("tasks.csv")
            print(f"task {task_id} deleted successfully.")
            continue

        elif cmd=="add":
             
        
            new_objective=parts[2]
            new_deadline=parts[3]
            df.loc[task_id]=[new_objective,new_deadline]
            df.to_csv("tasks.csv")
            print(f"task updated successfully")
            continue

        elif cmd == "view":
            row = df.loc[task_id]
           
            current_task = Task(task_id, row["objective"], row["deadlines"])
            print(current_task.get_ai_encouragement())

    except (KeyError, IndexError):
        print(f"Sorry, that Task ID is not in the system.")
    finally:
        print("Keep going good, don't break this consistency")

        
