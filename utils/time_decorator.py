from datetime import datetime

def take_time(function):
    """Decorator to know the tima that takes a function executing

    Args:
        function
    """
    def wrapper(*args, **kwargs):
        before = datetime.now()
        function(*args, **kwargs)
        after = datetime.now()
        final_time = (after-before).microseconds
        final_time = final_time / 1000        
        return float('{:.3}'.format(final_time))
    return wrapper
