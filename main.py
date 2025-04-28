from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


# Step 1: Access OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Step 2: Create an agent
blog_writer = Agent(
    role="Tech Blog Writer",
    goal="Write a simple blog post on futuristic uses of AI agents and cloud computing",
    backstory="You are an expert in AI and cloud computing technologies, skilled at writing easy-to-understand blogs.",
    verbose=True
)

# Step 3: Define a task
write_blog = Task(
    description="Create a blog post explaining futuristic applications of AI agents integrated with cloud computing.",
    expected_output="A blog article with a title, introduction, 3-5 sections, and a conclusion.",
    agent=blog_writer
)

# Step 4: Assemble the crew
crew = Crew(
    agents=[blog_writer],
    tasks=[write_blog],
    verbose=True
)

# Step 5: Run it
result = crew.kickoff()

# Step 6: Save the blog post
with open("ai_cloud_blog.html", "w") as file:
    file.write("<html><body>")
    file.write(f"<h1>Blog Post</h1><p>{result}</p>")
    file.write("</body></html>")

print("Success! Blog saved as ai_cloud_blog.html")

