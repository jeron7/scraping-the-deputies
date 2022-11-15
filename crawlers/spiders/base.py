import scrapy
from scrapy.selector import Selector

class BaseSpider(scrapy.Spider):
	gender = None

	def parse(self, response):
		deputy = {}
		informacoes_dep = response.xpath('//ul[@class="informacoes-deputado"]').get()
		
		def info_pessoal(info):
			return Selector(text=informacoes_dep).xpath(f'//li[span[contains(text(), "{info}")]]/text()').get()[1:]

		deputy['nome'] = info_pessoal("Nome Civil:")
		deputy['genero'] = self.gender
		deputy['data_nascimento'] = info_pessoal("Data de Nascimento:")

		def get_atuacao(contexto):
			return response.xpath(f'//a[@class="list-table__heading" and text()="{contexto}"]/following-sibling::dl').get()

		atuacao_plenario = get_atuacao("em Plenário")
		atuacao_comissao = get_atuacao("em comissões")

		def atuacao_by_column(contexto, column_text):
			value = Selector(text=contexto).xpath(f'//dt[contains(text(), "{column_text}")]/following-sibling::dd/text()').get()
			return value.replace("\n", "").strip().split(" ")[0]
		
		deputy['presença_plenario'] = atuacao_by_column(atuacao_plenario, "Presenças")
		deputy['ausencia_justificada_plenario'] = atuacao_by_column(atuacao_plenario, "Ausências justificadas")
		deputy['ausencia_plenario'] = atuacao_by_column(atuacao_plenario, "Ausências não justificadas")
		deputy['presença_comissao'] = atuacao_by_column(atuacao_comissao, "Presenças")
		deputy['ausencia_justificada_comissao'] = atuacao_by_column(atuacao_comissao, "Ausências justificadas")
		deputy['ausencia_comissao'] = atuacao_by_column(atuacao_comissao, "Ausências não justificadas")
		
		def recurso_gasto(recurso):
			return response.xpath(f'//h3[text()="{recurso}"]/following-sibling::div').get()

		verba_par = recurso_gasto("Cota parlamentar ")
		verba_gab = recurso_gasto("Verba de gabinete ")

		def salario_to_float(salario):
			if (salario is None):
				return 'NaN'
			return float(salario.replace("R$", "").replace(".", "").replace(",", "."))

		def percetual_gasto(verba, gasto):
			percentuais = Selector(text=verba).xpath('//div/p[contains(text(), "Percentual gasto")]/following-sibling::table/tbody').get()
			return salario_to_float(Selector(text=percentuais).xpath(f'//td[text()="{gasto}"]/following-sibling::td/text()').get())
		
		deputy['gasto_total_par'] = percetual_gasto(verba_par, "Total Gasto")

		meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

		def gastos_mensais(verba, mes):
			gastos_mensais = Selector(text=verba).xpath('//div/p[contains(text(), "Gasto mensal")]/following-sibling::table/tbody').get()
			return salario_to_float(Selector(text=gastos_mensais).xpath(f'//td[text()="{mes}"]/following-sibling::td/text()').get())

		for mes in meses:
			key = f'gasto_{mes.lower()}_par'
			deputy[key] = gastos_mensais(verba_par, mes)
		
		deputy['salario_bruto_par'] = deputy['gasto_total_par'] + percetual_gasto(verba_par, "Total Disponível")
		
		deputy['gasto_total_gab'] = percetual_gasto(verba_gab, "Total Gasto")

		for mes in meses:
			key = f'gasto_{mes.lower()}_gab'
			deputy[key] = gastos_mensais(verba_gab, mes)

		deputy['salario_bruto'] = salario_to_float(response.xpath(f'//h3[text()="Salário mensal bruto "]/following-sibling::a[@class="beneficio__info"]/text()').get())

		deputy['quant_viagem'] = response.xpath('//div[@class="beneficio beneficio__viagens"]/span/text()').get()
		if (deputy['quant_viagem'] is None):
			deputy['quant_viagem'] = response.xpath('//div[@class="beneficio beneficio__viagens"]/a[@class="beneficio__info"]/text()').get()

		deputy['avatar'] = response.xpath('//img[@class="foto-deputado__imagem"]/@src').get()

		return deputy