def build_prompt(recipent, tone, purpose, length):
    prompt=f"""
    you are an experienced email writer your job is to write emails for
    living. You are really good at it.
    You have to write the email based on the information below:

    recipent: {recipent}
    tone of the email: {tone}
    purpose of the email: {purpose}
    length of the email: {length}

    Give the response following the below guidlines strictly:
    - Return ONLY the Email.
    - Do not explain anything.
    - Do not add bullet points.

    """
    return prompt