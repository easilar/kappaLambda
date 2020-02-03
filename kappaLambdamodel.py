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
		self.modelBuilder.factory_("expr::%s(\"@0*@0\", kappa_lambda)" % (name))
		print 'Scaling %s/%s by kappa_lambda square' % (bin, process)
		return name
	else:
        	return 1

kLambda = kappaLambda()
