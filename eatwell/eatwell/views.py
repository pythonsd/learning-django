from django.views.generic import TemplateView


class Contact(TemplateView):

    """Page stating our contact information"""

    template_name = 'contact.html'

    def get_context_data(self):
        return {'title': "Contact Us"}

contact = Contact.as_view()


class Home(TemplateView):

    """EatWell homepage"""

    template_name = 'home.html'

    def get_context_data(self):
        return {'title': "Home"}

home = Home.as_view()