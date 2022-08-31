from .latex import JSON_to_LaTeX, render_jinja

def Springer_export(text, configuration):
	document=JSON_to_LaTeX(text)
	return render_jinja("latex/Springer/Pramana.tex", document=document, values=configuration['project']['values'])

	