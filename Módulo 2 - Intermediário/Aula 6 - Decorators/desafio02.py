def repetir(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
        
@repetir(3)
def minha_função():
    print("Executando função")

minha_função()

