class ValidationResult:
    def __init__(self, code, severity, message):
        self.code = code
        self.severity = severity
        self.message = message

    def to_dict(self):
        return {
            "code": self.code,
            "severity": self.severity,
            "message": self.message
        }
