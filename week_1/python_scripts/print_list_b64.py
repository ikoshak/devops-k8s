import base64
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

for step in steps:
    step_code_base64 = base64.b64encode(step.encode()).decode()
    result = f"b'{step_code_base64}'"
    print(result)