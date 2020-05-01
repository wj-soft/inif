from stocklab.agent.ebest import EBest

ebest = EBest("DEMO")
ebest.login()

result = ebest.get_code_list("ALL")

print(result)