
#Write model here:
def model(survey: dict = None):
    if not survey:
        return {"key" : "random feed"}
    else:
        return {"key" : "recommendations"}