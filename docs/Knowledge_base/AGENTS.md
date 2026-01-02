# Fill gap and Memorize

```
Notice when your coding agent is missing context
Another important point is to be alert to when your AI is missing context. If you didn’t summarize your IaC (as explained in the last section), you’ll probably notice the agent is always:

Listing all table names
Reasoning about which table is the correct one to access now
Try accessing one table, and sometimes be wrong, and have to try another table
This is a result of your coding agent missing important context. Whenever you notice a pattern like this, you should immediately interrupt and inform the coding agent:

"
When you look for documents, you can find them in the table called
DocumentTable. Memorize this in AGENTS.md
"


Now the agent will remember this for next time, and you’ll save a lot of time and tokens.

I urge you to always look for situations where your coding agent is struggling. If it’s taking longer than usual for a task, it’s usually because it’s missing context, and it’s your job to provide that context to the AI coding agent.

```
