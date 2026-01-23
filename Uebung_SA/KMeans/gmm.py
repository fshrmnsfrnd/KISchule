# Datasets lade
from sklearn.datasets import load_breast_cancer
bc = load_breast_cancer()
x = bc.data
y = bc.target

print(y)

# Anzahl Cluster bestimmen
from Elbow_Chart_Funktion import create_elbow_chart
kmeans_estimator,ineritas = create_elbow_chart(x, 10)
kmeans = kmeans_estimator[1]

#Gaussian
from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=2, means_init=kmeans.cluster_centers_, max_iter=300)

gmm.fit(x)
print(gmm.predict(x))
print(gmm.precisions_)