from langdet import language_detector

def main():
    text = """
    "'...рейс): аптасына 7 рет «Южное небо» әуе компаниясымен орындалады. Сондай-ақ биыл 1 шілдеден бастап Qazaq Air әуекомпаниясы аптасына 4 рейс жиілігімен (сейсенбі, бейсенбі, жұма және жексенбі күндері)...")
    
    """
    print(language_detector.detect_language(text))

if __name__ == "__main__":
    main()
