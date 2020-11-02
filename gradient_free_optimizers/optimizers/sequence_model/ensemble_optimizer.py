# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from .exp_imp_based_opt import ExpectedImprovementBasedOptimization
from .surrogate_models import EnsembleRegressor


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcessRegressor


class EnsembleOptimizer(ExpectedImprovementBasedOptimization):
    def __init__(
        self,
        search_space,
        estimators=[
            GradientBoostingRegressor(n_estimators=10),
            SVR(),
            DecisionTreeRegressor(),
            GaussianProcessRegressor(),
        ],
        xi=0.01,
        warm_start_sbom=None,
        rand_rest_p=0.03,
    ):
        super().__init__(search_space)
        self.regr = EnsembleRegressor(estimators)
        self.xi = xi
        self.warm_start_sbom = warm_start_sbom
        self.rand_rest_p = rand_rest_p
