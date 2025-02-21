try:
    import lessons
    print(f"NumPy установлен. Версия: {numpy.__version__}")
except ImportError:
    print("NumPy не установлен.")