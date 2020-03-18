from HiggsAnalysis.CombinedLimit.PhysicsModel import *
from HiggsAnalysis.CombinedLimit.SMHiggsBuilder import SMHiggsBuilder
from HiggsAnalysis.CombinedLimit.LHCHCGModels import LHCHCGBaseModel
import ROOT, os


class kappaLambda(PhysicsModel):

    def doParametersOfInterest(self):
        """Create POI out of signal strength and MH"""
        self.modelBuilder.doVar("kappa_lambda[1,0,4]")
        pois = 'kappa_lambda'
        self.modelBuilder.doSet("POI",pois)

    def getYieldScale(self, bin, process):
	name = "my_scale"
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        if process=="ggH":
		self.modelBuilder.factory_("expr::%s(\"@0\", kappa_lambda)" % (name))
		print 'Scaling %s/%s by kappa_lambda' % (bin, process)
		return name
	else:
        	return 1

kLambda = kappaLambda()



class kappaLambda_real(PhysicsModel):

    def doParametersOfInterest(self):
        """Create POI out of signal strength and MH"""
        self.modelBuilder.doVar("kappa_lambda[1,-20,20]")
        pois = 'kappa_lambda'
        self.modelBuilder.doSet("POI",pois)

    def getYieldScale(self, bin, process):
	energy = "13TeV"
	production = "ggH"
	cXSmap_13  = {"ggH":0.66e-2,"qqH":0.64e-2,"WH":1.03e-2,"ZH":1.19e-2,"ttH":3.51e-2}
	EWKmap_13  = {"ggH":1.049,"qqH":0.932,"WH":0.93,"ZH":0.947,"ttH":1.014}
	cXSmaps = {"13TeV":cXSmap_13}
	C1_map = cXSmaps[energy]
	EWK = EWKmap_13[production]
	dZH = -1.536e-3
	decay = "Htt"
	name = "kVkFkl_XSBRscal_%s_%s_%s" % (production,decay,energy)
        if process=="ggH":
                self.modelBuilder.factory_("expr::kVkFkl_XSscal_%s_%s(\"((@0-1)*%g/%g)/((1-(@0*@0-1)*%g))\",kappa_lambda)"\
	       				%(production,energy,C1_map[production],EWK,dZH))
		print 'Scaling %s/%s by real kappa_lambda function' % (bin, process)
		return name
	else:
        	return 1

kLambda_real = kappaLambda_real()
