import logging 
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename="test.log", level=logging.DEBUG, 
					format="%(asctime)s:%(levelname)s:%(message)s"
					)
a = 'xdsfgs'
b = [1,4,4,5,5,5]
logging.debug("a = {}, b = {}".format(a,b))
