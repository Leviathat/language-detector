from lingua import Language, LanguageDetectorBuilder

class LanguageDetector:
    
    languages = [Language.KAZAKH, Language.RUSSIAN]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()

    def detect_language(self, text: str) -> Language:
        detector = LanguageDetectorBuilder.from_languages(*self.languages).build()
        return detector.detect_language_of(text)
