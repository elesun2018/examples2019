
import os
import folium
import numpy as np
 
data=[[	39.90403	,	116.407526	,	23014.59	]	,
[	39.084158	,	117.200983	,	16538.19	]	,
[	38.042309	,	114.514862	,	5440.6	]	,
[	37.87059	,	112.548879	,	2735.34	]	,
[	40.842585	,	111.74918	,	3090.52	]	,
[	41.805698	,	123.431474	,	7272.31	]	,
[	38.914003	,	121.614682	,	7731.64	]	,
[	43.817071	,	125.323544	,	5530.03	]	,
[	45.803775	,	126.534967	,	5751.21	]	,
[	31.230416	,	121.473701	,	25123.45	]	,
[	32.060255	,	118.796877	,	9720.77	]	,
[	30.274084	,	120.15507	,	10050.21	]	,
[	29.874556	,	121.550357	,	8003.61	]	,
[	31.820586	,	117.227239	,	5660.27	]	,
[	26.074507	,	119.296494	,	5618.08	]	,
[	24.479833	,	118.089425	,	3466.03	]	,
[	28.682892	,	115.858197	,	4000.01	]	,
[	36.651216	,	117.119999	,	6100.23	]	,
[	36.067082	,	120.382639	,	9300.07	]	,
[	34.746599	,	113.625368	,	7311.52	]	,
[	30.593098	,	114.305392	,	10905.6	]	,
[	28.228209	,	112.938814	,	8510.13	]	,
[	23.129162	,	113.264434	,	18100.41	]	,
[	22.543099	,	114.057868	,	17502.86	]	,
[	22.817002	,	108.366543	,	3410.09	]	,
[	20.044001	,	110.198293	,	1161.96	]	,
[	29.563009	,	106.551556	,	15717.27	]	,
[	30.572269	,	104.066541	,	10801.16	]	,
[	26.647661	,	106.630153	,	2891.16	]	,
[	24.880095	,	102.832891	,	3968.01	]	,
[	29.645554	,	91.140856	,	376.73	]	,
[	34.341568	,	108.940174	,	5801.2	]	,
[	36.061089	,	103.834303	,	2095.99	]	,
[	36.617144	,	101.778228	,	1131.62	]	,
[	38.487193	,	106.230909	,	1493.86	]	,
[	43.825592	,	87.616848	,	2631.64	]	]
#data = (np.random.normal(size=(100, 3)) *
#        np.array([[1, 1, 1]]) +
#       np.array([[48, 5, 1]])).tolist()
 
from folium.plugins import HeatMap
 
m = folium.Map([ 33., 113.], tiles='stamentoner', zoom_start=5)
 
HeatMap(data).add_to(m)
 
m.save(os.path.join('map3.html'))
 
m
