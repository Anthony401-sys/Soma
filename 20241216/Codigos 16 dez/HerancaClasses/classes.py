#coding: utf-8

class Camera(object):
	def __init__(self, marca, resolucao):
		self.marca = marca
		self.resolucao = resolucao
	def tirar_foto(self):
		print(f"Foto da camera {self.marca} usando {self.resolucao} megapixels")


class CameraCelular(Camera):
	def __init__(self, marca, resolucao, qde_cameras):
		#super().__init__(marca, resolucao)
		Camera.__init__(self, marca, resolucao)
		self.qde_cameras = qde_cameras
	def Aplicar_filtro(self, filtro):
		print(f'Aplicando o filtro {filtro}')
	def tirar_foto(self):
		print(f"Foto da camera de celular {self.marca} usando {self.resolucao} megapixels, com {self.qde_cameras}")


