# File: ajCogswell_nestedTelemetry.py
# Author: Aj Cogswell
# Date: 11/24/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Recursively finds min, max, subsystem min, and subsystem max of data within simplifiedTelemetry500.txt. Outputs to analysis_log.txt.
# Collaborations: None


def getTelemetryData():
    telemetryFile = "simplifiedTelemetry500.txt"
    with open(telemetryFile, "r") as file:
        data = file.readlines()
    return data, telemetryFile


def readData(
    masterlist, subSysSelect, currSegment, subsys, listpos, segMin, segMax, index, data
):
    print(masterList[index])


def interpretData(
    data,
    index,
    masterList,
    currSegment,
    subsys,
    listPos,
    min,
    max,
    subSysSelect,
    segMin,
    segMax,
):
    if index >= len(data):
        return masterList, min, max, segMin, segMax

    if masterList is None:
        masterList = list()

    line = data[index].strip()

    if "[SEGMENT_ID:" in line:
        currSegment = line[12:-1:]
        tempDict = dict()
        tempDict["missionSegment"] = currSegment
        masterList.append(tempDict)
        listPos = int(line[13:-1:]) - 1
    elif "[SUBSYSTEM:" in line:
        subsys = line[11:12:]
        masterList[listPos][subsys] = dict()
    else:
        if "," in line:
            tempDict = dict()
            time, val = line.split(",")
            time = int(time)
            val = float(val)

            if max is None or val > max:
                max = val
            if subsys == subSysSelect:
                if segMin is None or val < segMin:
                    segMin = val

                if segMax is None or val > segMax:
                    segMax = val

            if min is None or val < min:
                min = val
            masterList[listPos][subsys][time] = val

    return interpretData(
        data,
        index + 1,
        masterList,
        currSegment,
        subsys,
        listPos,
        min,
        max,
        subSysSelect,
        segMin,
        segMax,
    )


data, telemetryFile = getTelemetryData()
currSegment = input("Enter Subsystem Target (P, T, G): ").strip().upper()
masterList, min, max, segMin, segMax = interpretData(
    data, 0, None, None, None, 0, None, None, currSegment, None, None
)
outFile = "analysis_log.txt"

with open(outFile, "w") as output:
    output.write(f"File analyzed: {telemetryFile}")
    output.write(f"Total pulses analyzed: {len(data)}\n")
    output.write(f"Target subsystem: {currSegment}\n")
    output.write(f"Overall max: {max}\n")
    output.write(f"Overall min: {min}\n")
    output.write(f"Subsystem max: {segMax}\n")
    output.write(f"Subsystem min: {segMin}\n")
    print(f"Wrote to {outFile}!")
