# kappaLambda
Some tests for kappaLambda study

text2workspace.py datacard.txt -P HiggsAnalysis.CombinedLimit.kappaLambdamodel:kLambda -o testWSdatacard.root

combine -M AsymptoticLimits testWSdatacard.root
