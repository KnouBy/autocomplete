from providers.provider import Provider


def inject(provider: Provider):
    """
    Used as a decorator to inject some service provider
    """
    def decorator(func):
        injection = provider.provide()

        def inject_dependency(*args, **kwargs):
            return func(injection, *args, **kwargs)

        return inject_dependency
    return decorator
