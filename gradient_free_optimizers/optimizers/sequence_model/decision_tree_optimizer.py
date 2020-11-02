# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from .exp_imp_based_opt import ExpectedImprovementBasedOptimization
from .surrogate_models import (
    RandomForestRegressor,
    ExtraTreesRegressor,
)

tree_regressor_dict = {
    "random_forest": RandomForestRegressor(n_estimators=10),
    "extra_tree": ExtraTreesRegressor(n_estimators=10),
}


class DecisionTreeOptimizer(ExpectedImprovementBasedOptimization):
    """Based on the forest-optimizer in the scikit-optimize package"""

    def __init__(
        self,
        search_space,
        tree_regressor="random_forest",
        xi=0.01,
        warm_start_sbom=None,
        rand_rest_p=0.03,
    ):
        super().__init__(search_space)
        self.regr = tree_regressor_dict[tree_regressor]
        self.xi = xi
        self.warm_start_sbom = warm_start_sbom
        self.rand_rest_p = rand_rest_p
