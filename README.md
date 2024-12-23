What if you could write a program that used system prompts to create system prompts?

In order for a human prompt engineer to write a good system prompt, they need two things:

* Domain knowledge for whatever the system prompt is supposed to do
* Knowledge of writing good system prompts

Is the latter really necessary?

Meaning, what if you took content from a place like: https://www.promptingguide.ai/techniques/prompt_chaining

and used that as the beginning of a system prompt before supplying a definition of the domain knowledge, couldn't a LLM generate a scaffold of a system prompt for you?

And what if you used a Mixture of Agents approach to get multiple candidates of a system prompt scaffold as well as an aggregate for a human prompt engineer to then iterate over?

In theory, that would speed the process and that's what this repo aims to experiment with.

## V1 ##
First, I took the [general tips from the Prompt Engineerin Guide](https://www.promptingguide.ai/introduction/tips) and reformatted them into markdown

I did the same for zero-shot prompting

Then I wrote code that reads in a list of Markdown files and aggregates them into a system prompt and then goes and gets a Markdown that has domain data in it. Tested that with the 20-something engineer case.