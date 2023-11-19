from datetime import datetime


def check_technologies(description: str) -> list:
    result = []
    if any(key in description.lower() for key in ["python", "python3"]):
        result.append("Python")
    if any(key in description.lower() for key in ["django"]):
        result.append("Django")
    if any(key in description.lower() for key in ["drf", "rest framework"]):
        result.append("DRF")
    if any(key in description.lower() for key in ["fastapi"]):
        result.append("FastAPI")
    if any(key in description.lower() for key in ["flask"]):
        result.append("Flask")
    if any(key in description.lower() for key in ["git"]):
        result.append("Git")
    if any(key in description.lower() for key in ["celery"]):
        result.append("Celery")
    if any(key in description.lower() for key in ["sql"]):
        result.append("SQL")
    if any(key in description.lower() for key in [" orm", "object relational mapper", "sqlalchemy"]):
        result.append("ORM")
    if any(key in description.lower() for key in ["docker"]):
        result.append("Docker")
    if any(key in description.lower() for key in ["aws", "azure"]):
        result.append("AWS/Azure")
    if any(key in description.lower() for key in ["linux"]):
        result.append("Linux")
    if any(key in description.lower() for key in ["js", "javascript", "java script"]):
        result.append("JS")
    if any(key in description.lower() for key in ["react", "angular", " vue"]):
        result.append("Frontend")
    if any(key in description.lower() for key in ["oop", "solid"]):
        result.append("OOP/SOLID")
    if any(key in description.lower() for key in ["nosql"]):
        result.append("NoSQL")
    if any(key in description.lower() for key in ["networking", "udp", "tcp"]):
        result.append("Networking")
    if any(key in description.lower() for key in ["html", "css"]):
        result.append("HTML/CSS")
    if any(key in description.lower() for key in ["algorithm", "data structure"]):
        result.append("Algorithms and data structures")
    if any(key in description.lower() for key in ["async"]):
        result.append("Asyncio")

    return result
