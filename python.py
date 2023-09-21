from TestEngineering import FileLoader
import config

files = FileLoader.GetFiles(config.inputDir)

for file in files:
    print(file)

dict = {
    "apple" : "red"
}