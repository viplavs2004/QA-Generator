
# Prompt template for generating the initial set of questions.
prompt_template = """
You are an expert at creating questions based on the provided text.
Your goal is to prepare a user for an exam or test on the material.
You do this by asking questions about the text below:

------------
{text}
------------

Create questions that will prepare the user for their test.
Make sure not to lose any important information.
Do not create more than 10 questions.

QUESTIONS:
"""

# Prompt template for refining the questions with additional context.
# This can be used in the 'refine' chain type to improve the questions iteratively.
refine_template = """
You are an expert at creating practice questions based on material and documentation.
Your goal is to help a user prepare for a test.
We have received some practice questions to a certain extent: {existing_answer}.
We have the option to refine the existing questions or add new ones
(only if necessary) with some more context below.
------------
{text}
------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the original questions.

QUESTIONS:
"""
