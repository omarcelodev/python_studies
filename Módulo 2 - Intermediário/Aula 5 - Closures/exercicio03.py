def prefixo(x):
    def formatar(y):
        return x + y
    return formatar

log = prefixo("[LOG] ")
print(log("erro"))
