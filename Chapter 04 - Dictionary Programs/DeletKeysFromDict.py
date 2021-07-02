sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keysToRemove = ["name", "salary"]
sampleDict={k : sampleDict[k] for k in sampleDict.keys() - keysToRemove}
print(sampleDict)