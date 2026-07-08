from ai.build_prompt import build_prompt
from ai.model_integration import generate_response

def email_output(recipent, tone, purpose, length):
    prompt=build_prompt(recipent=recipent, tone=tone, purpose=purpose, length=length)
    output=generate_response(prompt=prompt)

    return output