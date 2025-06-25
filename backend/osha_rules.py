def check_osha_reportability(text: str):
    # Basic keyword checks
    rules_triggered = []

    if "hospitalized" in text.lower() or "admitted" in text.lower():
        rules_triggered.append("Hospitalization → Must report within 24 hours")
    if "fatal" in text.lower() or "death" in text.lower():
        rules_triggered.append("Fatality → Must report within 8 hours")
    if "amputation" in text.lower():
        rules_triggered.append("Amputation → Must report within 24 hours")
    if "lost eye" in text.lower() or "loss of eye" in text.lower():
        rules_triggered.append("Loss of eye → Must report within 24 hours")

    if rules_triggered:
        return {
            "report_required": True,
            "reason": rules_triggered
        }
    else:
        return {
            "report_required": False,
            "reason": ["No OSHA-reportable keywords detected"]
        }
