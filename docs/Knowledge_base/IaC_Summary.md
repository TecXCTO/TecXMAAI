#Centrlize IaC Schemas

```

Store IaC schema in a Markdown file
A simple technique you can use to give the AI more context is to store your Infrastructure as Code in a simple-to-access file.

IaC is the code representing information such as:

Table names
S3 buckets and prefixes
Production logs
Permissions,
When you’ve been working in a company for a while, you probably have all of this information memorized. You remember the table names of the most important tables, and which S3 buckets store what, and in which prefixes.

However, your coding agent doesn’t have simple access to this, unless you provide them access. The simplest way to do this is:

Store all your IaC repositories in one folder
Tell a coding agent to go through all of these repositories and summarize all the IaC in a single Markdown file
Now you can refer to this Markdown file whenever you want your agent to work with anything IaC



```
