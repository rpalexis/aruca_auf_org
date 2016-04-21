from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Contact
from forms import ContactForm

class InscriptionCPlugin(CMSPluginBase):
    # model = Contact
    name = _("Inscription Chercheurs")
    render_template = "inscriptionC.html"

    def render(self, context, instance, placeholder):
	request = context['request']

	if request.method == "POST":
		print("I'm in the post from InscriptionPostPlugin")
			return context
	# else:
	# 	form = ContactForm()
    #     context.update({
	# 	'contact': instance,
	# 	'form': form,
    #     	})
    #     return context

plugin_pool.register_plugin(testPlugin)
