from sklearn.datasets import load_iris
from sklearn2pmml.statsmodels import StatsModelsClassifier, StatsModelsRegressor
from statsmodels.api import Logit, MNLogit
from unittest import TestCase

import numpy

class StatsModelsClassifierTest(TestCase):

	def test_binary_classification(self):
		iris_X, iris_y = load_iris(return_X_y = True)
		iris_y = (iris_y == 1)
		classifier = StatsModelsClassifier(Logit)
		self.assertTrue(hasattr(classifier, "model_class"))
		classifier.fit(iris_X, iris_y)
		self.assertTrue(hasattr(classifier, "model_"))
		self.assertTrue(hasattr(classifier, "result_"))
		self.assertIsInstance(classifier.model_, Logit)
		self.assertEqual([False, True], classifier.classes_.tolist())
		species = classifier.predict(iris_X)
		self.assertEqual((150,), species.shape)
		self.assertEqual(classifier.classes_.tolist(), numpy.unique(species).tolist())
		species_proba = classifier.predict_proba(iris_X)
		self.assertEqual((150, 2), species_proba.shape)
		self.assertEqual(150, numpy.sum(species_proba))

	def test_multiclass_classification(self):
		iris_X, iris_y = load_iris(return_X_y = True)
		classifier = StatsModelsClassifier(MNLogit)
		self.assertTrue(hasattr(classifier, "model_class"))
		classifier.fit(iris_X, iris_y)
		self.assertTrue(hasattr(classifier, "model_"))
		self.assertTrue(hasattr(classifier, "result_"))
		self.assertIsInstance(classifier.model_, MNLogit)
		self.assertEqual([0, 1, 2], classifier.classes_.tolist())
		species = classifier.predict(iris_X)
		self.assertEqual((150,), species.shape)
		self.assertEqual(classifier.classes_.tolist(), numpy.unique(species).tolist())
		species_proba = classifier.predict_proba(iris_X)
		self.assertEqual((150, 3), species_proba.shape)
		self.assertEqual(150, numpy.sum(species_proba))

class StatsModelsRegressorTest(TestCase):

	def test_regression(self):
		pass