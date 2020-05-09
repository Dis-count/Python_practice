#GaussianNB differ from MultinomialNB in these two method:
# _calculate_feature_prob, _get_xj_prob
class GaussianNB(MultinomialNB):
        """
        GaussianNB inherit from MultinomialNB,so it has self.alpha
        and self.fit() use alpha to calculate class_prior
        However,GaussianNB should calculate class_prior without alpha.
        Anyway,it make no big different

        """
        #calculate mean(mu) and standard deviation(sigma) of the given feature
        def _calculate_feature_prob(self,feature):
                mu = np.mean(feature)
                sigma = np.std(feature)
                return (mu,sigma)

        #the probability density for the Gaussian distribution
        def _prob_gaussian(self,mu,sigma,x):
                return ( 1.0/(sigma * np.sqrt(2 * np.pi)) *
                        np.exp( - (x - mu)**2 / (2 * sigma**2)) )

        #given mu and sigma , return Gaussian distribution probability for target_value
        def _get_xj_prob(self,mu_sigma,target_value):
                return self._prob_gaussian(mu_sigma[0],mu_sigma[1],target_value)
