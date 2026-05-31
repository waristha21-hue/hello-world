def greet(name, greeting="Hello"):
    """Return a greeting string."""
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    print(greet("World"))
