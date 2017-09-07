import logging
import asyncio
import random
import json
import aiocoap.resource as resource
import aiocoap

__author__ = __maintainer__ = "Helder Moreira"
__email__ = "helderm14@ua.pt"
__version__ = "1.0.0"

def random_color(): 
	rgbhex = []
	for i in range(3):
		tmp = hex(random.randint(0,255))[2:]
		if len(tmp) == 1: tmp='0'+tmp
		rgbhex.append(tmp)
	rgbhex.reverse()
	return '#'+''.join(rgbhex)

class BoolResource(resource.Resource):
	def __init__(self, initial=False):
		super(BoolResource, self).__init__()
		self.content = initial

	def get_value(self):
		return self.content

	async def render_get(self, request):
		data = {
			'payload': self.content
		}
		return aiocoap.Message(payload=json.dumps(data).encode('ascii'))

	async def render_put(self, request):
		payload = ("ERROR: Value not changed").encode('utf8')
		try:
			data = json.loads(request.payload)
			if type(data['payload']) == bool:
				self.content = data['payload']
				payload = ("Accepted as JSON. Value changed").encode('utf8')
		except:
			try:
				data = request.payload.decode()
				if data.lower() in ['true', 'false']:
					self.content = data.lower() == 'true'
					payload = ("Accepted as string. Value changed").encode('utf8')
			except:
				pass
		return aiocoap.Message(payload=payload)

class TemperatureResource(resource.ObservableResource):
	def __init__(self):
		super(TemperatureResource, self).__init__()
		self.notify()

	def notify(self):
		self.updated_state()
		asyncio.get_event_loop().call_later(6, self.notify)

	def update_observation_count(self, count):
		if count:
			print(count)
		else:
			print(count)

	async def render_get(self, request):
		data = {
			'payload': random.randint(10,40)
		}
		return aiocoap.Message(payload=json.dumps(data).encode('ascii'))

class HumidityResource(resource.ObservableResource):
	def __init__(self):
		super(HumidityResource, self).__init__()
		self.notify()

	def notify(self):
		self.updated_state()
		asyncio.get_event_loop().call_later(6, self.notify)

	async def render_get(self, request):
		data = {
			'payload': random.randint(0,100)
		}
		return aiocoap.Message(payload=json.dumps(data).encode('ascii'))

class ColorResource(resource.ObservableResource):
	def __init__(self, randresource):
		super(ColorResource, self).__init__()
		self.color = self.lcolor = '#0000ff'
		self.randRes = randresource
		self.notify()

	def notify(self):
		if self.randRes.get_value() or self.color != self.lcolor:
			self.lcolor = self.color
			self.updated_state()
		asyncio.get_event_loop().call_later(6, self.notify)

	async def render_get(self, request):
		if self.randRes.get_value():
			self.color = self.lcolor = random_color()
		data = {
			'payload': self.color
		}
		return aiocoap.Message(payload=json.dumps(data).encode('ascii'))

	async def render_put(self, request):
		print('PUT payload: %s' % request.payload)
		self.color = request.payload.decode()
		payload = ("New color accepted").encode('utf8')
		return aiocoap.Message(payload=payload)

def main():
	root = resource.Site()

	randColor = BoolResource(False)

	tempRes = TemperatureResource()
	humRes = HumidityResource()
	colorRes = ColorResource(randColor)

	root.add_resource(('.well-known', 'core'), resource.WKCResource(root.get_resources_as_linkheader))

	root.add_resource(('temperature',), tempRes)
	root.add_resource(('humidity',), humRes)
	root.add_resource(('color',), colorRes)

	root.add_resource(('settings', 'random_color'), randColor)

	asyncio.Task(aiocoap.Context.create_server_context(root))
	asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
	main()
