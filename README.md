# kappaLambda
Some tests for kappaLambda study


```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
```
```
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v8.0.1
scramv1 b clean; scramv1 b # always make a clean build
```
```
cd $CMSSW_BASE/src/
git clone https://github.com/easilar/kappaLambda.git
cd kappaLambdaAna 
cp kappaLambdamodel.py ../HiggsAnalysis/CombinedLimit/python/kappaLambdamodel.py
```
```
text2workspace.py datacard.txt -P HiggsAnalysis.CombinedLimit.kappaLambdamodel:kLambda -o testWSdatacard.root
combine -M AsymptoticLimits testWSdatacard.root
```
Run with the existing kappalambda model from combinetools
```
text2workspace.py datacard_ggh.txt -P HiggsAnalysis.CombinedLimit.TrilinearCouplingModels:trilinearHiggs -o testWSdatacard_ggh.root
```
