# import numpy as np
# import matplotlib.pyplot as plt
# x = np.random.uniform(0.0,5.0,1000)
#
# plt.hist(x,5)
# plt.show()

# import numpy
# import matplotlib.pyplot as plt
#
# x = numpy.random.normal(5.0, 10.0, 1000)
#
# plt.hist(x, 100)
# plt.show()
# plt.close()

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)


plt.scatter(x, y)
plt.show()