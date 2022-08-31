from .latex import JSON_to_LaTeX, render_jinja

def APS_export(text, configuration):
	document=JSON_to_LaTeX(text)
	return render_jinja("latex/APS/Physical_Review.tex", document=document, values=configuration['project']['values'])

	