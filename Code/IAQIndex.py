def BreakingPoints(pollutant, value):
    if pollutant == "PM10":
        if 0.0 <= value <= 54.0:
            return 0.0, 54.0
        elif 55.0 <= value <= 154.0:
            return 55.0, 154.0
        elif 155.0 <= value <= 254.0:
            return 155.0, 254.0
        elif 255.0 <= value <= 354.0:
            return 255.0, 354.0
        elif 355.0 <= value <= 424.0:
            return 355.0, 424.0
        elif 425.0 <= value <= 504.0:
            return 425.0, 504.0
        elif 505.0 <= value <= 604.0:
            return 505.0, 604.0

    elif pollutant == "PM2.5":
        if 0.0 <= value <= 15.4:
            return 0.0, 15.4
        elif 15.5 <= value <= 40.4:
            return 15.5, 40.4
        elif 40.5 <= value <= 65.4:
            return 40.5, 65.4
        elif 65.5 <= value <= 150.4:
            return 65.5, 150.4
        elif 150.5 <= value <= 250.4:
            return 150.5, 250.4
        elif 250.5 <= value <= 350.4:
            return 250.5, 350.4
        elif 350.5 <= value <= 500.4:
            return 350.5, 500.4

########################################################################################################################
# Parameters: (1) pollutant is selfexplanatory and (2) concentrations parameter repsesents the value of each pollutant #
# measured in the appropreriate units.                                                                                 #
########################################################################################################################
def AirQualityIndex(pollutant, concentration):
    # Pollutant abbreviation
    p = pollutant
    # Concentrantation of pollutant
    Cp = concentration
    # Upper & Lower Breaking Points
    LBP, UBP = BreakingPoints(p, Cp)
    # Determine breaking points for air quality index
    IndexLB = 0
    IndexUB = 0
    if p == "PM10":
        if 0.0 <= Cp <= 54.0:
            IndexLB = 0
            IndexUB = 50
        elif 55.0 <= value <= 154.0:
            IndexLB = 51
            IndexUB = 100
        elif 155.0 <= Cp <= 254.0:
            IndexLB = 101
            IndexUB = 150
        elif 255.0 <= Cp <= 354.0:
            IndexLB = 151
            IndexUB = 200
        elif 355.0 <= Cp <= 424.0:
            IndexLB = 201
            IndexUB = 300
        elif 425.0 <= Cp <= 504.0:
            IndexLB = 301
            IndexUB = 400
        elif 505.0 <= Cp <= 604.0:
            IndexLB = 401
            IndexUB = 500

    elif p == "PM2.5":
        if 0.0 <= Cp <= 15.4:
            IndexLB = 0
            IndexUB = 50
        elif 15.5 <= Cp <= 40.4:
            IndexLB = 51
            IndexUB = 100
        elif 40.5 <= Cp <= 65.4:
            IndexLB = 101
            IndexUB = 150
        elif 65.5 <= Cp <= 150.4:
            IndexLB = 151
            IndexUB = 200
        elif 150.5 <= Cp <= 250.4:
            IndexLB = 201
            IndexUB = 300
        elif 250.5 <= Cp <= 350.4:
            IndexLB = 301
            IndexUB = 400
        elif 350.5 <= Cp <= 500.4:
            IndexLB = 401
            IndexUB = 500
    # Formula for IAQ index computation
    Ip = (Cp - LBP) * (IndexUB - IndexLB) / (UBP - LBP) + IndexLB
    return Ip

def HealthLevel(index):
    if 0 <= index <= 50:
        return "Good"
    elif 51 <= index <= 100:
        return "Moderate"
    elif 101 <= index <= 150:
        return "Unhealthy!"
    elif 151 <= index <= 200:
        return "Unhealthy"
    elif 201 <= index <= 300:
        return "Very unhealthy"
    else:
        return "Hazardous"
