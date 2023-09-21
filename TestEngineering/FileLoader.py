import os
import re

FILE_NAME_REGEX = "\d{8}\w{1}\d{6}\w{1}"
FILE_NAME_EXTENSION = ".txt"


def GetFiles(inputDir: str):
    validFilePathsToReturn = []
    filesInDirectory = os.listdir(inputDir)
    for file in filesInDirectory:
        fileFullPath = os.path.join(inputDir, file)
        if checkFileNameIsCorrect(file) and checkFileSizeIsCorrect(fileFullPath):
            validFilePathsToReturn.append(fileFullPath)
        else:
            continue
    return validFilePathsToReturn


def checkFileNameIsCorrect(fileName: str):
    if not fileName.endswith(FILE_NAME_EXTENSION):
        return False
    if not re.match(FILE_NAME_REGEX, fileName):
        return False
    return True


def checkFileSizeIsCorrect(filePath: str):
    if os.path.getsize(filePath) == 0:
        return False
    return True
